"""Scriptlerin modeli çağırdığı TEK kapı: `claude -p` (Pro limitinden) + bütçe kaydı.

Kullanım:
  python araclar/claude_calistir.py --departman medya --is "başlık yaz" --model haiku "istem metni"
  python araclar/claude_calistir.py --departman instagram --model sonnet --klasor 60-ofisler/instagram "..."

Kurallar:
  - Departman payı %90'ı geçtiyse, --kritik verilmedikçe çalışmaz.
  - Opus sadece --patron-onayi ile ve Opus payı dolmadıysa çalışır (otomatik işler Opus çağıramaz).
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

from ortak import KOK
import butce_kaydet as butce


def calistir(istem, departman, is_adi, model="haiku", klasor=None, kritik=False,
             patron_onayi=False, ek_argumanlar=()):
    """Modeli çağırır; (cevap_metni, maliyet) döndürür. Kural ihlalinde RuntimeError."""
    ayar = butce.ayarlar()
    if butce.oran(departman) >= float(ayar["kritik_esigi"]) and not kritik:
        raise RuntimeError(f"{departman} haftalık payının %90'ını geçti; sadece kritik işler çalışır.")
    if butce.model_ailesi(model) == "opus":
        if not patron_onayi:
            raise RuntimeError("Opus sadece Patron onayıyla çağrılır (--patron-onayi).")
        if butce.opus_orani() >= 1.0:
            raise RuntimeError("Bu haftanın Opus payı doldu; Sonnet kullanın veya gelecek haftayı bekleyin.")

    claude = shutil.which("claude")
    if not claude:
        raise RuntimeError("`claude` komutu bulunamadı (Claude Code kurulu mu?).")
    komut = [claude, "-p", "--model", model, "--output-format", "json", *ek_argumanlar]
    ortam = dict(os.environ, MERKEZ_SCRIPT_CAGRISI="1")  # oturum kancası çift saymasın
    cikti = subprocess.run(komut, input=istem, capture_output=True, text=True,
                           encoding="utf-8", cwd=KOK / klasor if klasor else KOK, env=ortam)
    if cikti.returncode != 0 and not cikti.stdout.strip():
        raise RuntimeError(f"claude hata verdi: {cikti.stderr.strip()[:500]}")
    veri = json.loads(cikti.stdout)

    kullanim = veri.get("usage", {})
    giris = kullanim.get("input_tokens", 0) + kullanim.get("cache_creation_input_tokens", 0)
    onbellek = kullanim.get("cache_read_input_tokens", 0)
    cikis = kullanim.get("output_tokens", 0)
    maliyet = veri.get("total_cost_usd")
    if maliyet is None:
        maliyet = butce.maliyet_hesapla(model, giris, cikis, onbellek)
    butce.kaydet(departman, is_adi, model, giris, cikis, onbellek, maliyet, kaynak="claude-p")

    if veri.get("is_error"):
        raise RuntimeError(f"Model hata döndürdü: {veri.get('result', '')[:500]}")
    return veri.get("result", ""), maliyet


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="claude -p çağrısı + bütçe kaydı")
    p.add_argument("istem", help="modele gidecek metin (- verilirse stdin'den okunur)")
    p.add_argument("--departman", required=True)
    p.add_argument("--is", dest="is_adi", default="")
    p.add_argument("--model", default="haiku", choices=["haiku", "sonnet", "opus"])
    p.add_argument("--klasor", help="oturumun açılacağı klasör (proje köküne göre)")
    p.add_argument("--kritik", action="store_true")
    p.add_argument("--patron-onayi", action="store_true")
    a = p.parse_args()
    istem = sys.stdin.read() if a.istem == "-" else a.istem
    try:
        cevap, maliyet = calistir(istem, a.departman, a.is_adi or istem[:60], a.model,
                                  a.klasor, a.kritik, a.patron_onayi)
    except RuntimeError as hata:
        print(f"DURDURULDU: {hata}", file=sys.stderr)
        sys.exit(2)
    print(cevap)
    print(butce.durum_satiri(a.departman, maliyet), file=sys.stderr)
