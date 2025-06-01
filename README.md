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
| **Producer-Consumer** | <video src="https://github.com/user-attachments/assets/e307194b-9e8f-42e2-a1cd-71c9e1798adf" width="300"></video> | [Download MP4](media/videos/temp_render/1080p60/ProducerConsumer_en.mp4) |
| **Neural Producer-Consumer** | <video src="https://github.com/user-attachments/assets/b9f2d98c-350a-4687-a6de-48ec8b9779f1" width="300"></video> | [Download MP4](media/videos/temp_render/1080p60/NeuralProducerConsumer_en.mp4) |
| **CPU Clock Signal** | <video src="https://github.com/user-attachments/assets/03eb7b85-e4eb-4331-8a9a-9ca14c4f5ca7" width="300"></video> | [Download MP4](media/videos/temp_render/1080p60/CPUClock_en.mp4) |

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
| **Producer-Consumer** | <video src="https://github.com/user-attachments/assets/503493ed-06ce-4421-89e9-033266cfdd76" width="300"></video> | [MP4 İndir](media/videos/temp_render/1080p60/ProducerConsumer_tr.mp4) |
| **Neural Producer-Consumer** | <video src="https://github.com/user-attachments/assets/d8c227e5-5277-4030-a9e3-c92acc57b1fd" width="300"></video> | [MP4 İndir](media/videos/temp_render/1080p60/NeuralProducerConsumer_tr.mp4) |
| **CPU Saat Sinyali** | <video src="https://github.com/user-attachments/assets/dbd40c84-5072-4f10-87c3-f8abf7f27da2" width="300"></video> | [MP4 İndir](media/videos/temp_render/1080p60/CPUClock_tr.mp4) |

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



