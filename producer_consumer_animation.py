from manim import *
import random


class ProducerConsumerBase(Scene):
    """Base class for Producer-Consumer animation"""
    
    def __init__(self, language="en", **kwargs):
        super().__init__(**kwargs)
        self.language = language
        self.setup_translations()
    
    def setup_translations(self):
        """Set up text translations based on language"""
        if self.language == "tr":
            self.texts = {
                "title": "Üretici-Tüketici Problemi",
                "producer": "Üretici",
                "consumer": "Tüketici",
                "buffer": "Tampon",
                "buffer_size": "Tampon Boyutu: {}",
                "current_size": "Mevcut: {}",
                "producing": "Üretiliyor...",
                "consuming": "Tüketiliyor...",
                "waiting": "Bekliyor...",
                "cycle": "Döngü {}/8",
                "producer_alg": r"\textbf{Üretici Algoritması}",
                "consumer_alg": r"\textbf{Tüketici Algoritması}",
                "end_text": "Simülasyon Tamamlandı!"
            }
        else:
            self.texts = {
                "title": "Producer-Consumer Problem",
                "producer": "Producer",
                "consumer": "Consumer", 
                "buffer": "Buffer",
                "buffer_size": "Buffer Size: {}",
                "current_size": "Current: {}",
                "producing": "Producing...",
                "consuming": "Consuming...",
                "waiting": "Waiting...",
                "cycle": "Cycle {}/8",
                "producer_alg": r"\textbf{Producer Algorithm}",
                "consumer_alg": r"\textbf{Consumer Algorithm}",
                "end_text": "Simulation Complete!"
            }
    
    def construct(self):
        # Set background color
        self.camera.background_color = "#1a1a1a"
        
        # Main title
        title = Text(self.texts["title"], font_size=48, weight=BOLD, color=WHITE).to_edge(UP, buff=0.3)
        
        # Language indicator - top right corner
        lang_text = "TR | Türkçe" if self.language == "tr" else "EN | English"
        lang_indicator = Text(
            lang_text, 
            font_size=16, 
            weight=BOLD, 
            color=WHITE
        )
        lang_box = RoundedRectangle(
            width=lang_indicator.width + 0.4,
            height=lang_indicator.height + 0.2,
            corner_radius=0.1,
            color=GOLD, 
            fill_color=GOLD,
            fill_opacity=0.2,
            stroke_width=2
        )
        lang_group = VGroup(lang_box, lang_indicator).arrange(ORIGIN)
        lang_group.to_corner(UR, buff=0.2)
        
        self.play(
            Write(title),
            FadeIn(lang_group)
        )
        self.wait(0.5)
        
        # Center Y position for main components
        main_y = 0.8
        
        # Producer box - LEFT
        producer_box = RoundedRectangle(
            corner_radius=0.15, 
            width=3, 
            height=2.5, 
            color=BLUE, 
            fill_color=BLUE, 
            fill_opacity=0.1,
            stroke_width=3
        )
        producer_text = Text(self.texts["producer"], color=BLUE, font_size=32, weight=BOLD)
        producer_group = VGroup(producer_text, producer_box).arrange(DOWN, buff=0.2)
        producer_group.move_to(LEFT * 4.5 + UP * main_y)
        
        # Buffer box - CENTER
        buffer_box = RoundedRectangle(
            corner_radius=0.15,
            width=3.5, 
            height=3.5, 
            color=GREEN, 
            fill_color=GREEN,
            fill_opacity=0.1,
            stroke_width=3
        )
        buffer_text = Text(self.texts["buffer"], color=GREEN, font_size=32, weight=BOLD)
        buffer_size_text = Text(self.texts["buffer_size"].format(5), font_size=20, color=GRAY_B)
        buffer_current_text = Text(self.texts["current_size"].format(0), font_size=24, color=YELLOW, weight=BOLD)
        
        # Buffer info outside the box
        buffer_info = VGroup(buffer_size_text, buffer_current_text).arrange(DOWN, buff=0.1)
        buffer_group = VGroup(buffer_text, buffer_box).arrange(DOWN, buff=0.2)
        buffer_group.move_to(UP * main_y)
        buffer_info.next_to(buffer_box, DOWN, buff=0.2)
        
        # Consumer box - RIGHT
        consumer_box = RoundedRectangle(
            corner_radius=0.15,
            width=3, 
            height=2.5, 
            color=RED,
            fill_color=RED,
            fill_opacity=0.1,
            stroke_width=3
        )
        consumer_text = Text(self.texts["consumer"], color=RED, font_size=32, weight=BOLD)
        consumer_group = VGroup(consumer_text, consumer_box).arrange(DOWN, buff=0.2)
        consumer_group.move_to(RIGHT * 4.5 + UP * main_y)
        
        # Position all elements
        self.play(
            Create(producer_group),
            Create(buffer_group),
            Create(consumer_group),
            Write(buffer_info),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Arrows - slightly below the boxes
        arrow_y_offset = -0.3
        arrow_p_to_b = Arrow(
            producer_box.get_right() + UP * arrow_y_offset, 
            buffer_box.get_left() + UP * arrow_y_offset, 
            color=YELLOW, 
            stroke_width=4,
            buff=0.1,
            max_stroke_width_to_length_ratio=10,
            max_tip_length_to_length_ratio=0.3
        )
        arrow_b_to_c = Arrow(
            buffer_box.get_right() + UP * arrow_y_offset, 
            consumer_box.get_left() + UP * arrow_y_offset, 
            color=YELLOW, 
            stroke_width=4,
            buff=0.1,
            max_stroke_width_to_length_ratio=10,
            max_tip_length_to_length_ratio=0.3
        )
        
        self.play(Create(arrow_p_to_b), Create(arrow_b_to_c))
        
        # Algorithm descriptions - BOTTOM SECTION
        # Producer algorithm
        producer_algo_title = Tex(self.texts["producer_alg"], font_size=20, color=BLUE)
        producer_algo_code = MathTex(
            r"\begin{array}{l}" + 
            r"\textbf{ALGORITHM Producer} \\" +
            r"\quad \textbf{WHILE } \text{system is running} \textbf{ DO} \\" +
            r"\quad \quad \text{data} \leftarrow \text{generateNewData()} \\" +
            r"\quad \quad \textbf{IF } \text{buffer has space} \textbf{ THEN} \\" +
            r"\quad \quad \quad \text{add data to buffer} \\" +
            r"\quad \quad \textbf{ELSE} \\" +
            r"\quad \quad \quad \text{wait until space becomes available} \\" +
            r"\quad \quad \textbf{END IF} \\" +
            r"\quad \textbf{END WHILE} \\" +
            r"\textbf{END ALGORITHM}" +
            r"\end{array}",
            font_size=12,
            color=BLUE_B
        )
        producer_algo = VGroup(producer_algo_title, producer_algo_code).arrange(DOWN, buff=0.15)
        producer_algo.move_to(LEFT * 4 + DOWN * 2.8)
        
        # Consumer algorithm
        consumer_algo_title = Tex(self.texts["consumer_alg"], font_size=20, color=RED)
        consumer_algo_code = MathTex(
            r"\begin{array}{l}" +
            r"\textbf{ALGORITHM Consumer} \\" +
            r"\quad \textbf{WHILE } \text{system is running} \textbf{ DO} \\" +
            r"\quad \quad \textbf{IF } \text{buffer has data} \textbf{ THEN} \\" +
            r"\quad \quad \quad \text{data} \leftarrow \text{get data from buffer} \\" +
            r"\quad \quad \quad \text{process(data)} \\" +
            r"\quad \quad \textbf{ELSE} \\" +
            r"\quad \quad \quad \text{wait until data becomes available} \\" +
            r"\quad \quad \textbf{END IF} \\" +
            r"\quad \textbf{END WHILE} \\" +
            r"\textbf{END ALGORITHM}" +
            r"\end{array}",
            font_size=12,
            color=RED_B
        )
        consumer_algo = VGroup(consumer_algo_title, consumer_algo_code).arrange(DOWN, buff=0.15)
        consumer_algo.move_to(RIGHT * 4 + DOWN * 2.8)
        
        self.play(
            Write(producer_algo),
            Write(consumer_algo),
            run_time=2
        )
        self.wait(1)
        
        # Simulation state
        buffer_items = []
        max_buffer_size = 5
        
        # Status texts - above the boxes
        producer_status = Text(self.texts["producing"], color=BLUE, font_size=28, weight=BOLD)
        producer_status.next_to(producer_group, UP, buff=0.3)
        
        consumer_status = Text(self.texts["waiting"], color=RED, font_size=28, weight=BOLD)
        consumer_status.next_to(consumer_group, UP, buff=0.3)
        
        # Run the simulation
        for cycle in range(8):
            # Cycle counter - center, above algorithms
            cycle_text = Text(
                self.texts["cycle"].format(cycle + 1), 
                font_size=28, 
                weight=BOLD, 
                color=GOLD
            )
            cycle_text.move_to(DOWN * 3.1)
            self.play(Write(cycle_text), run_time=0.5)
            
            # Producer produces
            if len(buffer_items) < max_buffer_size:
                self.play(Write(producer_status), run_time=0.5)
                
                # Create data item
                data_value = random.randint(1, 99)
                data_item = Circle(radius=0.25, color=BLUE_C, fill_opacity=0.8, stroke_width=2)
                data_text = Text(str(data_value), font_size=20, color=WHITE, weight=BOLD)
                data_text.move_to(data_item.get_center())
                data_group = VGroup(data_item, data_text)
                data_group.move_to(producer_box.get_center())
                
                self.play(Create(data_group), run_time=0.4)
                
                # Move to buffer - proper positioning
                rows = 2  # 2 rows
                cols = 3  # 3 columns
                index = len(buffer_items)
                row = index // cols
                col = index % cols
                
                # Grid position inside buffer
                x_offset = (col - 1) * 0.7  # -0.7, 0, 0.7
                y_offset = (0.5 - row) * 0.7  # 0.5, -0.2
                
                target_pos = buffer_box.get_center() + RIGHT * x_offset + UP * y_offset
                self.play(data_group.animate.move_to(target_pos), run_time=0.6)
                buffer_items.append(data_group)
                
                # Update buffer count
                new_count_text = Text(
                    self.texts["current_size"].format(len(buffer_items)), 
                    font_size=24, 
                    color=YELLOW,
                    weight=BOLD
                )
                new_count_text.move_to(buffer_current_text.get_center())
                self.play(Transform(buffer_current_text, new_count_text), run_time=0.3)
                
                self.play(FadeOut(producer_status), run_time=0.3)
            else:
                # Buffer is full
                wait_text = Text(self.texts["waiting"], color=ORANGE, font_size=28, weight=BOLD)
                wait_text.next_to(producer_group, UP, buff=0.3)
                self.play(Write(wait_text), run_time=0.5)
                self.wait(0.5)
                self.play(FadeOut(wait_text), run_time=0.3)
            
            # Consumer consumes
            if len(buffer_items) > 0 and cycle % 2 == 1:
                consumer_status_active = Text(self.texts["consuming"], color=RED, font_size=28, weight=BOLD)
                consumer_status_active.next_to(consumer_group, UP, buff=0.3)
                self.play(Write(consumer_status_active), run_time=0.5)
                
                # Take from buffer
                data_to_consume = buffer_items.pop(0)
                self.play(data_to_consume.animate.move_to(consumer_box.get_center()), run_time=0.6)
                self.play(FadeOut(data_to_consume), run_time=0.4)
                
                # Rearrange remaining items
                for i, item in enumerate(buffer_items):
                    row = i // cols
                    col = i % cols
                    x_offset = (col - 1) * 0.7
                    y_offset = (0.5 - row) * 0.7
                    new_pos = buffer_box.get_center() + RIGHT * x_offset + UP * y_offset
                    self.play(item.animate.move_to(new_pos), run_time=0.3)
                
                # Update buffer count
                new_count_text = Text(
                    self.texts["current_size"].format(len(buffer_items)), 
                    font_size=24, 
                    color=YELLOW,
                    weight=BOLD
                )
                new_count_text.move_to(buffer_current_text.get_center())
                self.play(Transform(buffer_current_text, new_count_text), run_time=0.3)
                
                self.play(FadeOut(consumer_status_active), run_time=0.3)
            
            self.play(FadeOut(cycle_text), run_time=0.3)
            self.wait(0.3)
        
        # End animation
        end_text = Text(
            self.texts["end_text"], 
            font_size=40, 
            color=GOLD, 
            weight=BOLD
        ).move_to(DOWN * 1.8)
        self.play(Write(end_text))
        self.wait(2)


class ProducerConsumerSimple(ProducerConsumerBase):
    """Simple version for video rendering"""
    
    def __init__(self, language="tr", **kwargs):
        super().__init__(language=language, **kwargs)