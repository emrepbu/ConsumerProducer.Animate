#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Choose language / Dil seçin:"
echo "1. English"
echo "2. Türkçe"

read -p "Enter your choice / Seçiminizi girin (1-2): " lang_choice

case $lang_choice in
    1)
        LANG="en"
        ;;
    2)
        LANG="tr"
        ;;
    *)
        echo "Invalid choice. Defaulting to Turkish / Geçersiz seçim. Varsayılan olarak Türkçe kullanılacak."
        LANG="tr"
        ;;
esac

echo ""
echo "Choose rendering option / Render seçeneğini seçin:"
echo "1. Render as high quality video (MP4 - 1080p60) / Yüksek kaliteli video (MP4 - 1080p60)"
echo "2. Render as high quality GIF / Yüksek kaliteli GIF"

read -p "Enter your choice / Seçiminizi girin (1-2): " choice

case $choice in
    1)
        echo "Rendering as high quality MP4 video (1080p60)..."
        # Create temporary Python file with selected language parameter
        cat > temp_render.py << EOF
from producer_consumer_animation import ProducerConsumerSimple

class TempScene(ProducerConsumerSimple):
    def __init__(self):
        super().__init__(language="${LANG}")

if __name__ == "__main__":
    scene = TempScene()
    scene.render()
EOF
        manim -pqh --fps 60 temp_render.py TempScene -o "ProducerConsumer_${LANG}"
        rm temp_render.py
        ;;
    2)
        echo "Rendering as high quality GIF (1080p30)..."
        # Create temporary Python file with selected language parameter
        cat > temp_render.py << EOF
from producer_consumer_animation import ProducerConsumerSimple

class TempScene(ProducerConsumerSimple):
    def __init__(self):
        super().__init__(language="${LANG}")

if __name__ == "__main__":
    scene = TempScene()
    scene.render()
EOF
        manim -pqh --format=gif --fps 30 temp_render.py TempScene -o "ProducerConsumer_${LANG}"
        rm temp_render.py
        ;;
    *)
        echo "Invalid choice. Please run the script again. / Geçersiz seçim. Lütfen scripti tekrar çalıştırın."
        exit 1
        ;;
esac

echo ""
echo "Animation complete! Check the 'media' folder for output files."