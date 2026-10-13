"""Müdür Asistanı (script, 0 token): gelen kutusundaki iş emirlerini karşılar.

Rutin iş → tanımlı script işçisi çalışır, müdür hiç açılmaz.
İstisna → Müdür (Sonnet) ofis klasöründe ayrı oturum olarak başlatılır.

Müdürü çağırma kuralları (brif Bölüm 5):
  1. İş emri "rutin" değilse
  2. Bir işçi hata verdiyse (hata_sayisi > 0)
  3. Marka bekçisi iki kez reddettiyse (ret_sayisi >= 2)
  4. Departman bütçe payının %70'ine ulaştıysa
  5. Patron/CEO açıkça istediyse (mudur_iste: evet)

Kullanım:
  python moduller/{{departman}}/scripts/asistan.py             # sadece ne yapacağını söyler
  python moduller/{{departman}}/scripts/asistan.py --calistir  # gerçekten yürütür
"""
import argparse
import os
import sys
from pathlib import Path

DEPARTMAN = "{{departman}}"


def _kok():
    if os.environ.get("MERKEZ_KOK"):
        return Path(os.environ["MERKEZ_KOK"])
    for baslangic in (Path(__file__).resolve(), Path.cwd().resolve()):
        for aday in [baslangic, *baslangic.parents]:
            if (aday / "CLAUDE.md").exists() and (aday / "00-yonetim").is_dir():
                return aday
    sys.exit("Proje kökü bulunamadı; proje klasöründen çalıştırın veya MERKEZ_KOK ayarlayın.")


KOK = _kok()
sys.path.insert(0, str(KOK / "araclar"))
from ortak import ozellik_oku, ozellik_yaz  # noqa: E402
import butce_kaydet as butce  # noqa: E402
import claude_calistir  # noqa: E402

OFIS = KOK / "60-ofisler" / DEPARTMAN
GELEN = OFIS / "gelen-kutusu"

# Rutin işler: is_kodu -> fonksiyon(emir_yolu, ozellikler). Faz 3'te doldurulur.
RUTIN_ISLER = {}


def mudur_gerekcesi(oz):
    """Müdür gerekiyorsa gerekçeyi, gerekmiyorsa None döndürür."""
    if oz.get("is_turu") != "rutin":
        return "iş emri rutin değil"
    if int(oz.get("hata_sayisi") or 0) > 0:
        return "işçi hata verdi"
    if int(oz.get("ret_sayisi") or 0) >= 2:
        return "marka bekçisi iki kez reddetti"
    if butce.oran(DEPARTMAN) >= float(butce.ayarlar()["uyari_esigi"]):
        return "departman bütçesi %70'e ulaştı"
    if str(oz.get("mudur_iste", "")).lower() in ("evet", "true"):
        return "Patron/CEO müdürü istedi"
    if oz.get("is_kodu") not in RUTIN_ISLER:
        return "bu rutin iş için tanımlı script yok"
    return None


def mudur_cagir(emir):
    istem = (f"Gelen kutusundaki iş emrini işle: gelen-kutusu/{emir.name}. "
             "Önce CLAUDE.md'deki görev tanımını uygula; işi işçilere dağıt, "
             "sonunda raporlar/ klasörüne kısa rapor yaz.")
    cevap, maliyet = claude_calistir.calistir(
        istem, DEPARTMAN, f"müdür: {emir.stem}", model="sonnet",
        klasor=f"60-ofisler/{DEPARTMAN}",
        kritik=str(ozellik_oku(emir).get("oncelik")) == "kritik",
        ek_argumanlar=["--permission-mode", "acceptEdits"])
    return cevap, maliyet


def ana():
    p = argparse.ArgumentParser(description=f"{DEPARTMAN} müdür asistanı")
    p.add_argument("--calistir", action="store_true", help="gerçekten yürüt (yoksa sadece plan)")
    a = p.parse_args()

    emirler = sorted(y for y in GELEN.glob("*.md") if ozellik_oku(y).get("durum") == "acik")
    if not emirler:
        print(f"[{DEPARTMAN}] açık iş emri yok.")
        return
    for emir in emirler:
        oz = ozellik_oku(emir)
        gerekce = mudur_gerekcesi(oz)
        hedef = f"MÜDÜR ({gerekce})" if gerekce else f"rutin script: {oz.get('is_kodu')}"
        print(f"[{DEPARTMAN}] {emir.name} → {hedef}")
        if not a.calistir:
            continue
        ozellik_yaz(emir, "durum", "surmekte")
        try:
            if gerekce:
                cevap, maliyet = mudur_cagir(emir)
                print(cevap)
            else:
                RUTIN_ISLER[oz["is_kodu"]](emir, oz)
                maliyet = 0.0
            ozellik_yaz(emir, "durum", "bitti")
        except Exception as hata:  # işçi hatası → bir sonraki turda müdüre gider
            ozellik_yaz(emir, "durum", "acik")
            ozellik_yaz(emir, "hata_sayisi", int(oz.get("hata_sayisi") or 0) + 1)
            print(f"  HATA: {hata}", file=sys.stderr)
            continue
        print("  " + butce.durum_satiri(DEPARTMAN, maliyet))


if __name__ == "__main__":
    ana()
