# BYD Dizayn — Seal Kadran güncellemeleri

Bu depo uygulamanın herkese açık APK yayınları içindir. Özel imzalama anahtarı veya erişim parolası yüklenmez.

## İlk yayın
1. Releases → Draft a new release bölümünü açın.
2. Yeni etiket: `v1.2.3`, başlık: `Seal Kadran v1.2.3 — Beta`.
3. Verilen imzalı v1.2.3 APK'yı dosya olarak ekleyin. Bir yayına yalnızca bir APK ekleyin.
4. Sürüm notlarını yazın. Bu sürümün araç testlerinin tamamlanmadığını belirtin.
5. Güncelleme kanalının bu yayını alması için “pre-release” seçeneğini işaretlemeyin. Bu, araç üzerinde test edildiği anlamına gelmez; yalnızca GitHub latest adresinin çalışması içindir.
6. Publish release düğmesine basın.
7. Actions bölümündeki Publish app update metadata işinin yeşil olmasını bekleyin. İş, APK imzasını doğrular ve yayına latest.json dosyasını ekler.

## Sonraki güncellemeler
Aynı adımları yeni etiket ve daha büyük versionCode ile tekrarlayın. Aynı özel anahtarla imzalanmış APK gerekir. Sürüm notları uygulamada görünür. Dosyayı önce taslak yayına yükleyip sonra yayını açın. Hatalı bir dosyayı değiştirmeniz gerekirse yeni sürüm numarasıyla yayınlayın.

## Sabit uygulama adresi
https://github.com/aytacuygun837-glitch/BYD-Dizayn-Updates/releases/latest/download/latest.json

Bu adres ilk APK yayını ve başarılı Actions çalışması tamamlanana kadar aktif değildir. Kullanıcılar ilk güncelleme destekli APK'yı bir kez elle kurar. Sonraki sürümleri uygulamadaki Güncellemeler ekranından indirip Android kurulum ekranında onaylar. Uygulama açılışında günde bir kez kontrol eder; arka planda anlık push bildirimi yoktur.

Otomasyonun hata vermesi durumunda Actions günlüklerini inceleyin. Mevcut bir yayının etiketini Actions → Publish app update metadata → Run workflow alanından vererek tekrar çalıştırabilirsiniz. Bu işlem var olan latest.json dosyasını yeniler ve seçilen yayını latest yapar; daha eski sürümü seçmeyin.
