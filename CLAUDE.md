# Şirket anayasası

Bu klasör hem bir el işi markasının yapay zekâ ajansı hem de Obsidian kasasıdır. Herkes (CEO, müdür, işçi) bu kurallara uyar.

## Dil ve iletişim
- Her şey sade Türkçe. Patron yeni başlıyor: teknik adımı gerekçesiyle anlat.
- İletişim dosyayla: iş emri → `gelen-kutusu/`, kısa rapor → `raporlar/`. Şablonlar `00-yonetim/sablonlar/`.

## Token ekonomisi
- Önce script (0 token), sonra skill, en son ajan.
- Bir klasöre girince önce `_dizin.md`'yi oku; sadece gereken dosyayı aç. Klasör taramak yerine `[[bağlantıları]]` takip et.
- Dosyanın önce özelliklerini (YAML) oku; metne gerekirse geç.
- Görsellere bakma; `30-medya/medya-indeksi.csv` açıklamasını oku.
- Model: işçiler Haiku, müdür/CEO Sonnet. **Opus sadece `/danisman` ile ve Patron onayıyla.** Hiçbir otomatik iş Opus çağıramaz.
- Script içinden model çağrısı sadece `araclar/claude_calistir.py` ile (bütçe defterine yazar). Anthropic API kullanılmaz.

## Marka
- Marka adını hiçbir yere sabit yazma; `10-marka/kimlik.yaml`'dan oku.
- Önce `10-marka/marka-ozeti.md`; detaylar `10-marka/detay/` (sadece gerekirse).
- `10-marka/` sadece Patron tarafından değiştirilir.
- İçerikte annenin **yüzü asla görünmez**; **üretim sırrı gösterilmez**. Üretim kesitleri gerçek çekimdir; yapay zekâyla sahte üretim videosu yapılmaz.

## Yazma bölgeleri
- Her departman sadece kendi `60-ofisler/<departman>/` klasörüne ve ortak alanda kendine ayrılan yere yazar: temsilci → `40-veri-odasi/raporlar/`, gözcü → `40-veri-odasi/fikir-kartlari/`, stüdyo → `30-medya/`.
- Departmanlar birbirinin adını anmaz, klasörüne bakmaz. Bağımlılık `00-yonetim/aktif-moduller.md`'deki yeteneklerle kurulur.
- `arsiv/` ve `.obsidian/` okunmaz.

## Adlandırma
- Tarih `YYYY-AA-GG`. Dosya/klasör adı: küçük harf, tire, Türkçe karakter ve boşluk yok.

## Kalıcı değişiklik
- Skill/kural değişikliği: müdür önerir, **Patron onaylar**. Öğrenilenler `60-ofisler/<departman>/ogrenme/` altında.
