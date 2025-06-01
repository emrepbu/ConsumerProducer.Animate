# Producer-Consumer Animation

Animated visualization of Producer-Consumer problem using Manim. Features buffer management, synchronization, and neural network implementations. Educational tool for understanding concurrent programming concepts.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Manim](https://img.shields.io/badge/ManimCE-v0.17.0+-red.svg)](https://www.manim.community/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[English](#english) | [Türkçe](#türkçe)

## English

### Features

- Visual representation of Producer and Consumer components
- Limited capacity buffer visualization
- Data production and consumption animations
- Waiting animations for full/empty buffer states
- Neural network-based producer-consumer variant
- CPU Clock signal visualization
- Bilingual support (English/Turkish)

### Installation

1. Ensure Python 3.8+ is installed
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

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

# CPU Clock version
manim -pqh cpu_clock_animation.py CPUClock
```

### Animation Details

The animation includes these components:

1. **Producer**: Shown in blue box, continuously generates data
2. **Buffer**: Yellow rectangle in center, 5-slot capacity
3. **Consumer**: Shown in green box, processes data

Animation flow:
- Producer generates data and adds to buffer
- Producer waits when buffer is full
- Consumer takes data from buffer and processes it
- Consumer waits when buffer is empty

### Generated Videos

The project includes the following rendered videos (English versions):

| Animation | Preview | Download |
|-----------|---------|----------|
| **Producer-Consumer** | <video src="https://github.com/user-attachments/assets/4b5e8c9e-2f8e-4bcd-ab93-60a1b8f0c2b1" width="300"></video> | [Download MP4](media/videos/producer_consumer_animation/1080p60/ProducerConsumer_en.mp4) |
| **Neural Producer-Consumer** | <video src="https://github.com/user-attachments/assets/1d8e9c35-6b68-4bb5-b64f-2e0f7e36cc25" width="300"></video> | [Download MP4](media/videos/neural_producer_consumer/1080p60/NeuralProducerConsumer_en.mp4) |
| **CPU Clock Signal** | <video src="https://github.com/user-attachments/assets/cpu-clock-video.mp4" width="300"></video> | [Download MP4](media/videos/cpu_clock_animation/1080p60/CPUClock_en.mp4) |

All videos are rendered in 1080p 60fps quality. Turkish versions are also available.

### Keywords

`producer-consumer-problem` `manim-animation` `concurrent-programming` `thread-synchronization` `buffer-management` `educational-visualization` `computer-science-education` `operating-systems-concepts` `neural-network-visualization` `cpu-clock-signal` `digital-signal-processing` `python-animation` `manim-community` `cs-education` `threading-visualization` `synchronization-primitives` `animated-algorithms`

---

## Türkçe

### Özellikler

- Producer (Üretici) ve Consumer (Tüketici) bileşenlerinin görsel temsili
- Sınırlı kapasiteli buffer (tampon bellek) gösterimi
- Veri üretimi ve tüketimi animasyonu
- Buffer dolu/boş durumlarında bekleme animasyonları
- Sinir ağı tabanlı üretici-tüketici varyantı
- CPU Saat sinyali görselleştirmesi
- İki dil desteği (İngilizce/Türkçe)

### Kurulum

1. Python 3.8+ yüklü olduğundan emin olun
2. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

### Kullanım

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

# CPU Saat versiyonu
manim -pqh cpu_clock_animation.py CPUClock
```

### Animasyon Detayları

Animasyon şu bileşenleri içerir:

1. **Producer (Üretici)**: Mavi kutuda gösterilir, sürekli veri üretir
2. **Buffer (Tampon)**: Ortada sarı dikdörtgen, 5 slotlu kapasite
3. **Consumer (Tüketici)**: Yeşil kutuda gösterilir, veriyi işler

Animasyon akışı:
- Producer veri üretir ve buffer'a ekler
- Buffer dolduğunda Producer bekler
- Consumer buffer'dan veri alır ve işler
- Buffer boşsa Consumer bekler

### Oluşturulan Videolar

Proje kapsamında aşağıdaki videolar oluşturulmuştur (Türkçe versiyonlar):

| Animasyon | Önizleme | İndir |
|-----------|----------|--------|
| **Producer-Consumer** | <video src="https://github.com/user-attachments/assets/1ee88769-8af8-4c7f-a318-e2f83f93e53f" width="300"></video> | [MP4 İndir](media/videos/producer_consumer_animation/1080p60/ProducerConsumer_tr.mp4) |
| **Neural Producer-Consumer** | <video src="https://github.com/user-attachments/assets/7dc2dd33-6d02-48ba-bb23-b1861e96e38d" width="300"></video> | [MP4 İndir](media/videos/neural_producer_consumer/1080p60/NeuralProducerConsumer_tr.mp4) |
| **CPU Saat Sinyali** | <video src="https://github.com/user-attachments/assets/cpu-clock-video-tr.mp4" width="300"></video> | [MP4 İndir](media/videos/cpu_clock_animation/1080p60/CPUClock_tr.mp4) |

Tüm videolar 1080p 60fps kalitesinde render edilmiştir. İngilizce versiyonlar da mevcuttur.

### Anahtar Kelimeler

`üretici-tüketici-problemi` `manim-animasyon` `eşzamanlı-programlama` `thread-senkronizasyon` `tampon-yönetimi` `eğitsel-görselleştirme` `bilgisayar-bilimi-eğitimi` `işletim-sistemleri-kavramları` `sinir-ağı-görselleştirme` `cpu-saat-sinyali` `dijital-sinyal-işleme` `python-animasyon` `manim-topluluğu` `cs-eğitim` `threading-görselleştirme` `senkronizasyon-primitifleri` `animasyonlu-algoritmalar`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Star History

If you find this project helpful, please consider giving it a star!

## Contact

For questions or feedback, please open an issue on GitHub.
