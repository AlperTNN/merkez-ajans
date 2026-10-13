---
tur: modul
ad: {{departman}}
surum: 0.1.0
durum: hazirlaniyor     # hazirlaniyor | aktif
gerekli_yetenekler: []  # ör. [meta_hesabi] — başka modülün adı yazılmaz
saglanan_yetenekler: [] # ör. [meta_hesabi] — açılınca aktif-moduller.md'de "acik" yapılır
mcp: []                 # bu departmana özel MCP'ler (.mcp.json)
---

# {{departman}} — modül kimlik kartı

## Okur
- `10-marka/marka-ozeti.md` (gerekirse `10-marka/detay/`)
- `20-urunler/` (ürün özellikleri)
- `30-medya/medya-indeksi.csv`
- `60-ofisler/{{departman}}/gelen-kutusu/`

## Yazar
- `60-ofisler/{{departman}}/` (asıl çalışma)
- `40-veri-odasi/raporlar/YYYY-AA-GG_{{departman}}.md` (temsilci)
- `40-veri-odasi/fikir-kartlari/` (gözcü)

## Ekip
| rol | tür | model |
|---|---|---|
| Müdür Asistanı | script (`scripts/asistan.py`) | — |
| Müdür | ofis `CLAUDE.md`, sadece istisnada | Sonnet |
| Uygulayıcı | ajan (`agents/uygulayici.md`) | Haiku |
| Temsilci | ajan (`agents/temsilci.md`) | Haiku |
| Gözcü | ajan (`agents/gozcu.md`) | Haiku |
| Görsel uzmanı | script (`scripts/gorsel_uzmani.py`) | — |

## Platform kuralları
`skills/platform-kurallari/SKILL.md` (ölçüler, hashtag, başlık, format, paylaşım saatleri).
