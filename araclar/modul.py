"""Modül (departman) ekleme / kaldırma — kuralı belli iş olduğu için script (0 token).

Kullanım:
  python araclar/modul.py ekle instagram --aciklama "Instagram departmanı"
  python araclar/modul.py kaldir instagram
  python araclar/modul.py liste

Ekle:   şablonu kopyalar ({{departman}} yer tutucusunu doldurur) → ofis klasörünü açar →
        marketplace.json ve aktif-moduller.md'ye ekler.
Kaldır: listelerden siler → modül ve ofis klasörünü arsiv/ altına taşır.
Eklentinin Claude Code'a kurulması/kaldırılması ekranda yazan /plugin komutuyla yapılır.
"""
import argparse
import json
import re
import shutil
import sys
from datetime import date

from ortak import KOK, ozellik_oku, ozellik_yaz

MODULLER = KOK / "moduller"
SABLON = MODULLER / "_sablon"
OFIS_SABLONU = MODULLER / "_ofis-sablonu"
OFISLER = KOK / "60-ofisler"
PAZAR = MODULLER / ".claude-plugin" / "marketplace.json"
AKTIF = KOK / "00-yonetim" / "aktif-moduller.md"
PAZAR_ADI = "merkez-moduller"


def _pazar_oku():
    return json.loads(PAZAR.read_text(encoding="utf-8"))


def _pazar_yaz(veri):
    PAZAR.write_text(json.dumps(veri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _aktif_liste():
    deger = ozellik_oku(AKTIF).get("moduller", [])
    return deger if isinstance(deger, list) else [deger]


def _aktif_yaz(liste):
    ozellik_yaz(AKTIF, "moduller", "[" + ", ".join(sorted(liste)) + "]")


def _yer_tutucu_doldur(klasor, ad):
    for yol in klasor.rglob("*"):
        if yol.is_file():
            try:
                metin = yol.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if "{{departman}}" in metin:
                yol.write_text(metin.replace("{{departman}}", ad), encoding="utf-8")


def ekle(ad, aciklama):
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", ad):
        sys.exit("Modül adı küçük harf/rakam ve tire olmalı (Türkçe karakter yok), ör. instagram")
    hedef, ofis = MODULLER / ad, OFISLER / ad
    if hedef.exists() or ofis.exists():
        sys.exit(f"'{ad}' zaten var.")
    shutil.copytree(SABLON, hedef)
    shutil.copytree(OFIS_SABLONU, ofis)
    _yer_tutucu_doldur(hedef, ad)
    _yer_tutucu_doldur(ofis, ad)

    pazar = _pazar_oku()
    pazar["plugins"].append({"name": ad, "source": f"./{ad}", "description": aciklama or f"{ad} departmanı"})
    _pazar_yaz(pazar)
    _aktif_yaz(set(_aktif_liste()) | {ad})

    print(f"'{ad}' modülü hazırlandı: moduller/{ad}/ ve 60-ofisler/{ad}/")
    print("Sıradaki adımlar:")
    print(f"  1. moduller/{ad}/MODUL.md ve skills/ içine platform kurallarını doldur")
    print("  2. Claude Code'da eklentiyi kur:")
    print("       /plugin marketplace add ./moduller      (sadece ilk seferde)")
    print(f"       /plugin install {ad}@{PAZAR_ADI}")
    print("  3. Gerekiyorsa aktif-moduller.md'deki yetenekleri güncelle (ör. meta_hesabi: acik)")
    print("  4. python araclar/denetim.py")


def kaldir(ad):
    hedef, ofis = MODULLER / ad, OFISLER / ad
    if ad.startswith("_") or not (hedef.exists() or ofis.exists() or ad in _aktif_liste()):
        sys.exit(f"'{ad}' adında modül yok.")
    pazar = _pazar_oku()
    pazar["plugins"] = [e for e in pazar["plugins"] if e.get("name") != ad]
    _pazar_yaz(pazar)
    _aktif_yaz(set(_aktif_liste()) - {ad})

    arsiv = KOK / "arsiv" / f"{date.today().isoformat()}_{ad}"
    arsiv.mkdir(parents=True, exist_ok=True)
    for kaynak, alt in ((hedef, "modul"), (ofis, "ofis")):
        if kaynak.exists():
            shutil.move(str(kaynak), str(arsiv / alt))

    print(f"'{ad}' kaldırıldı; dosyalar {arsiv.relative_to(KOK)}/ altında.")
    print("Sıradaki adımlar:")
    print(f"  1. Claude Code'da eklentiyi kaldır: /plugin uninstall {ad}@{PAZAR_ADI}")
    print("  2. Bu modüle bağlı yetenekleri aktif-moduller.md'de 'kapali' yap")
    print("  3. python araclar/denetim.py")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Modül ekle/kaldır")
    alt = p.add_subparsers(dest="komut", required=True)
    e = alt.add_parser("ekle")
    e.add_argument("ad")
    e.add_argument("--aciklama", default="")
    k = alt.add_parser("kaldir")
    k.add_argument("ad")
    alt.add_parser("liste")
    a = p.parse_args()
    if a.komut == "ekle":
        ekle(a.ad, a.aciklama)
    elif a.komut == "kaldir":
        kaldir(a.ad)
    else:
        print("Aktif modüller:", ", ".join(_aktif_liste()) or "(yok)")
