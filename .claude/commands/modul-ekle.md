---
description: Yeni departman modülü ekler (şablondan)
argument-hint: <modul-adi> [açıklama]
model: haiku
---

Yeni modül ekle: $ARGUMENTS

1. Modül adını al (küçük harf, tire, Türkçe karakter yok). Belirsizse Patron'a sor.
2. Çalıştır: `python araclar/modul.py ekle <ad> --aciklama "<açıklama>"`
3. Script çıktısındaki "Sıradaki adımlar"ı Patron'a sade Türkçe aktar. Eklentiyi kurma komutlarını (`/plugin ...`) Patron'un kendisi yazacak.
4. `python araclar/denetim.py` çalıştır ve sonucu bildir.

Platform kurallarını (skills/platform-kurallari) bu komutta doldurma; ayrı bir iş emriyle yapılır.
