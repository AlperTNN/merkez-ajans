"""Ortak yardımcılar: proje kökünü bulma, basit YAML ve not özelliklerini okuma.

Sadece Python standart kütüphanesi kullanılır (ek kurulum gerekmez).
YAML okuyucu bilinçli olarak basittir: "anahtar: deger" satırları ve
"[a, b]" biçimindeki tek satırlık listeler. İç içe yapılar desteklenmez.
"""
import os
import sys
from pathlib import Path

# Windows konsolunda Türkçe karakterler bozulmasın
for _akis in (sys.stdout, sys.stderr):
    try:
        _akis.reconfigure(encoding="utf-8")
    except Exception:
        pass


def kok_bul(baslangic=None):
    """CLAUDE.md ve 00-yonetim/ içeren ilk üst klasörü döndürür."""
    if os.environ.get("MERKEZ_KOK"):
        return Path(os.environ["MERKEZ_KOK"])
    yol = Path(baslangic or __file__).resolve()
    for aday in [yol, *yol.parents]:
        if (aday / "CLAUDE.md").exists() and (aday / "00-yonetim").is_dir():
            return aday
    raise SystemExit("Proje kökü bulunamadı (CLAUDE.md + 00-yonetim/ yok).")


KOK = kok_bul()


def _deger_coz(ham):
    ham = ham.strip()
    # Satır sonu yorumunu at (tırnak dışındaysa)
    if not ham.startswith(("'", '"')) and " #" in ham:
        ham = ham.split(" #", 1)[0].strip()
    if ham.startswith("[") and ham.endswith("]"):
        ic = ham[1:-1].strip()
        return [_deger_coz(p) for p in ic.split(",")] if ic else []
    if len(ham) >= 2 and ham[0] == ham[-1] and ham[0] in "'\"":
        return ham[1:-1]
    try:
        return int(ham)
    except ValueError:
        pass
    try:
        return float(ham)
    except ValueError:
        return ham


def yaml_metni_oku(metin):
    """Düz "anahtar: deger" satırlarını sözlüğe çevirir; girintili satırları atlar."""
    sonuc = {}
    for satir in metin.splitlines():
        if not satir.strip() or satir.lstrip().startswith("#") or satir[0] in " \t-":
            continue
        if ":" not in satir:
            continue
        anahtar, deger = satir.split(":", 1)
        sonuc[anahtar.strip()] = _deger_coz(deger)
    return sonuc


def yaml_oku(yol):
    return yaml_metni_oku(Path(yol).read_text(encoding="utf-8"))


def ozellik_oku(yol):
    """Markdown notunun başındaki --- ... --- özellik bloğunu okur."""
    metin = Path(yol).read_text(encoding="utf-8")
    if not metin.startswith("---"):
        return {}
    parcalar = metin.split("---", 2)
    return yaml_metni_oku(parcalar[1]) if len(parcalar) >= 3 else {}


def ozellik_yaz(yol, anahtar, deger):
    """Özellik bloğundaki tek bir satırı günceller (yoksa ekler)."""
    yol = Path(yol)
    satirlar = yol.read_text(encoding="utf-8").splitlines(keepends=True)
    if not satirlar or not satirlar[0].startswith("---"):
        raise ValueError(f"{yol} dosyasında özellik bloğu yok")
    for i in range(1, len(satirlar)):
        if satirlar[i].startswith("---"):
            satirlar.insert(i, f"{anahtar}: {deger}\n")
            break
        if satirlar[i].split(":", 1)[0].strip() == anahtar:
            satirlar[i] = f"{anahtar}: {deger}\n"
            break
    yol.write_text("".join(satirlar), encoding="utf-8")
