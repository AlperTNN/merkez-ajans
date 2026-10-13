"""Bütçe defteri: her yapay zekâ çağrısını kaydeder ve durum satırı üretir.

Kullanım:
  python araclar/butce_kaydet.py --durum                 # şirket durumu
  python araclar/butce_kaydet.py --durum --departman ceo # departman durumu

Diğer scriptler kaydet() ve durum_satiri() fonksiyonlarını içe aktarır.
Maliyet "API karşılığı" tahmini USD'dir; Pro'da gerçek ödeme değildir, göreli ölçüdür.
"""
import argparse
import csv
from datetime import date, datetime

from ortak import KOK, yaml_oku

DEFTER = KOK / "00-yonetim" / "butce-defteri.csv"
AYARLAR = KOK / "00-yonetim" / "butce-ayarlari.yaml"
ALANLAR = ["tarih", "saat", "departman", "is", "model", "giris_token",
           "cikis_token", "onbellek_token", "maliyet_usd", "kaynak"]

# Milyon token başına tahmini USD (giriş, çıkış). Fiyatlar değişirse buradan güncellenir.
FIYATLAR = {"haiku": (1.0, 5.0), "sonnet": (3.0, 15.0), "opus": (5.0, 25.0)}


def model_ailesi(model):
    model = (model or "").lower()
    for aile in FIYATLAR:
        if aile in model:
            return aile
    return "sonnet"


def maliyet_hesapla(model, giris, cikis, onbellek_okuma=0, onbellek_yazma=0):
    g, c = FIYATLAR[model_ailesi(model)]
    return (giris * g + cikis * c + onbellek_okuma * g * 0.1 + onbellek_yazma * g * 1.25) / 1e6


def ayarlar():
    return yaml_oku(AYARLAR)


def departman_payi(departman, ayar=None):
    ayar = ayar or ayarlar()
    return float(ayar.get(f"pay_{departman}", ayar.get("pay_diger", 2.0)))


def _hafta(tarih_metni):
    return date.fromisoformat(tarih_metni).isocalendar()[:2]


def bu_haftanin_kayitlari():
    if not DEFTER.exists():
        return []
    bu_hafta = date.today().isocalendar()[:2]
    with DEFTER.open(encoding="utf-8", newline="") as f:
        return [s for s in csv.DictReader(f) if s.get("tarih") and _hafta(s["tarih"]) == bu_hafta]


def harcama(departman=None, aile=None):
    toplam = 0.0
    for s in bu_haftanin_kayitlari():
        if departman and s["departman"] != departman:
            continue
        if aile and model_ailesi(s["model"]) != aile:
            continue
        toplam += float(s["maliyet_usd"] or 0)
    return toplam


def kaydet(departman, is_adi, model, giris=0, cikis=0, onbellek=0, maliyet=None, kaynak="script"):
    if maliyet is None:
        maliyet = maliyet_hesapla(model, giris, cikis)
    yeni = not DEFTER.exists() or DEFTER.stat().st_size == 0
    with DEFTER.open("a", encoding="utf-8", newline="") as f:
        yazici = csv.DictWriter(f, fieldnames=ALANLAR)
        if yeni:
            yazici.writeheader()
        simdi = datetime.now()
        yazici.writerow({
            "tarih": simdi.date().isoformat(), "saat": simdi.strftime("%H:%M"),
            "departman": departman, "is": is_adi.replace("\n", " ")[:80], "model": model,
            "giris_token": giris, "cikis_token": cikis, "onbellek_token": onbellek,
            "maliyet_usd": f"{maliyet:.4f}", "kaynak": kaynak,
        })
    return maliyet


def oran(departman):
    return harcama(departman) / departman_payi(departman)


def opus_orani():
    ayar = ayarlar()
    pay = float(ayar["sirket_haftalik_pay"]) * float(ayar["opus_payi_orani"])
    return harcama(aile="opus") / pay


def durum_satiri(departman=None, bu_is=None):
    ayar = ayarlar()
    sirket_pay = float(ayar["sirket_haftalik_pay"])
    sirket = harcama()
    parcalar = []
    if bu_is is not None:
        parcalar.append(f"Bu iş: ${bu_is:.3f}")
    if departman:
        pay = departman_payi(departman, ayar)
        dep = harcama(departman)
        parcalar.append(f"{departman} bu hafta: ${dep:.2f}/{pay:.0f} (%{dep / pay * 100:.0f})")
    parcalar.append(f"Şirket: ${sirket:.2f}/{sirket_pay:.0f} (%{sirket / sirket_pay * 100:.0f})")
    parcalar.append(f"Opus payı: %{opus_orani() * 100:.0f}")
    satir = " · ".join(parcalar)
    en_yuksek = max(sirket / sirket_pay, oran(departman) if departman else 0)
    if en_yuksek >= float(ayar["kritik_esigi"]):
        satir += "  ⛔ %90 aşıldı: sadece kritik işler"
    elif en_yuksek >= float(ayar["uyari_esigi"]):
        satir += "  ⚠ %70 aşıldı"
    return satir


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Bütçe defteri durumu")
    p.add_argument("--durum", action="store_true", help="bu haftanın durum satırını yaz")
    p.add_argument("--departman")
    a = p.parse_args()
    print(durum_satiri(a.departman))
