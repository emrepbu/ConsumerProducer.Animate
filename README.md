# Consumer-Producer Animation

Bu proje, Consumer-Producer (Tüketici-Üretici) yazılım modelini görselleştiren bir Manim animasyonu içerir.

## Özellikler

- Producer (Üretici) ve Consumer (Tüketici) bileşenlerinin görsel temsili
- Sınırlı kapasiteli buffer (tampon bellek) gösterimi
- Veri üretimi ve tüketimi animasyonu
- Buffer dolu/boş durumlarında bekleme animasyonları
- Algoritma kodlarının görüntülenmesi

## Kurulum

1. Python 3.8+ yüklü olduğundan emin olun
2. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

Animasyonu çalıştırmak için:

```bash
./run_animation.sh
```

Veya manuel olarak:

```bash
# Video olarak render et (MP4)
manim -pqh producer_consumer_animation.py ProducerConsumerSimple

# Düşük kalitede önizleme
manim -pql producer_consumer_animation.py ProducerConsumerSimple

# GIF olarak render et
manim -pql --format=gif producer_consumer_animation.py ProducerConsumerSimple

# Slayt sunumu olarak (manim-slides)
manim-slides render producer_consumer_animation.py ProducerConsumerAnimation
manim-slides present ProducerConsumerAnimation
```

## Animasyon Detayları

Animasyon şu bileşenleri içerir:

1. **Producer (Üretici)**: Mavi kutuda gösterilir, sürekli veri üretir
2. **Buffer (Tampon)**: Ortada sarı dikdörtgen, 5 slotlu kapasite
3. **Consumer (Tüketici)**: Yeşil kutuda gösterilir, veriyi işler

Animasyon akışı:
- Producer veri üretir ve buffer'a ekler
- Buffer dolduğunda Producer bekler (WAIT)
- Consumer buffer'dan veri alır ve işler
- Buffer boşsa Consumer bekler (WAIT)

## Oluşturulan Videolar

Proje kapsamında aşağıdaki videolar oluşturulmuştur:

### 1. Producer-Consumer Animasyonu
- **Türkçe Versiyon**: `media/videos/temp_render/1080p60/ProducerConsumer_tr.mp4`
- **İngilizce Versiyon**: `media/videos/temp_render/1080p60/ProducerConsumer_en.mp4`

### 2. Neural Producer-Consumer Animasyonu
- **Türkçe Versiyon**: `media/videos/temp_render/1080p60/NeuralProducerConsumer_tr.mp4`
- **İngilizce Versiyon**: `media/videos/temp_render/1080p60/NeuralProducerConsumer_en.mp4`

Bu videolar 1080p 60fps kalitesinde render edilmiştir ve hem Türkçe hem de İngilizce versiyonları mevcuttur.

