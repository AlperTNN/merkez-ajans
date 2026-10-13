# PROJE BRİFİ — Merkez Ajans (çalışma adı: Aurista)

> Bu dosya, Patron (Alper) ile claude.ai'de yapılan planlama görüşmesinin eksiksiz özetidir.
> Claude Code: Planlamaya başlamadan önce bu dosyanın tamamını oku. Burada "KARAR" olarak geçenler Patron tarafından onaylanmıştır; "ÖNERİ" olarak geçenler henüz onay bekler. Belirsiz bir nokta görürsen varsayım yapma, Patron'a sor.

---

## 1. Bağlam

- **Patron:** Alper. Türkiye'de yaşıyor. Şahıs şirketi var (KDV'li ve tevkifatlı fatura kesiyor, mali müşaviri var). E-ticaret işi aynı şirkete bağlanacak.
- **Bilgisayar:** Windows. **Abonelik:** Claude Pro (claude.ai sohbetleri ile Claude Code aynı kullanım limitini paylaşır).
- **Öğrenme hedefi:** Claude Code, skill'ler, ajanlar ve MCP'leri adım adım öğrenmek. Açıklamalar sade Türkçe olmalı.
- **Üretici:** Patron'un annesi. Profesyonel düzeyde el işi yapıyor:
  - El örgüsü kıyafetler
  - Tığ örgüsü çantalar
  - Yılbaşı süsleri
  - Takı tasarımı
  - Tel ve boncukla yapılan gelin aksesuarları
- **Üretim süresi:** Ürüne göre 2 saat ile 2 gün arası. Fiyat emeğe/süreye göre belirlenir; uzun ve zahmetli ürünler daha pahalı.

## 2. Marka

- **KARAR:** Çalışma adı **Aurista**. ("Aur" = altın, "-ista" = usta → "altın usta"; Türkçedeki "eli altın" deyimine bağlanır.)
- **KARAR:** İsim değişebilir. Marka adı sistemde **tek bir dosyada** yaşar (`10-marka/kimlik.yaml`). Klasör, modül ve ajan adları "aurista" kelimesini içermez; hepsi adı bu dosyadan okur.
- **Varsayım (KARAR):** Marka tescilinin ve tüm sosyal medya hesaplarının açık olduğu varsayılarak planlanır. Gerçekte henüz hiçbir hesap açılmadı.
- **Tescil/ön kontrol notları (yapılacak):**
  - TÜRKPATENT'te arama; ilgili sınıflar: 14 (takı), 18 (çanta), 25 (giyim), 26 (saç/gelin aksesuarı), 28 (yılbaşı süsü). Başvuru şahıs şirketi üzerinden.
  - ABD'de Aurista Technologies Inc. adına eski bir "AURISTA" kaydı bulundu (kaplamalı madeni para ve takı). Güncel durumu bilinmiyor. Etsy/ABD'ye açılmadan önce kontrol edilmeli.
  - aurista.com / aurista.com.tr alan adı kontrolü.
  - Dört platformda aynı kullanıcı adı; alınmışsa tutarlı alternatif (ör. aurista.atelier, auristahandmade).
  - Takı dünyasında "aur-" ile başlayan isimler kalabalık; görsel kimlikle ayrışmak önemli.
- **Marka mimarisi:** Marka ürün türüne göre değil, **üreticiye ve ustalığa** göre kurulur. Tek çatı marka, altında koleksiyonlar (örgü, çanta, yılbaşı, takı, gelin). Gelin aksesuarı ileride ayrı alt marka olabilir; başta koleksiyon olarak kalır.
- **Hikâye:** "Eli altın bir ustanın elinden." Fabrika ürününe karşı ustalık ve emek.
- **KARAR — İçerik kuralları:**
  - Annenin **yüzü hiçbir içerikte görünmez.** Çekimler omuz üstünden veya tepeden.
  - **Elleri** tanıtım ve reklam videolarında görünebilir.
  - **Üretim sırrı gösterilmez.** Sadece seçilmiş kesitler: ilk ilmek, malzeme seçimi, son dokunuş, şekil verme, paketleme gibi.
  - Emek görünür kılınır: "Bu ürün X saatte yapıldı" bilgisi sabit unsur.
  - Eller tutarlı görünür: aynı masa, ışık, arka plan (isteğe bağlı imza aksesuar: yüzük/bileklik).
  - **Üretim kesitleri her zaman gerçek çekim.** Yapay zekâ (Higgsfield) sadece ürün sunumu, sahne ve arka plan için. Yapay zekâyla sahte üretim videosu yapılmaz (güven riski).
  - Ayda 1-2 **çekim günü**; telefon + tepeden çeken tripod; farklı ürünlerin farklı aşamaları toplu çekilir; kesitler etiketli depolanır (ürün, aşama, süre).
- **Marka biriminin içeriği:** strateji (neden var, farkı), 2-3 müşteri profili (gelin adayı, hediye arayan, el işi sever), hikâye, sözel kimlik (isim, slogan, ses tonu, kullanılan/yasak kelimeler), görsel kimlik (logo, renk, yazı tipi, fotoğraf tarzı), **Higgsfield komut kütüphanesi**, yıllık kampanya takvimi (yılbaşı, sevgililer günü, anneler günü, düğün sezonu).
- **Marka kuralları:** Herkes okur, **sadece Patron değiştirir** (toplantı kararıyla).
- **Marka bekçisi** (ucuz model): yayından önce her içeriği kontrol listesiyle tarar (ton, renk, yasak kelime, yüz yok, sır yok).
- **Token kuralı:** Herkesin okuduğu **tek sayfalık marka özeti** + ayrı detay dosyaları (sadece ihtiyacı olan açar).

## 3. Satış kanalları (sıralı)

1. Sosyal medya: Instagram, Facebook, TikTok, Pinterest
2. Türkiye e-ticaret: Shopier, Shopify (sosyal medyaya benzer ama daha kapsamlı planlanacak)
3. Yurt dışı: Etsy; Shopier ve Shopify yurt dışına açılır
- **KARAR:** Başlangıç **sadece Instagram** ile. Uçtan uca oturunca diğerleri onun şablonundan, tek tek ve kontrollü eklenir.

## 4. Şirket hiyerarşisi (KARAR)

```
Patron (Alper)
 └─ CEO (Claude) — sadece orkestrasyon, sadece müdürlerle konuşur
     ├─ Marka Müdürü
     ├─ Ürün & Fiyat Müdürü
     ├─ Medya Stüdyosu Müdürü
     ├─ Instagram Müdürü
     ├─ Facebook Müdürü
     ├─ TikTok Müdürü
     ├─ Pinterest Müdürü
     ├─ Meta Reklam Müdürü      (ileride)
     ├─ TikTok Reklam Müdürü    (ileride)
     ├─ Analiz & ARGE Müdürü
     └─ (ileride) Shopier, Shopify, Etsy, Sipariş & Müşteri
```

- Sosyal medya müdürleri **doğrudan CEO'ya** bağlıdır (ara direktör yok). Her platform kendi dinamikleri olan bir satış kanalı gibi ele alınır.
- **Müdürler sadece orkestrasyon yapar;** hiçbir işi kendileri yapmaz. İşleri departmanın işçilerine dağıtır.
- **Komut zinciri hiyerarşik, veri ortak:** Emirler yukarıdan aşağı, raporlar aşağıdan yukarı. Ortak kaynakları (marka özeti, ürün kataloğu, medya deposu) herkes doğrudan okur.

## 5. Departman iç yapısı (KARAR)

```
CEO → iş emri
       ↓
  Müdür Asistanı (script) — her işi karşılar
       ├─ rutin → işçilere dağıtır → rapor
       └─ istisna → Müdür'ü (Sonnet) çağırır
```

- **Müdür Asistanı (script, önde):** Rutin işleri sıfır/az token ile yürütür.
- **Müdür (Sonnet, arkada):** Sadece istisnalarda devreye girer. Çağırma kuralları:
  - İş emri "rutin" olarak işaretlenmemişse (yeni kampanya, özel gün)
  - Bir işçi hata verdiyse veya beklenmeyen sonuç çıktıysa
  - Marka bekçisi bir içeriği iki kez reddettiyse
  - Departman bütçe sınırına yaklaştıysa
  - Patron veya CEO açıkça istediyse
- **İşçiler iki türdür:**
  - **Script işçiler** (0 token): görsel uzmanı (platform ölçüsüne boyutlandırma, video kırpma), zamanlayıcı, veri toplayıcı vb.
  - **Ajan işçiler** (Haiku): metin yazarı, hashtag/başlık uzmanı, temsilci, gözcü vb.
- Her platform departmanında en az şu roller: **uygulayıcı(lar)** (içerik/paylaşım), **temsilci** (iç veri → ARGE), **gözcü** (rakip/trend → ARGE), **görsel uzmanı** (script).
- Hashtag, başlık, format: her platformun kendi algoritmasına göre.
- **Öğrenen işçiler:** Model kendi kendine öğrenmez; öğrenme yazılı tecrübeyle olur.
  - Her işçinin `ogrenilenler.md` dosyası (iş sonrası, Patron geri bildirimi sonrası ve haftalık ARGE sonuçlarıyla güncellenir).
  - Müdür bu dosyaları **ayda bir budar** (eskiyi siler, tekrarı birleştirir) ki şişip token yemesin.
  - Kalıcı yöntem değişikliği (skill güncellemesi) müdürün önerisi + **Patron onayı** ile.

## 6. Ortak birimler

- **Ürün & Fiyat:** Her ürün bir dosya (foto, ölçü, malzeme, üretim süresi, maliyet, fiyat, stok, koleksiyon). Fiyat formülü üretim süresini hesaba katar. "Üretim saati başına kazanç" ölçüsü tutulur.
- **Medya Stüdyosu:** Ham görselleri alır → Higgsfield ile yeni görsel/video üretir → **tek bir depoda** saklar. Her görselin kaydı **medya indeksinde** (ürün, renk, ham/işlenmiş, aşama, dosya yolu). Platform departmanları görselleri depodan alıp **kendi platformlarına göre boyutlandırır**. Higgsfield sadece onaylı ürünler için kullanılır; üretilen dosya bir kez kaydedilir, tüm platformlar yeniden kullanır. (Higgsfield erişim yöntemi — API/MCP — kurulumda güncel haliyle kontrol edilecek.)
- **Marka:** Bölüm 2.

## 7. Analiz & ARGE departmanı (KARAR)

- **Çekirdek ekip:**
  - Satış & kârlılık analisti
  - Müşteri sesi analisti (sorular, yorumlar, DM'ler; tekrarlayan soru, şikâyet, talep)
  - **ARGE şefi** (trend araştırmacısı; gözcülerin fikir kartlarını birleştirir, toplantıya en iyi 3 fikri getirir)
  - Strateji sorumlusu (gündem ve karar önerileri)
- **Temsilciler:** Her departmanda bir temsilci (her sosyal medya platformu, reklam masaları, Medya Stüdyosu, Ürün & Fiyat, ileride e-ticaret). Temsilci **kendi departmanının içinde** oturur (modülle birlikte takılır/çıkar). Hepsi **aynı rapor şablonunu** doldurur: öne çıkanlar, temel rakamlar, müşteri soruları, sorunlar, öneriler. Raporlar "veri odasına" bırakılır.
- **Gözcüler:** Her platform departmanında bir gözcü; rakip ve trend takibi:
  - Instagram & TikTok: yükselen sesler, tutan formatlar, el işi hesaplarının en çok etkileşim alan paylaşımları
  - Pinterest: Pinterest Trends (sezon trendleri en erken burada)
  - Facebook: el işi grupları, Marketplace fiyat ve talepleri
  - Meta Reklam: Meta Reklam Kütüphanesi (uzun süre yayında kalan rakip reklamlar)
  - TikTok Reklam: TikTok Creative Center
  - Medya Stüdyosu: görsel trendler, Higgsfield yenilikleri
  - İleride Etsy/Shopier: çok satanlar, fiyat aralıkları, rakip yorumları
- **Gözcü kuralları:** Platform başına sabit rakip listesi (5-10 hesap); sadece geçen haftadan beri **değişeni** raporlar; haftada bir (Pinterest gibi yavaşlar iki haftada bir); ucuz model; sadece **resmî/herkese açık araçlar**, kurallara aykırı otomatik veri kazıma (scraping) yok.
- **Fikir kartı formatı:** fikir, kanıt (link/örnek), uyduğu ürün, annenin üretim yükü, tahmini öncelik. Seçilmeyenler **fikir bankasında** bekler; sezonu gelince tekrar önerilir.
- **Haftalık toplantı akışı:**
  1. Hazırlık (otomatik): temsilciler veriyi toplar, tek sayfalık rapor (rakamları script çeker, raporu ucuz model yazar)
  2. Gündem: strateji sorumlusu kısa gündem + 3-5 karar önerisi
  3. Toplantı: Patron gündemi okur, soru sorar; detay gerekirse sadece ilgili temsilci "odaya çağrılır"
  4. Kararlar **karar defterine** yazılır, ilgili departmanların görev kutusuna iner
  5. Ölçüm: bir sonraki toplantıda her kararın sonucu kontrol edilir
- **Aylık derin toplantı** (isteğe bağlı): kârlılık analizi, yeni ürün/kampanya planı.
- Toplantı tek komutla başlar (ör. `/haftalik-toplanti`); ARGE arada kendiliğinden çalışmaz.
- **Gerçekçilik notu:** İlk haftalarda veri az olacak. Platform istatistiklerine otomatik erişim (API) zamanla kurulur; başta temsilciler Patron'un indirdiği istatistik dosyalarından/ekran görüntülerinden çalışabilir.
- Bütçe defteri de toplantının gündem maddesidir (bkz. Bölüm 10).

## 8. Modülerlik — tak-çıkar (KARAR)

- **Departman = modül = Claude Code eklentisi (plugin).** Müdürü, asistanı, işçileri, skill'leri, scriptleri ve MCP bağlantılarıyla birlikte takılır/çıkarılır.
- **Ofisler birbirini tanımaz.** Bir modül başka bir modüle adıyla atıf yapmaz; sadece ortak alanlardan okur. Biri çıkarılınca diğerleri hiçbir şey kaybetmez.
- **Ortak alanlar sözleşmeyle çalışır** (sabit formatlar: medya indeksi, ürün dosyası, rapor şablonu, fikir kartı, iş emri).
- **Yazma bölgeleri:** Modül ortak alanlarda sadece kendine ayrılmış yerlere yazar (temsilci → veri odası, gözcü → fikir kartları, stüdyo → medya deposu). Asıl çalışması kendi ofis klasöründe kalır.
- **Reklam masaları ayrı modül:** Meta Reklam (Instagram veya Facebook'tan en az biri açıksa çalışır), TikTok Reklam. Reklama başlanana kadar kapalı, sıfır token.
- **Modül kimlik kartı (`MODUL.md`):** ne okur, nereye yazar, neye bağımlı, hangi MCP'leri gerektirir.
- **Ekleme (`/modul-ekle`):** şablonu kopyala → platform kurallarını doldur → eklentiyi kur → aktif modül listesine satır ekle → ofis klasörünü aç.
- **Çıkarma (`/modul-kaldir`):** eklentiyi kaldır → listeden sil → ofis klasörünü `arsiv/`e taşı. Arşive ajanlar bakmaz (token harcanmaz). Çıkarılan modülün kalıntısı yanlış sonuca veya gereksiz token'a yol açmamalı.
- **Denetim scripti:** (1) Bir modülün adı başka modülün içinde geçiyor mu? (2) `kimlik.yaml` dışında marka adı sabit yazılmış mı? Uyarır.
- Yeni platform = şablonun kopyası; şablon uygulayıcı + temsilci + gözcü + görsel uzmanını hazır getirir.

## 9. Teknik mimari

- **Tek proje klasörü** hem Obsidian kasası hem Claude Code çalışma alanıdır (dosyalar Markdown).
- **Teknik kısıt:** Claude Code'da alt ajan başka alt ajan çalıştıramaz (tek seviye). Bu yüzden: CEO ana oturumdur; departman müdürleri gerektiğinde **departman klasöründe ayrı (headless) oturum** olarak başlatılır; işçiler müdürün alt ajanlarıdır. Rutin işlerde müdür oturumu hiç açılmaz, Müdür Asistanı scripti yürütür.
- **İletişim dosya tabanlı:** CEO departmanın `gelen-kutusu/`na **iş emri** yazar; departman `raporlar/`a **kısa rapor** döner. Sabit, kısa şablonlar.
- **CLAUDE.md dikkat:** Claude Code üst klasörlerdeki CLAUDE.md'leri de okur. Kökteki CLAUDE.md herkesin uyduğu **kısa şirket anayasası** olur; CEO'nun görev tanımı **ayrı bir dosyada** durur (müdürler okumasın).
- **KARAR — CEO.md yüklenmesi:** CEO rolü sadece `/ceo` komutuyla açılır (komut `00-yonetim/CEO.md`'yi yükler); kök CLAUDE.md onu içe aktarmaz.
- **KARAR — Ortak birimler çekirdektir:** Marka, Ürün & Fiyat, Medya Stüdyosu, Analiz & ARGE her zaman açıktır, tak-çıkar değildir. Sadece platform ve reklam departmanları modüldür.
- **KARAR — Öğrenme dosyaları ofiste:** Claude Code eklentiyi kurarken kendi önbelleğine kopyalar; bu yüzden `ogrenilenler.md` eklentide değil `60-ofisler/<departman>/ogrenme/` içinde durur.
- **KARAR — Model çağrısı yolu:** Scriptler modeli Anthropic API ile değil, `araclar/claude_calistir.py` üzerinden `claude -p` ile çağırır (Pro limitinden düşer, bütçe defterine yazar).
- **KARAR — Adlandırma:** Tarih `YYYY-AA-GG`; dosya/klasör adlarında küçük harf ve tire, Türkçe karakter ve boşluk yok.
- **KARAR — Klasör iskeleti** (Faz 0'da kuruldu; aşağıdaki brif taslağıdır, güncel hali klasörün kendisi ve `_dizin.md` notlarıdır. Eklenenler: `.claude/commands/`, `araclar/`, `00-yonetim/sablonlar/`, `00-yonetim/butce-ayarlari.yaml`, `moduller/_sablon/`, `moduller/_ofis-sablonu/`):

```
merkez-ajans/
├─ CLAUDE.md               ← şirket anayasası (kısa)
├─ 00-yonetim/
│   ├─ CEO.md              ← CEO görev tanımı
│   ├─ aktif-moduller.md
│   ├─ karar-defteri.md
│   ├─ butce-defteri.csv
│   └─ gorev-kutulari/
├─ 10-marka/
│   ├─ kimlik.yaml         ← marka adı, slogan, hesaplar (TEK KAYNAK)
│   ├─ marka-ozeti.md
│   └─ detay/
├─ 20-urunler/
├─ 30-medya/
│   ├─ ham/  islenmis/
│   └─ medya-indeksi.csv
├─ 40-veri-odasi/
│   ├─ raporlar/
│   └─ fikir-kartlari/  fikir-bankasi/
├─ 50-toplantilar/
├─ 60-ofisler/
│   └─ instagram/
│       ├─ CLAUDE.md       ← müdür görev tanımı
│       ├─ gelen-kutusu/  raporlar/  ogrenme/
├─ arsiv/
└─ moduller/               ← eklentiler (yerel marketplace)
    └─ instagram/
        ├─ MODUL.md
        ├─ agents/  skills/  scripts/
        └─ .mcp.json
```

## 9.1 Obsidian ile çalışma (KARAR — ilk günden)

- Proje **en baştan Obsidian ile birlikte** kurulur. Proje klasörü Faz 0'da Obsidian kasası olarak açılır. Amaç hem düzen hem token tasarrufu.
- **Patron okur, Claude özetlemez:** Raporlar, karar defteri, bütçe durumu, fikir bankası ve içerik taslakları Obsidian'da doğrudan okunabilir olmalı. Patron'un "durum ne?" diye CEO'ya sorması (token) yerine Obsidian'da açıp bakabilmesi hedeflenir.
- **Özellikler (frontmatter/properties):** Ürün dosyaları, iş emirleri, raporlar, fikir kartları YAML özellikleriyle yazılır (ör. `fiyat`, `uretim_saati`, `durum`, `departman`, `oncelik`). Scriptler ve ajanlar uzun metin yerine bu alanları okur.
- **Şablonlar:** Obsidian'ın şablon özelliğiyle ürün, iş emri, rapor, fikir kartı, toplantı notu şablonları. Ajanlar ve scriptler aynı şablonları kullanır (tek format).
- **Bağlantılar:** Notlar arası ilişkiler `[[...]]` bağlantılarıyla kurulur (ürün ↔ medya ↔ içerik ↔ rapor). Ajanlar klasör taramak yerine bağlantıyı takip eder.
- **Dizin notları:** Her ana klasörde kısa bir dizin notu (ne nerede). Ajanlar önce dizini okur, sadece gereken dosyayı açar.
- **Panolar (ÖNERİ):** Obsidian'ın yerleşik Bases özelliğiyle (veya Dataview gibi bir eklentiyle) Patron için sıfır token panolar: bu haftanın içerikleri, departman bütçeleri, açık iş emirleri, stok durumu. (Topluluk eklentisi; kurulmadan önce Patron'a sorulur.)
- **Ek dosya ayarı:** Obsidian'a eklenen görseller otomatik olarak `30-medya/ham/` klasörüne düşecek şekilde ayarlanır.
- **Gürültü engeli:** Claude Code `.obsidian/` ayar klasörünü ve `arsiv/`i okumayacak şekilde yapılandırılır (gereksiz token önlenir).
- Obsidian eklentileri minimum tutulur; her eklenti Patron onayıyla.

## 10. Token ekonomisi ve bütçe (KARAR)

- **Hedef:** Başlangıçta her şey **Claude Pro limitine sığmalı.**
- **Temel kural: Önce script, sonra skill, en son ajan.**
  - Script (0 token): kuralı belli her iş
  - Skill (az token): uzmanlık bilgisi, sadece gerekince yüklenir
  - Ajan: sadece yaratıcılık/muhakeme
- **Bağlam hijyeni:** kısa CLAUDE.md ve görev tanımları; tek sayfa marka özeti; ajanlar görsellere bakmaz, medya indeksindeki açıklamayı okur; kısa sabit rapor/iş emri şablonları.
- **MCP'ler departmana özel** (her MCP her oturumda bağlama yük bindirir). Rutin API işlerinde script, MCP'den ucuzdur.
- **Toplu çalışma:** her paylaşım için ayrı oturum değil, departman başına haftada bir toplu üretim.
- **KARAR — model dağılımı:** Haiku: işçiler, temsilciler, gözcüler, marka bekçisi. Sonnet: CEO, müdür (istisna), haftalık toplantı.
- **KARAR — Opus "danışman":** Opus sadece `/danisman` komutuyla ve Patron onayıyla çalışır; hiçbir otomatik iş Opus çağıramaz (`claude_calistir.py` onaysız Opus'u durdurur). Ham veri değil 1-2 sayfalık hazır özet okur; çıktısı kalıcı "tarif"tir (skill, şablon, formül, kontrol listesi) — Opus öğretir, Haiku uygular. Bütçede ayrı pay: şirket haftalık payının %10-15'i (başta %12); dolunca Sonnet'e düşer veya ertelenir. Kullanım anları: Faz 1 marka stratejisi ve fiyat formülü, aylık derin toplantı, aylık öğrenme budaması/skill güncellemesi, Sonnet'in iki kez çözemediği sorun.
- **Faz 0 ölçümü (2026-10-13):** Tek kelimelik bir `claude -p` Haiku çağrısı ~35 bin token tuttu (Claude Code'un kendi talimatları + anayasa). Her ayrı çağrının sabit bir "giriş ücreti" var → toplu çalışma şart; Faz 3'te bu yükü azaltan ayarlar denenecek.
- **Bütçe defteri (KARAR):** Her yapay zekâ çağrısının kullanımı scriptle kaydedilir. **Her iş bittikten sonra** kısa durum satırı: bu işin maliyeti, departmanın haftalık harcaması, şirket toplamı. Amaç zamanında müdahale.
- **KARAR — eşikler:** departman başına haftalık pay; %70'te uyarı, %90'da sadece kritik işler. Paylar `00-yonetim/butce-ayarlari.yaml`'da; birim "API karşılığı" tahmini USD (göreli ölçü).
- **Bütçe ölçümü iki yoldan:** script çağrıları `claude_calistir.py` ile, etkileşimli oturumlar `Stop` kancası (`araclar/oturum_kullanimi.py`) ile deftere yazılır. Oturum ölçümü yaklaşıktır.
- **Not:** Pro'nun kalan limiti scriptlerden doğrudan görülemez; kendi harcamamız ölçülür, ilk haftalarda Claude'un kullanım ekranıyla kalibre edilir.
- **KARAR — haftalık ritim:** Pazartesi toplu içerik üretimi, Perşembe kısa kontrol, Pazar hafif toplantı. Ağır işler Patron'un sohbette yoğun olmadığı saatlere.
- Limit sık aşılırsa: önce optimize, gerekirse plan büyütme konuşulur.

## 11. Kurulum fazları

- **Faz 0:** Obsidian kurulumu ve kasa ayarları (Bölüm 9.1), iskelet, Obsidian şablonları, şirket anayasası (CLAUDE.md), CEO.md, kimlik.yaml, departman şablonu (asistan + müdür + işçiler + öğrenme + bütçe kaydı), denetim scripti, bütçe defteri
  - **Faz 0 durumu (2026-10-13): tamamlandı.** Kurulanlar: iskelet + `_dizin.md` notları, 6 ortak şablon, CLAUDE.md, CEO.md, `/ceo` `/danisman` `/modul-ekle` `/modul-kaldir` komutları, kimlik.yaml, departman şablonu (`moduller/_sablon` + `_ofis-sablonu`), `araclar/` scriptleri (denetim, bütçe, claude_calistir, oturum kancası, modul), `.claude/settings.json` (izinler + bütçe kancası), Obsidian ayarları, Git.
- **Faz 1:** Marka birimi (marka özeti, ton, renkler) + Ürün & Fiyat (ilk ~10 ürün, fiyat formülü)
- **Faz 2:** Medya Stüdyosu (depo + indeks + boyutlandırma scriptleri, sonra Higgsfield)
- **Faz 3:** Instagram departmanı, uçtan uca
- **Faz 4:** Şablonla Facebook, TikTok, Pinterest (tek tek)
- **Faz 5:** Analiz & ARGE çekirdeği + ilk haftalık toplantı
- **Faz 6:** Reklam masaları, sonra e-ticaret katı

## 12. Açık konular (Patron'a sorulacak)

- ~~Yedekleme~~ → **KARAR:** Git + özel GitHub deposu (mevcut hesap; ileride depo transferiyle başka hesaba taşınabilir). Büyük medya Git dışında, OneDrive'da.
- ~~Klasör iskeleti, model dağılımı, eşikler, ritim~~ → **KARAR** (Bölüm 9 ve 10).
- Higgsfield'e erişim yöntemi ve maliyeti → **Faz 2'de**. Higgsfield maliyeti Pro limitinin dışındadır; bütçe defterinde ayrı kalem olacak.
- Platform istatistiklerine erişim (işletme hesapları, API) — başta manuel → **Faz 3'te**.
- Marka tescili, alan adı ve kullanıcı adı kontrolleri (Bölüm 2) → Patron yapar; **Faz 1'de** kontrol listesi.
- Panolar: Obsidian'ın yerleşik **Bases** özelliği açık; Dataview yerine bununla yapılması önerilir (topluluk eklentisi gerekmez) → Patron onayı bekliyor.

## 13. Ertelenen araçlar

- Codex veya Google Antigravity'yi ikinci ajan olarak eklemek **şimdilik yok.** Gerekirse ileride (Claude limiti yetmezse veya ikinci göz gerekirse). Eklenirse ortak talimat için AGENTS.md düzeni kurulur, iki ajan aynı anda aynı dosyayı düzenlemez.

---

## Claude Code için çalışma talimatı

1. Bu dosyayı oku, **hiçbir şey kurmadan** önce anladıklarını 10 maddede özetle ve Bölüm 12'deki açık konuları Patron'a sor.
2. Eksik veya çelişkili gördüğün her noktayı listele.
3. Onaydan sonra sadece **Faz 0** için ayrıntılı bir plan çıkar; Patron onaylamadan dosya oluşturma.
4. Her fazın sonunda bu brifi güncelle (alınan yeni kararları "KARAR" olarak işle).
5. Patron yeni başlayan biri; teknik adımları sade Türkçe ve gerekçeleriyle anlat.
