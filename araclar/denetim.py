"""Denetim scripti: modülerlik ve marka kurallarını kontrol eder, hiçbir şeyi değiştirmez.

Kontroller:
  1. Bir modülün adı başka bir modülün (eklenti veya ofis) içinde geçiyor mu?
  2. Marka adı kimlik.yaml dışında sabit yazılmış mı?
  3. aktif-moduller.md, moduller/, 60-ofisler/ ve marketplace.json tutarlı mı?

Kullanım: python araclar/denetim.py      (uyarı varsa çıkış kodu 1)
"""
import json
import re
import sys

from ortak import KOK, ozellik_oku, yaml_oku

METIN_UZANTILARI = {".md", ".yaml", ".yml", ".json", ".py", ".csv", ".txt", ".base", ".canvas"}
MARKA_HARIC = {".git", ".obsidian", "arsiv", ".durum", "__pycache__"}
MARKA_HARIC_DOSYALAR = {KOK / "10-marka" / "kimlik.yaml", KOK / "PROJE-BRIEF.md"}


def metin_dosyalari(klasor, haric=MARKA_HARIC):
    for yol in klasor.rglob("*"):
        if yol.is_file() and yol.suffix.lower() in METIN_UZANTILARI \
                and not any(p in haric for p in yol.relative_to(KOK).parts):
            yield yol


def oku(yol):
    try:
        return yol.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return ""


def modul_adlari():
    """moduller/ altındaki gerçek modüller (_ ile başlayan şablonlar ve gizli klasörler hariç)."""
    klasor = KOK / "moduller"
    return sorted(d.name for d in klasor.iterdir()
                  if d.is_dir() and not d.name.startswith(("_", ".")))


def ofis_adlari():
    klasor = KOK / "60-ofisler"
    return sorted(d.name for d in klasor.iterdir() if d.is_dir() and not d.name.startswith("."))


def kontrol_capraz_atif(uyarilar):
    adlar = sorted(set(modul_adlari()) | set(ofis_adlari()))
    for modul in adlar:
        klasorler = [KOK / "moduller" / modul, KOK / "60-ofisler" / modul]
        digerleri = [a for a in adlar if a != modul]
        if not digerleri:
            continue
        # Tire de adın parçası sayılır: "deneme-iki" içinde "deneme" geçmiş sayılmaz
        desen = re.compile(r"(?<![\w-])(" + "|".join(map(re.escape, digerleri)) + r")(?![\w-])",
                           re.IGNORECASE)
        for klasor in klasorler:
            if not klasor.is_dir():
                continue
            for yol in metin_dosyalari(klasor):
                for no, satir in enumerate(oku(yol).splitlines(), 1):
                    bulunan = desen.search(satir)
                    if bulunan:
                        uyarilar.append(f"[çapraz atıf] {yol.relative_to(KOK)}:{no} "
                                        f"'{bulunan.group(0)}' modülünü anıyor")


def kontrol_marka_adi(uyarilar):
    marka = str(yaml_oku(KOK / "10-marka" / "kimlik.yaml").get("marka_adi", "")).strip()
    if not marka:
        uyarilar.append("[marka] kimlik.yaml içinde marka_adi boş")
        return
    desen = re.compile(re.escape(marka), re.IGNORECASE)
    for yol in metin_dosyalari(KOK):
        if yol in MARKA_HARIC_DOSYALAR:
            continue
        for no, satir in enumerate(oku(yol).splitlines(), 1):
            if desen.search(satir):
                uyarilar.append(f"[marka] {yol.relative_to(KOK)}:{no} marka adı sabit yazılmış")


def kontrol_tutarlilik(uyarilar):
    aktif = ozellik_oku(KOK / "00-yonetim" / "aktif-moduller.md").get("moduller", [])
    aktif = set(aktif if isinstance(aktif, list) else [aktif])
    moduller, ofisler = set(modul_adlari()), set(ofis_adlari())
    try:
        pazar = json.loads((KOK / "moduller" / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        pazar_adlari = {e["name"] for e in pazar.get("plugins", [])}
    except (OSError, ValueError, KeyError) as hata:
        uyarilar.append(f"[tutarlılık] marketplace.json okunamadı: {hata}")
        pazar_adlari = set()

    for ad in sorted(aktif - moduller):
        uyarilar.append(f"[tutarlılık] '{ad}' aktif listede ama moduller/ içinde yok")
    for ad in sorted(aktif - ofisler):
        uyarilar.append(f"[tutarlılık] '{ad}' aktif listede ama 60-ofisler/ içinde ofisi yok")
    for ad in sorted((moduller | ofisler) - aktif):
        uyarilar.append(f"[tutarlılık] '{ad}' klasörü var ama aktif listede değil (kalıntı?)")
    for ad in sorted(aktif ^ pazar_adlari):
        uyarilar.append(f"[tutarlılık] '{ad}' aktif liste ile marketplace.json arasında uyumsuz")


def ana():
    uyarilar = []
    kontrol_capraz_atif(uyarilar)
    kontrol_marka_adi(uyarilar)
    kontrol_tutarlilik(uyarilar)
    if uyarilar:
        print(f"Denetim: {len(uyarilar)} uyarı")
        for u in uyarilar:
            print("  - " + u)
        return 1
    print("Denetim: temiz ✓")
    return 0


if __name__ == "__main__":
    sys.exit(ana())
