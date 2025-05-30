#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pip install -r requirements.txt

# Install ManimML from submodule
echo "Installing ManimML from submodule..."
if [ -d "ManimML" ]; then
    cd ManimML && /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pip install -e . && cd ..
else
    echo "ManimML submodule not found. Initializing submodules..."
    git submodule init
    git submodule update
    cd ManimML && /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pip install -e . && cd ..
fi

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
echo "Choose animation type / Animasyon türünü seçin:"
echo "1. Producer-Consumer / Üretici-Tüketici"
echo "2. Neural Network Style Multi-Producer-Consumer / Sinir Ağı Tarzı Çoklu Üretici-Tüketici"

read -p "Enter animation choice / Animasyon seçiminizi girin (1-2): " anim_choice

case $anim_choice in
    1)
        ANIM_FILE="producer_consumer_animation.py"
        ANIM_CLASS="ProducerConsumer"
        ;;
    2)
        ANIM_FILE="neural_producer_consumer.py"
        ANIM_CLASS="NeuralProducerConsumer"
        ;;
    *)
        echo "Invalid choice. Defaulting to animation / Geçersiz seçim. Varsayılan animasyon kullanılacak."
        ANIM_FILE="producer_consumer_animation.py"
        ANIM_CLASS="ProducerConsumer"
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
from ${ANIM_FILE%.*} import ${ANIM_CLASS}

class TempScene(${ANIM_CLASS}):
    def __init__(self):
        super().__init__(language="${LANG}")

if __name__ == "__main__":
    scene = TempScene()
    scene.render()
EOF
        /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m manim -pqh --fps 60 temp_render.py TempScene -o "${ANIM_CLASS}_${LANG}"
        rm temp_render.py
        ;;
    2)
        echo "Rendering as high quality GIF (1080p30)..."
        # Create temporary Python file with selected language parameter
        cat > temp_render.py << EOF
from ${ANIM_FILE%.*} import ${ANIM_CLASS}

class TempScene(${ANIM_CLASS}):
    def __init__(self):
        super().__init__(language="${LANG}")

if __name__ == "__main__":
    scene = TempScene()
    scene.render()
EOF
        /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m manim -pqh --format=gif --fps 30 temp_render.py TempScene -o "${ANIM_CLASS}_${LANG}"
        rm temp_render.py
        ;;
    *)
        echo "Invalid choice. Please run the script again. / Geçersiz seçim. Lütfen scripti tekrar çalıştırın."
        exit 1
        ;;
esac

echo ""
echo "Animation complete! Check the 'media' folder for output files."