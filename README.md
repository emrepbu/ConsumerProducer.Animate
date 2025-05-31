# Producer-Consumer Animation

🎬 Animated visualization of Producer-Consumer problem using Manim. Features buffer management, synchronization, and neural network implementations. Educational tool for understanding concurrent programming concepts.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Manim](https://img.shields.io/badge/ManimCE-v0.17.0+-red.svg)](https://www.manim.community/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[English](#english) | [Türkçe](#türkçe)

## English

### 🎯 Features

- Visual representation of Producer and Consumer components
- Limited capacity buffer visualization
- Data production and consumption animations
- Waiting animations for full/empty buffer states
- Neural network-based producer-consumer variant
- Bilingual support (English/Turkish)

### 📦 Installation

1. Ensure Python 3.8+ is installed
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 🚀 Usage

Run the animation:

```bash
./run_animation.sh
```

Or manually:

```bash
# Render as video (MP4)
manim -pqh producer_consumer_animation.py ProducerConsumer

# Low quality preview
manim -pql producer_consumer_animation.py ProducerConsumer

# Render as GIF
manim -pql --format=gif producer_consumer_animation.py ProducerConsumer

# Neural network version
manim -pqh neural_producer_consumer.py NeuralProducerConsumer
```

### 🎥 Animation Details

The animation includes these components:

1. **Producer**: Shown in blue box, continuously generates data
2. **Buffer**: Yellow rectangle in center, 5-slot capacity
3. **Consumer**: Shown in green box, processes data

Animation flow:
- Producer generates data and adds to buffer
- Producer waits when buffer is full
- Consumer takes data from buffer and processes it
- Consumer waits when buffer is empty

### 📹 Generated Videos

The project includes the following rendered videos:

#### 1. Producer-Consumer Animation
- **English Version**: `media/videos/temp_render/1080p60/ProducerConsumer_en.mp4`
- **Turkish Version**: `media/videos/temp_render/1080p60/ProducerConsumer_tr.mp4`

#### 2. Neural Producer-Consumer Animation
- **English Version**: `media/videos/temp_render/1080p60/NeuralProducerConsumer_en.mp4`
- **Turkish Version**: `media/videos/temp_render/1080p60/NeuralProducerConsumer_tr.mp4`

All videos are rendered in 1080p 60fps quality.

### 🏷️ Keywords

`producer-consumer-problem` `manim-animation` `concurrent-programming` `thread-synchronization` `buffer-management` `educational-visualization` `computer-science-education` `operating-systems-concepts` `neural-network-visualization` `python-animation` `manim-community` `cs-education` `threading-visualization` `synchronization-primitives` `animated-algorithms`

---

## Türkçe

### 🎯 Özellikler

- Producer (Üretici) ve Consumer (Tüketici) bileşenlerinin görsel temsili
- Sınırlı kapasiteli buffer (tampon bellek) gösterimi
- Veri üretimi ve tüketimi animasyonu
- Buffer dolu/boş durumlarında bekleme animasyonları
- Sinir ağı tabanlı üretici-tüketici varyantı
- İki dil desteği (İngilizce/Türkçe)

### 📦 Kurulum

1. Python 3.8+ yüklü olduğundan emin olun
2. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

### 🚀 Kullanım

Animasyonu çalıştırmak için:

```bash
./run_animation.sh
```

Veya manuel olarak:

```bash
# Video olarak render et (MP4)
manim -pqh producer_consumer_animation.py ProducerConsumer

# Düşük kalitede önizleme
manim -pql producer_consumer_animation.py ProducerConsumer

# GIF olarak render et
manim -pql --format=gif producer_consumer_animation.py ProducerConsumer

# Sinir ağı versiyonu
manim -pqh neural_producer_consumer.py NeuralProducerConsumer
```

### 🎥 Animasyon Detayları

Animasyon şu bileşenleri içerir:

1. **Producer (Üretici)**: Mavi kutuda gösterilir, sürekli veri üretir
2. **Buffer (Tampon)**: Ortada sarı dikdörtgen, 5 slotlu kapasite
3. **Consumer (Tüketici)**: Yeşil kutuda gösterilir, veriyi işler

Animasyon akışı:
- Producer veri üretir ve buffer'a ekler
- Buffer dolduğunda Producer bekler
- Consumer buffer'dan veri alır ve işler
- Buffer boşsa Consumer bekler

### 📹 Oluşturulan Videolar

Proje kapsamında aşağıdaki videolar oluşturulmuştur:

#### 1. Producer-Consumer Animasyonu
- **İngilizce Versiyon**: `media/videos/temp_render/1080p60/ProducerConsumer_en.mp4`
- **Türkçe Versiyon**: `media/videos/temp_render/1080p60/ProducerConsumer_tr.mp4`

#### 2. Neural Producer-Consumer Animasyonu
- **İngilizce Versiyon**: `media/videos/temp_render/1080p60/NeuralProducerConsumer_en.mp4`
- **Türkçe Versiyon**: `media/videos/temp_render/1080p60/NeuralProducerConsumer_tr.mp4`

Tüm videolar 1080p 60fps kalitesinde render edilmiştir.

### 🏷️ Anahtar Kelimeler

`üretici-tüketici-problemi` `manim-animasyon` `eşzamanlı-programlama` `thread-senkronizasyon` `tampon-yönetimi` `eğitsel-görselleştirme` `bilgisayar-bilimi-eğitimi` `işletim-sistemleri-kavramları` `sinir-ağı-görselleştirme` `python-animasyon` `manim-topluluğu` `cs-eğitim` `threading-görselleştirme` `senkronizasyon-primitifleri` `animasyonlu-algoritmalar`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⭐ Star History

If you find this project helpful, please consider giving it a star!

## 📧 Contact

For questions or feedback, please open an issue on GitHub.