from manim import *
try:
    from manim_ml.neural_network.layers import FeedForwardLayer
    from manim_ml.neural_network.neural_network import NeuralNetwork
    MANIM_ML_AVAILABLE = True
except ImportError:
    MANIM_ML_AVAILABLE = False
    print("manim-ml not available. Using fallback implementation.")

import random
import numpy as np

config.background_color = "#0f0f0f"


class NeuralProducerConsumerBase(Scene):
    """Neural network style Producer-Consumer animation with multiple agents"""
    
    def __init__(self, language="en", **kwargs):
        super().__init__(**kwargs)
        self.language = language
        self.setup_translations()
    
    def setup_translations(self):
        """Set up text translations based on language"""
        if self.language == "tr":
            self.texts = {
                "title": "Çoklu Üretici-Tüketici Ağı",
                "producers": "Üreticiler",
                "consumers": "Tüketiciler",
                "buffer_layer": "Tampon Katmanı",
                "garbage_collector": "Çöp Toplayıcı",
                "data_flow": "Veri Akışı",
                "processing": "İşleniyor...",
                "waiting": "Bekliyor...",
                "dropped": "Düşürüldü: {}",
                "cycle": "Döngü {}/10",
                "buffer_added": "Yeni Buffer Eklendi!",
                "system_upgraded": "Sistem Güncellendi",
                "neural_title": "Sinir Ağı Tarzında Üretici-Tüketici Modeli",
                "end_text": "Ağ Simülasyonu Tamamlandı!"
            }
        else:
            self.texts = {
                "title": "Multi-Producer Consumer Network",
                "producers": "Producers",
                "consumers": "Consumers", 
                "buffer_layer": "Buffer Layer",
                "garbage_collector": "Garbage Collector",
                "data_flow": "Data Flow",
                "processing": "Processing...",
                "waiting": "Waiting...",
                "dropped": "Dropped: {}",
                "cycle": "Cycle {}/10",
                "buffer_added": "New Buffer Added!",
                "system_upgraded": "System Upgraded",
                "neural_title": "Neural Network Style Producer-Consumer Model",
                "end_text": "Network Simulation Complete!"
            }
    
    def create_neural_network_fallback(self):
        """Create a fallback neural network visualization when manim-ml is not available"""
        producer_nodes = []
        for i in range(4):
            node = Circle(radius=0.3, color=BLUE, fill_opacity=0.8)
            node.move_to(LEFT * 5 + UP * (1.5 - i * 1))
            producer_nodes.append(node)
        
        buffer_nodes = []
        for i in range(4):
            node = Circle(radius=0.25, color=GREEN, fill_opacity=0.6)
            node.move_to(UP * (1.5 - i * 1))
            buffer_nodes.append(node)
        
        consumer_nodes = []
        for i in range(3):
            node = Circle(radius=0.3, color=RED, fill_opacity=0.8)
            node.move_to(RIGHT * 5 + UP * (1 - i * 1))
            consumer_nodes.append(node)
        
        connections = []
        
        for p_node in producer_nodes:
            for b_node in buffer_nodes:
                line = Line(p_node.get_center(), b_node.get_center(), 
                           color=GRAY, stroke_width=1, stroke_opacity=0.3)
                connections.append(line)
        
        for b_node in buffer_nodes:
            for c_node in consumer_nodes:
                line = Line(b_node.get_center(), c_node.get_center(),
                           color=GRAY, stroke_width=1, stroke_opacity=0.3)
                connections.append(line)
        
        garbage_collector = RoundedRectangle(
            width=2.5, height=1.5, corner_radius=0.2,
            color=DARK_GRAY, fill_color=DARK_GRAY, fill_opacity=0.7
        )
        garbage_collector.move_to(DOWN * 3)
        
        trash_icon = Text("GC", font_size=30, color=WHITE, weight=BOLD)
        trash_icon.move_to(garbage_collector.get_center())
        garbage_group = VGroup(garbage_collector, trash_icon)
        
        return producer_nodes, buffer_nodes, consumer_nodes, connections, garbage_group
    
    def create_data_packet(self, value, color=PURPLE):
        """Create a data packet visualization"""
        packet = Circle(radius=0.25, color=color, fill_opacity=0.9, stroke_width=2)
        text = Text(str(value), font_size=18, color=WHITE, weight=BOLD)
        text.move_to(packet.get_center())
        return VGroup(packet, text)
    
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        
        title = Text(self.texts["neural_title"], font_size=40, weight=BOLD, color=WHITE)
        title.to_edge(UP, buff=0.3)
        
        lang_text = "TR | Türkçe" if self.language == "tr" else "EN | English"
        lang_indicator = Text(lang_text, font_size=14, weight=BOLD, color=WHITE)
        lang_box = RoundedRectangle(
            width=lang_indicator.width + 0.3,
            height=lang_indicator.height + 0.15,
            corner_radius=0.08,
            color=GOLD, 
            fill_color=GOLD,
            fill_opacity=0.2,
            stroke_width=2
        )
        lang_group = VGroup(lang_box, lang_indicator).arrange(ORIGIN)
        lang_group.to_corner(UR, buff=0.2)
        
        self.play(Write(title), FadeIn(lang_group))
        self.wait(1)
        
        if MANIM_ML_AVAILABLE:
            try:
                input_layer = FeedForwardLayer(4, rectangle_color=BLUE, rectangle_fill_color=BLUE)
                hidden_layer = FeedForwardLayer(4, rectangle_color=GREEN, rectangle_fill_color=GREEN)
                output_layer = FeedForwardLayer(3, rectangle_color=RED, rectangle_fill_color=RED)
                
                nn = NeuralNetwork([input_layer, hidden_layer, output_layer], 
                                 layer_spacing=3)
                nn.move_to(ORIGIN)
                
                producer_nodes = input_layer.neurons
                buffer_nodes = hidden_layer.neurons  
                consumer_nodes = output_layer.neurons
                connections = nn.connections
                
                network_group = VGroup(nn)
                
            except Exception as e:
                print(f"manim-ml error: {e}. Using fallback.")
                producer_nodes, buffer_nodes, consumer_nodes, connections, garbage_group = self.create_neural_network_fallback()
                network_group = VGroup(*producer_nodes, *buffer_nodes, *consumer_nodes, *connections)
        else:
            producer_nodes, buffer_nodes, consumer_nodes, connections, garbage_group = self.create_neural_network_fallback()
            network_group = VGroup(*producer_nodes, *buffer_nodes, *consumer_nodes, *connections)
        
        if MANIM_ML_AVAILABLE and 'garbage_group' not in locals():
            garbage_collector = RoundedRectangle(
                width=2.5, height=1.5, corner_radius=0.2,
                color=DARK_GRAY, fill_color=DARK_GRAY, fill_opacity=0.7
            )
            garbage_collector.move_to(DOWN * 3)
            trash_icon = Text("GC", font_size=30, color=WHITE, weight=BOLD)
            trash_icon.move_to(garbage_collector.get_center())
            garbage_group = VGroup(garbage_collector, trash_icon)
        
        producer_label = Text(self.texts["producers"], font_size=24, color=BLUE, weight=BOLD)
        producer_label.next_to(producer_nodes[0], LEFT, buff=0.5)
        
        buffer_label = Text(self.texts["buffer_layer"], font_size=24, color=GREEN, weight=BOLD)
        buffer_label.next_to(buffer_nodes[1], UP, buff=0.5)
        
        consumer_label = Text(self.texts["consumers"], font_size=24, color=RED, weight=BOLD)
        consumer_label.next_to(consumer_nodes[0], RIGHT, buff=0.5)
        
        garbage_label = Text(self.texts["garbage_collector"], font_size=20, color=DARK_GRAY, weight=BOLD)
        garbage_label.next_to(garbage_group, DOWN, buff=0.3)
        
        self.play(
            Create(network_group),
            Write(producer_label),
            Write(buffer_label),
            Write(consumer_label),
            Create(garbage_group),
            Write(garbage_label),
            run_time=2
        )
        self.wait(1)
        
        buffer_states = [0] * len(buffer_nodes)
        buffer_capacity = 1
        buffer_counts = [0] * len(buffer_nodes)
        
        active_packets = []
        buffer_visual_packets = {}
        dropped_count = 0
        dropped_before_upgrade = 0
        garbage_collector = garbage_group[0]
        
        new_buffer_added = False
        
        for cycle in range(10):
            cycle_text = Text(
                self.texts["cycle"].format(cycle + 1),
                font_size=24,
                weight=BOLD,
                color=GOLD
            )
            cycle_text.to_edge(DOWN, buff=0.3)
            self.play(Write(cycle_text), run_time=0.3)
            
            animations = []
            
            active_producers = random.sample(range(len(producer_nodes)), k=random.randint(2, 4))
            active_consumers = []
            
            if active_packets and random.random() > 0.3:
                active_consumers = random.sample(range(len(consumer_nodes)), 
                                               k=min(len(active_packets), random.randint(1, 3)))
            
            producer_packets = []
            for p_idx in active_producers:
                data_value = random.randint(10, 99)
                packet = self.create_data_packet(data_value)
                packet.move_to(producer_nodes[p_idx].get_center())
                producer_packets.append((packet, p_idx, data_value))
                
                animations.append(Create(packet))
                animations.append(producer_nodes[p_idx].animate.set_fill(BLUE, opacity=1))
            
            packets_to_consume = []
            for c_idx in active_consumers:
                if not active_packets:
                    break
                    
                available_packets = [(i, packet, b_idx, value) for i, (packet, b_idx, value) in enumerate(active_packets)
                                   if buffer_counts[b_idx] > 0]
                
                if available_packets:
                    packet_idx, packet, b_idx, value = random.choice(available_packets)
                    packets_to_consume.append((c_idx, packet_idx, packet, b_idx, value))
                    
                    animations.append(consumer_nodes[c_idx].animate.set_fill(RED, opacity=1))
            
            if animations:
                self.play(*animations, run_time=0.3)
            
            movement_animations = []
            
            for packet, p_idx, value in producer_packets:
                available_buffers = [i for i, count in enumerate(buffer_counts) 
                                   if count < buffer_capacity]
                
                if available_buffers:
                    b_idx = random.choice(available_buffers)
                    
                    if b_idx not in buffer_visual_packets:
                        buffer_visual_packets[b_idx] = []
                    
                    target_pos = buffer_nodes[b_idx].get_center()
                    
                    movement_animations.append(packet.animate.scale(0.7).move_to(target_pos))
                    
                    buffer_counts[b_idx] += 1
                    active_packets.append((packet, b_idx, value))
                    buffer_visual_packets[b_idx].append(packet)
                else:
                    movement_animations.append(packet.animate.move_to(garbage_collector.get_center()))
                    dropped_count += 1
            
            packets_to_remove = []
            for c_idx, packet_idx, packet, b_idx, value in packets_to_consume:
                movement_animations.append(
                    packet.animate.scale(1/0.7).move_to(consumer_nodes[c_idx].get_center())
                )
                
                buffer_counts[b_idx] -= 1
                packets_to_remove.append(packet_idx)
                
                if packet in buffer_visual_packets[b_idx]:
                    buffer_visual_packets[b_idx].remove(packet)
            
            if movement_animations:
                self.play(*movement_animations, run_time=0.7)
            
            fade_animations = []
            
            for c_idx, packet_idx, packet, b_idx, value in packets_to_consume:
                fade_animations.append(FadeOut(packet))
            
            for packet, p_idx, value in producer_packets:
                available_buffers = [i for i, count in enumerate(buffer_counts) 
                                   if count < buffer_capacity + 1]
                if not available_buffers:
                    fade_animations.append(FadeOut(packet))
            
            for idx in sorted(packets_to_remove, reverse=True):
                if idx < len(active_packets):
                    active_packets.pop(idx)
            
            buffer_updates = []
            for i, node in enumerate(buffer_nodes):
                new_opacity = 0.6 + 0.4 * buffer_counts[i]/buffer_capacity
                buffer_updates.append(node.animate.set_fill(GREEN, opacity=new_opacity))
            
            reset_animations = []
            for p_idx in active_producers:
                reset_animations.append(producer_nodes[p_idx].animate.set_fill(BLUE, opacity=0.8))
            for c_idx in active_consumers:
                reset_animations.append(consumer_nodes[c_idx].animate.set_fill(RED, opacity=0.8))
            
            all_cleanup = fade_animations + buffer_updates + reset_animations
            if all_cleanup:
                self.play(*all_cleanup, run_time=0.3)
            
            
            self.play(FadeOut(cycle_text), run_time=0.3)
            
            if cycle == 4 and not new_buffer_added:
                self.wait(0.5)
                
                upgrade_text = Text(
                    self.texts["system_upgraded"],
                    font_size=32,
                    color=YELLOW,
                    weight=BOLD
                )
                upgrade_text.move_to(UP * 3.5)
                
                new_buffer = Circle(radius=0.25, color=GREEN, fill_opacity=0.6)
                new_buffer_pos = DOWN * 2.5
                new_buffer.move_to(new_buffer_pos)
                
                new_producer_connections = []
                for p_node in producer_nodes:
                    line = Line(p_node.get_center(), new_buffer.get_center(), 
                               color=GRAY, stroke_width=1, stroke_opacity=0.3)
                    new_producer_connections.append(line)
                
                new_consumer_connections = []
                for c_node in consumer_nodes:
                    line = Line(new_buffer.get_center(), c_node.get_center(),
                               color=GRAY, stroke_width=1, stroke_opacity=0.3)
                    new_consumer_connections.append(line)
                
                self.play(
                    Write(upgrade_text),
                    Create(new_buffer),
                    *[Create(conn) for conn in new_producer_connections],
                    *[Create(conn) for conn in new_consumer_connections],
                    run_time=2
                )
                
                buffer_added_text = Text(
                    self.texts["buffer_added"],
                    font_size=24,
                    color=GREEN,
                    weight=BOLD
                )
                buffer_added_text.next_to(new_buffer, DOWN, buff=0.3)
                self.play(Write(buffer_added_text), run_time=0.5)
                
                buffer_nodes.append(new_buffer)
                connections.extend(new_producer_connections)
                connections.extend(new_consumer_connections)
                
                buffer_counts.append(0)
                buffer_visual_packets[len(buffer_nodes) - 1] = []
                
                new_buffer_added = True
                dropped_before_upgrade = dropped_count
                
                self.play(
                    buffer_label.animate.next_to(buffer_nodes[2], UP, buff=0.5),
                    run_time=0.5
                )
                
                self.wait(1)
                self.play(
                    FadeOut(upgrade_text),
                    FadeOut(buffer_added_text),
                    run_time=0.5
                )
            
            self.wait(0.5)
        
        remaining_packets = []
        for b_idx, packets in buffer_visual_packets.items():
            remaining_packets.extend(packets)
        
        if remaining_packets:
            self.play(*[FadeOut(packet) for packet in remaining_packets], run_time=0.5)
        
        if dropped_count > 0:
            if new_buffer_added:
                stats_before = Text(
                    f"İlk 5 döngü: {dropped_before_upgrade} paket düşürüldü" if self.language == "tr" 
                    else f"First 5 cycles: {dropped_before_upgrade} packets dropped",
                    font_size=22,
                    color=ORANGE,
                    weight=BOLD
                )
                stats_after = Text(
                    f"Son 5 döngü: {dropped_count - dropped_before_upgrade} paket düşürüldü" if self.language == "tr"
                    else f"Last 5 cycles: {dropped_count - dropped_before_upgrade} packets dropped",
                    font_size=22,
                    color=GREEN,
                    weight=BOLD
                )
                improvement = Text(
                    f"Buffer eklenerek veri kaybı azaltıldı!" if self.language == "tr"
                    else f"Buffer addition reduced data loss!",
                    font_size=26,
                    color=YELLOW,
                    weight=BOLD
                )
                
                stats_group = VGroup(stats_before, stats_after, improvement).arrange(DOWN, buff=0.3)
                stats_group.move_to(ORIGIN)
                
                self.play(Write(stats_group), run_time=1.5)
                self.wait(2)
                self.play(FadeOut(stats_group))
            else:
                stats_text = Text(
                    f"{self.texts['dropped'].format(dropped_count)} packets",
                    font_size=24,
                    color=ORANGE,
                    weight=BOLD
                )
                stats_text.next_to(garbage_group, UP, buff=0.5)
                self.play(Write(stats_text))
                self.wait(1)
                self.play(FadeOut(stats_text))
        
        end_text = Text(
            self.texts["end_text"],
            font_size=36,
            color=GOLD,
            weight=BOLD
        )
        end_text.to_edge(DOWN, buff=0.5)
        
        for node_group in [producer_nodes, buffer_nodes, consumer_nodes]:
            for node in node_group:
                self.play(node.animate.scale(1.2).set_stroke(GOLD, width=3), run_time=0.1)
                self.play(node.animate.scale(1/1.2).set_stroke(node.color, width=1), run_time=0.1)
        
        self.play(Write(end_text))
        self.wait(2)


class NeuralProducerConsumer(NeuralProducerConsumerBase):
    """Neural Producer-Consumer animation for video rendering"""
    
    def __init__(self, language="tr", **kwargs):
        super().__init__(language=language, **kwargs)