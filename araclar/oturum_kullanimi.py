"""Claude Code "Stop" kancası: etkileşimli oturumun harcamasını bütçe defterine yazar.

Her cevaptan sonra çalışır, oturum kaydındaki (transcript) YENİ mesajların token
kullanımını toplar ve deftere tek satır ekler; kullanıcıya durum satırı gösterir.
Ölçüm yaklaşıktır. Asla hata vermez (oturumu bozmasın diye).
claude_calistir.py'nin açtığı oturumlar zaten kaydedildiği için atlanır.
"""
import json
import os
import sys
from pathlib import Path


def ana():
    if os.environ.get("MERKEZ_SCRIPT_CAGRISI"):
        return
    sys.stdin.reconfigure(encoding="utf-8")
    girdi = json.load(sys.stdin)
    kayit_yolu = Path(girdi.get("transcript_path", ""))
    if not kayit_yolu.is_file():
        return

    sys.path.insert(0, str(Path(__file__).parent))
    from ortak import KOK
    import butce_kaydet as butce

    durum_klasoru = KOK / "araclar" / ".durum"
    durum_klasoru.mkdir(exist_ok=True)
    durum_dosyasi = durum_klasoru / f"{girdi.get('session_id', 'oturum')}.json"
    durum = json.loads(durum_dosyasi.read_text(encoding="utf-8")) if durum_dosyasi.exists() else {}
    islenen_satir = durum.get("satir", 0)
    gorulen = set(durum.get("son_idler", []))

    satirlar = kayit_yolu.read_text(encoding="utf-8").splitlines()
    toplamlar = {}  # model -> [giris, cikis, onbellek_okuma, onbellek_yazma]
    yeni_idler = []
    for satir in satirlar[islenen_satir:]:
        try:
            olay = json.loads(satir)
        except ValueError:
            continue
        mesaj = olay.get("message") or {}
        kullanim = mesaj.get("usage")
        if olay.get("type") != "assistant" or not kullanim:
            continue
        mesaj_id = mesaj.get("id")
        if mesaj_id in gorulen:  # aynı mesaj birden çok satıra bölünebilir
            continue
        gorulen.add(mesaj_id)
        yeni_idler.append(mesaj_id)
        t = toplamlar.setdefault(mesaj.get("model", "sonnet"), [0, 0, 0, 0])
        t[0] += kullanim.get("input_tokens", 0)
        t[1] += kullanim.get("output_tokens", 0)
        t[2] += kullanim.get("cache_read_input_tokens", 0)
        t[3] += kullanim.get("cache_creation_input_tokens", 0)

    durum_dosyasi.write_text(json.dumps({"satir": len(satirlar), "son_idler": yeni_idler[-50:]}),
                             encoding="utf-8")
    if not toplamlar:
        return

    # Departman: oturum bir ofis klasöründe açıldıysa o ofis, değilse CEO
    departman = "ceo"
    try:
        goreli = Path(girdi.get("cwd", "")).resolve().relative_to(KOK)
        if goreli.parts[:1] == ("60-ofisler",) and len(goreli.parts) > 1:
            departman = goreli.parts[1]
    except ValueError:
        pass

    toplam_maliyet = 0.0
    for model, (g, c, oo, oy) in toplamlar.items():
        maliyet = butce.maliyet_hesapla(model, g, c, oo, oy)
        toplam_maliyet += maliyet
        butce.kaydet(departman, "etkilesimli oturum", model, g + oy, c, oo, maliyet, kaynak="oturum")
    print(json.dumps({"systemMessage": butce.durum_satiri(departman, toplam_maliyet)},
                     ensure_ascii=False))


if __name__ == "__main__":
    try:
        ana()
    except Exception:
        pass
    sys.exit(0)
