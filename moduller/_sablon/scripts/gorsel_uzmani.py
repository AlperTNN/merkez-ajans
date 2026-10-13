"""Görsel uzmanı (script işçi, 0 token): medya deposundaki görseli platform ölçüsüne getirir.

Faz 2'de (Medya Stüdyosu) doldurulacak: Pillow ile boyutlandırma/kırpma, ffmpeg ile video kırpma.
Ölçüler `skills/platform-kurallari/SKILL.md` tablosundan alınır.
"""
import sys

DEPARTMAN = "{{departman}}"

if __name__ == "__main__":
    print(f"[{DEPARTMAN}] görsel uzmanı henüz hazır değil (Faz 2).", file=sys.stderr)
    sys.exit(1)
