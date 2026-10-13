---
description: Departman modülünü kaldırır ve arşive taşır
argument-hint: <modul-adi>
model: haiku
---

Modülü kaldır: $ARGUMENTS

1. Patron'a onaylat: "<ad> modülü kaldırılacak, dosyaları arsiv/ altına taşınacak. Devam?"
2. Onay gelirse çalıştır: `python araclar/modul.py kaldir <ad>`
3. Script çıktısındaki "Sıradaki adımlar"ı Patron'a aktar (`/plugin uninstall ...` komutunu Patron yazacak).
4. `python araclar/denetim.py` çalıştır; kalıntı uyarısı varsa bildir.
