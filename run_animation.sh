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
echo "Dil / Language:"
echo "1. English"
echo "2. Türkçe"

read -p "Seçim / Choice (1-2): " lang_choice

case $lang_choice in
    1)
        LANG="en"
        ;;
    2)
        LANG="tr"
        ;;
    *)
        echo "Varsayılan: Türkçe"
        LANG="tr"
        ;;
esac

echo ""
echo "Animasyon / Animation:"
echo "1. Producer-Consumer"
echo "2. Neural Network Multi-Producer"
echo "3. CPU Clock"
echo "4. All Animations (Both Languages)"

read -p "Seçim / Choice (1-4): " anim_choice

case $anim_choice in
    1)
        ANIM_FILE="producer_consumer_animation.py"
        ANIM_CLASS="ProducerConsumer"
        ;;
    2)
        ANIM_FILE="neural_producer_consumer.py"
        ANIM_CLASS="NeuralProducerConsumer"
        ;;
    3)
        ANIM_FILE="cpu_clock_animation.py"
        ANIM_CLASS="CPUClock"
        ;;
    4)
        ANIM_FILE="all"
        ANIM_CLASS="all"
        ;;
    *)
        echo "Varsayılan: Producer-Consumer"
        ANIM_FILE="producer_consumer_animation.py"
        ANIM_CLASS="ProducerConsumer"
        ;;
esac

echo ""
echo "Format:"
echo "1. MP4 (1080p60)"
echo "2. GIF"

read -p "Seçim / Choice (1-2): " choice

if [ "$ANIM_FILE" = "all" ]; then
    case $choice in
        1)
            echo "Rendering all animations as MP4..."
            
            # Array of animations: file_name class_name
            animations=(
                "producer_consumer_animation.py ProducerConsumer"
                "neural_producer_consumer.py NeuralProducerConsumer"
                "cpu_clock_animation.py CPUClock"
            )
            
            for anim in "${animations[@]}"; do
                read -r file class <<< "$anim"
                
                for lang in "en" "tr"; do
                    echo "Rendering ${class}_${lang}.mp4..."
                    cat > temp_render.py << EOF
from ${file%.*} import ${class}

class TempScene(${class}):
    def __init__(self):
        super().__init__(language="${lang}")

if __name__ == "__main__":
    scene = TempScene()
    scene.render()
EOF
                    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m manim -pqh --fps 60 temp_render.py TempScene -o "${class}_${lang}"
                    rm temp_render.py
                done
            done
            ;;
        2)
            echo "Rendering all animations as GIF..."
            
            # Array of animations: file_name class_name
            animations=(
                "producer_consumer_animation.py ProducerConsumer"
                "neural_producer_consumer.py NeuralProducerConsumer"
                "cpu_clock_animation.py CPUClock"
            )
            
            for anim in "${animations[@]}"; do
                read -r file class <<< "$anim"
                
                for lang in "en" "tr"; do
                    echo "Rendering ${class}_${lang}.gif..."
                    cat > temp_render.py << EOF
from ${file%.*} import ${class}

class TempScene(${class}):
    def __init__(self):
        super().__init__(language="${lang}")

if __name__ == "__main__":
    scene = TempScene()
    scene.render()
EOF
                    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m manim -pqh --format=gif --fps 30 temp_render.py TempScene -o "${class}_${lang}"
                    rm temp_render.py
                done
            done
            ;;
        *)
            echo "Geçersiz seçim!"
            exit 1
            ;;
    esac
else
    case $choice in
        1)
            echo "Rendering MP4..."
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
            echo "Rendering GIF..."
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
            echo "Geçersiz seçim!"
            exit 1
            ;;
    esac
fi

echo ""
echo "Tamamlandı! / Complete!"