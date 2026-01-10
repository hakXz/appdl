# App – Video Downloader

Bu proje, Python kullanılarak geliştirilmiş basit ve temiz bir **video indirme masaüstü uygulamasıdır**.
Uygulama, grafik arayüz üzerinden **YouTube** ve **X (Twitter)** içeriklerini **MP4 (video)** veya **MP3 (ses)** formatında indirmeyi sağlar.

Arayüz Tkinter ile hazırlanmıştır ve indirme işlemleri arka planda çalışarak uygulamanın donmasını engeller.

---

## Özellikler

* YouTube ve X (Twitter) URL girişi
* MP4 (video) ve MP3 (ses) format seçimi
* YouTube için çözünürlük seçimi (360p, 720p, 1080p vb. – mevcut olanlar)
* FPS bilgisi görüntüleme (YouTube)
* X (Twitter) için otomatik kalite seçimi
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
* yt-dlp (YouTube & X indirme altyapısı)
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

1. Proje klasörü içindeki **`install_ffmpeg.bat`** dosyasına çift tıklayın
2. FFmpeg otomatik olarak indirilir ve PATH’e eklenir
3. Kurulumdan sonra **bilgisayarı yeniden başlatın**

Kontrol:

```bash
ffmpeg -version
```

---

### 4. Programı Çalıştırma

```bash
python app.py
```

---

## Kullanım

1. YouTube veya X (Twitter) linkini girin
2. YouTube için **Fetch Formats** ile çözünürlükleri alın
3. MP4 veya MP3 formatını seçin
4. İndirme klasörünü belirleyin
5. **Download** butonuna basın

İndirme işlemi arka planda gerçekleşir.

---

## Notlar

* YouTube videolarında video ve ses ayrı sunulduğu için **FFmpeg gereklidir**
* FFmpeg olmadan MP4 dosyaları sessiz olabilir
* X (Twitter) içerikleri otomatik en iyi kaliteyle indirilir
* Bazı videolarda çözünürlük veya FPS seçenekleri bulunmayabilir
* 403 hatalarında `yt-dlp` güncellenmelidir:

```bash
pip install -U yt-dlp
```

---

## Lisans

Bu proje eğitim ve kişisel kullanım amaçlıdır.
YouTube ve X platformlarının kullanım koşulları kullanıcı sorumluluğundadır.
