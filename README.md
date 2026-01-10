# App – YouTube Video Downloader

Bu proje, Python kullanılarak geliştirilmiş basit ve temiz bir **YouTube video indirme masaüstü uygulamasıdır**.
Uygulama, grafik arayüz üzerinden YouTube videolarını **MP4 (video)** veya **MP3 (ses)** formatında indirmeyi sağlar.

Arayüz Tkinter ile hazırlanmıştır ve indirme işlemleri arka planda çalışarak uygulamanın donmasını engeller.

---

## Özellikler

* YouTube video URL girişi
* MP4 (video) ve MP3 (ses) format seçimi
* MP4 için çözünürlük seçimi (360p, 720p, 1080p vb. – mevcut olanlar)
* FPS bilgisi görüntüleme
* İndirme konumu seçme
* Arka planda indirme (UI donmaz)
* Durum göstergesi

  * Idle
  * Downloading
  * Completed
  * Error

---

## Kullanılan Teknolojiler

* Python 3
* Tkinter (GUI)
* yt-dlp (YouTube indirme altyapısı)
* FFmpeg (video ve ses birleştirme / MP3 dönüştürme)

---

## Gereksinimler

* Python 3.8 veya üzeri
* Windows işletim sistemi
* Git

---

## Kurulum

### 1. Projeyi İndirme

```bash
git clone https://github.com/hakXz/appdl.git
cd appdl-main
```

---

### 2. Gerekli Python Kütüphanelerini Yükleme

```bash
pip install -r requirements.txt
```

---

### 3. FFmpeg Otomatik Kurulumu (Windows)

Bu uygulama, video ve ses akışlarını birleştirmek ve MP3 dönüştürme yapmak için **FFmpeg** kullanır.

Windows kullanıcıları için **otomatik kurulum scripti** projeye eklenmiştir.

1. Proje klasörü içinde bulunan
   **`install_ffmpeg.bat`** dosyasına çift tıklayın
2. Script:

   * FFmpeg’i resmi kaynaktan indirir
   * `C:\ffmpeg\` dizinine kurar
   * `C:\ffmpeg\bin` yolunu otomatik olarak **PATH** ortam değişkenine ekler
3. Kurulum tamamlandıktan sonra **bilgisayarı yeniden başlatın**
4. Kontrol için Komut İstemi (CMD) açın:

```bash
ffmpeg -version
```

Bilgi geliyorsa kurulum başarılıdır.

---

### 4. Programı Çalıştırma

```bash
python app.py
```

---

## Kullanım

1. YouTube video linkini girin
2. **Fetch Formats** ile mevcut çözünürlükleri alın
3. MP4 veya MP3 formatını seçin
4. İndirme klasörünü belirleyin
5. **Download** butonuna basın

İndirme işlemi arka planda gerçekleşir.

---

## Notlar

* YouTube videolarının büyük çoğunluğu video ve ses akışlarını ayrı sunduğu için **FFmpeg gereklidir**
* FFmpeg olmadan MP4 dosyaları sessiz olabilir
* Bazı videolarda belirli çözünürlük veya FPS seçenekleri bulunmayabilir
* YouTube zaman zaman 403 hatası verebilir, bu durumda `yt-dlp` güncellenmelidir:

```bash
pip install -U yt-dlp
```

---

## Lisans

Bu proje eğitim ve kişisel kullanım amaçlıdır.
YouTube’un kullanım koşulları kullanıcı sorumluluğundadır.
