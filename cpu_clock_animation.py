from manim import *
import numpy as np


class CPUClockBase:
    """Base class for CPU Clock animations with translation support"""
    
    def __init__(self):
        self.translations = {
            "en": {
                "title": "CPU Clock Signal",
                "intro_title": "How Does a CPU Clock Work?",
                "intro_text": "The heartbeat of every computer",
                "time_axis": "Time",
                "voltage_axis": "Voltage",
                "high": "HIGH (1)",
                "low": "LOW (0)",
                "period": "Clock Period",
                "frequency": "Frequency",
                "rising_edge": "Rising Edge",
                "falling_edge": "Falling Edge",
                "cycle": "Cycle",
                "clock_info": "Clock Information",
                "voltage_high": "3.3V",
                "voltage_low": "0V",
                "time_unit": "ns",
                "freq_unit": "GHz",
                "current_time": "Time",
                "current_voltage": "Voltage",
                "clock_speed": "Clock Speed",
                "modern_cpu": "Modern CPU",
                "cycles_per_second": "billion cycles/second",
                "binary_info": "Digital Signal: Only HIGH or LOW",
                "sync_info": "All components synchronized",
                "edge_trigger": "Operations triggered on edges",
                "cpu_operation": "CPU Operations",
                "fetch": "Fetch",
                "decode": "Decode", 
                "execute": "Execute",
                "clock_cycle": "Clock Cycle"
            },
            "tr": {
                "title": "CPU Saat Sinyali",
                "intro_title": "CPU Saati Nasıl Çalışır?",
                "intro_text": "Her bilgisayarın kalp atışı",
                "time_axis": "Zaman",
                "voltage_axis": "Voltaj",
                "high": "YÜKSEK (1)",
                "low": "DÜŞÜK (0)",
                "period": "Saat Periyodu",
                "frequency": "Frekans",
                "rising_edge": "Yükselen Kenar",
                "falling_edge": "Düşen Kenar",
                "cycle": "Döngü",
                "clock_info": "Saat Bilgisi",
                "voltage_high": "3.3V",
                "voltage_low": "0V",
                "time_unit": "ns",
                "freq_unit": "GHz",
                "current_time": "Zaman",
                "current_voltage": "Voltaj",
                "clock_speed": "Saat Hızı",
                "modern_cpu": "Modern İşlemci",
                "cycles_per_second": "milyar döngü/saniye",
                "binary_info": "Dijital Sinyal: Sadece YÜKSEK veya DÜŞÜK",
                "sync_info": "Tüm bileşenler senkronize",
                "edge_trigger": "İşlemler kenarlarda tetiklenir",
                "cpu_operation": "İşlemci İşlemleri",
                "fetch": "Getir",
                "decode": "Çöz",
                "execute": "Çalıştır",
                "clock_cycle": "Saat Döngüsü"
            }
        }
        
    def t(self, key):
        """Get translation for current language"""
        return self.translations[self.lang][key]


class CPUClock(CPUClockBase, MovingCameraScene):
    """CPU Clock animation with cinematic camera movements"""
    
    def __init__(self, language="en"):
        CPUClockBase.__init__(self)
        MovingCameraScene.__init__(self)
        self.lang = language
        
    def construct(self):
        self.intro_sequence()
        
        self.main_clock_demo()
        
    def intro_sequence(self):
        """Introduction with minimal camera movements"""
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-6, 6, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.2,
            }
        )
        
        title = Text(self.t("intro_title"), font_size=56, color=BLUE)
        title.set_stroke(BLUE_B, width=2)
        
        subtitle = Text(self.t("intro_text"), font_size=28, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.add(grid)
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)
        
        self.play(
            *[FadeOut(mob) for mob in [title, subtitle]],
            grid.animate.set_opacity(0.1),
            run_time=1.5
        )
        
    def main_clock_demo(self):
        """Main clock signal demonstration"""
        
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[-0.5, 4, 1],
            x_length=10,
            y_length=4,
            axis_config={
                "color": BLUE_B,
                "include_tip": True,
                "tip_length": 0.3,
                "include_numbers": True,
                "numbers_with_elongated_ticks": [0, 2, 4, 6, 8],
                "tick_size": 0.1,
            },
            x_axis_config={
                "numbers_to_include": np.arange(0, 9, 2),
                "font_size": 24,
            },
            y_axis_config={
                "numbers_to_include": [0, 3.3],
                "decimal_number_config": {"num_decimal_places": 1},
                "font_size": 24,
            }
        )
        
        time_icon = VGroup(
            Circle(radius=0.15, color=WHITE, stroke_width=2),
            Line(ORIGIN, UP * 0.1, color=WHITE, stroke_width=2),
            Line(ORIGIN, RIGHT * 0.12, color=WHITE, stroke_width=2).rotate(PI/3, about_point=ORIGIN)
        )
        time_icon.scale(1.5)
        
        voltage_icon = VGroup(
            Line(UP * 0.2, DOWN * 0.1 + LEFT * 0.05, color=YELLOW, stroke_width=3),
            Line(DOWN * 0.1 + LEFT * 0.05, DOWN * 0.1 + RIGHT * 0.05, color=YELLOW, stroke_width=3),
            Line(DOWN * 0.1 + RIGHT * 0.05, DOWN * 0.3, color=YELLOW, stroke_width=3),
        )
        voltage_icon.scale(1.2)
        
        x_label = VGroup(
            time_icon,
            Text(f"{self.t('time_axis')} ({self.t('time_unit')})", font_size=28)
        ).arrange(RIGHT, buff=0.3)
        x_label.next_to(axes.x_axis, DOWN, buff=0.5)
        
        y_label = VGroup(
            voltage_icon,
            Text(self.t("voltage_axis"), font_size=28)
        ).arrange(RIGHT, buff=0.3)
        y_label.rotate(PI/2)
        y_label.next_to(axes.y_axis, LEFT, buff=0.5)
        
        self.play(Create(axes), run_time=2)
        self.play(
            Write(x_label),
            Write(y_label)
        )
        
        clock_period = 2
        voltage_high = 3.3
        voltage_low = 0
        num_cycles = 4
        
        clock_path = self.create_clock_signal(axes, clock_period, voltage_high, voltage_low, num_cycles)
        
        self.play(
            Create(clock_path),
            run_time=3,
            rate_func=linear
        )
        
        self.add_voltage_indicators(axes, voltage_high, voltage_low)
        
        self.create_tracker_system(axes, clock_period, voltage_high, voltage_low, num_cycles)
        
        self.show_period_frequency(axes, clock_period)
        
        self.demonstrate_edges(axes, clock_period, voltage_high, voltage_low)
        
        self.wait(2)
        self.play(
            FadeOut(self.info_bg),
            FadeOut(self.time_display),
            FadeOut(self.voltage_display),
            FadeOut(self.tracker_dot),
            run_time=1
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )
        
    def create_clock_signal(self, axes, period, v_high, v_low, cycles):
        """Create a stylized clock signal with gradient effect"""
        points = []
        for cycle in range(cycles):
            t_start = cycle * period
            t_mid = t_start + period / 2
            t_end = t_start + period
            
            if cycle == 0:
                points.append(axes.c2p(t_start, v_low))
            
            rise_points = [
                axes.c2p(t_start, v_low),
                axes.c2p(t_start + 0.05, v_low + (v_high - v_low) * 0.5),
                axes.c2p(t_start + 0.1, v_high)
            ]
            points.extend(rise_points[1:])
            
            points.append(axes.c2p(t_mid - 0.1, v_high))
            
            fall_points = [
                axes.c2p(t_mid - 0.1, v_high),
                axes.c2p(t_mid - 0.05, v_high - (v_high - v_low) * 0.5),
                axes.c2p(t_mid, v_low)
            ]
            points.extend(fall_points[1:])
            
            points.append(axes.c2p(t_end, v_low))
        
        clock_signal = VMobject()
        clock_signal.set_points_as_corners(points)
        clock_signal.set_stroke(color=[YELLOW, ORANGE], width=4)
        clock_signal.set_sheen_direction(RIGHT)
        
        return clock_signal
        
    def add_voltage_indicators(self, axes, v_high, v_low):
        """Add animated voltage level indicators"""
        high_line = DashedLine(
            axes.c2p(0, v_high),
            axes.c2p(8, v_high),
            color=GREEN,
            stroke_width=2,
            dash_length=0.1
        )
        
        high_label = VGroup(
            Text("1", font_size=32, color=GREEN),
            Text(self.t("high"), font_size=20, color=GREEN)
        ).arrange(DOWN, buff=0.1)
        high_label.next_to(high_line, LEFT, buff=0.3)
        
        low_line = DashedLine(
            axes.c2p(0, v_low),
            axes.c2p(8, v_low),
            color=RED,
            stroke_width=2,
            dash_length=0.1
        )
        
        low_label = VGroup(
            Text("0", font_size=32, color=RED),
            Text(self.t("low"), font_size=20, color=RED)
        ).arrange(DOWN, buff=0.1)
        low_label.next_to(low_line, LEFT, buff=0.3)
        
        self.play(
            Create(high_line),
            Create(low_line),
            FadeIn(high_label, scale=0.8),
            FadeIn(low_label, scale=0.8)
        )
        
        self.play(
            high_label[0].animate.scale(1.2).set_color(YELLOW),
            low_label[0].animate.scale(1.2).set_color(ORANGE),
            rate_func=there_and_back,
            run_time=1
        )
        
    def create_tracker_system(self, axes, period, v_high, v_low, cycles):
        """Create an advanced tracking system with visual effects"""
        self.tracker_dot = Dot(radius=0.15, color=BLUE)
        self.tracker_dot.set_glow_factor(0.8)
        self.tracker_dot.move_to(axes.c2p(0, v_low))
        tracker_dot = self.tracker_dot
        
        trail = TracedPath(
            tracker_dot.get_center,
            stroke_color=[BLUE, PURPLE],
            stroke_width=2,
            stroke_opacity=[1, 0]
        )
        
        self.info_bg = RoundedRectangle(
            width=5,
            height=1.5,
            corner_radius=0.2,
            fill_color=BLACK,
            fill_opacity=0.9,
            stroke_color=BLUE,
            stroke_width=2
        ).to_corner(UR, buff=0.3)
        
        self.time_display = always_redraw(lambda: VGroup(
            Text(self.t('current_time') + ":", font_size=20, color=BLUE_B),
            Text(
                f"{(tracker_dot.get_x() - axes.c2p(0, 0)[0]) / (axes.c2p(1, 0)[0] - axes.c2p(0, 0)[0]):.2f} {self.t('time_unit')}",
                font_size=24,
                font="monospace",
                color=WHITE
            )
        ).arrange(RIGHT, buff=0.3).move_to(self.info_bg.get_center() + UP * 0.3))
        
        self.voltage_display = always_redraw(lambda: VGroup(
            Text(self.t('current_voltage') + ":", font_size=20, color=YELLOW),
            Text(
                f"{(tracker_dot.get_y() - axes.c2p(0, 0)[1]) * 3.3 / (axes.c2p(0, 3.3)[1] - axes.c2p(0, 0)[1]):.2f}V",
                font_size=24,
                font="monospace",
                color=WHITE
            )
        ).arrange(RIGHT, buff=0.3).move_to(self.info_bg.get_center() + DOWN * 0.3))
        
        self.play(
            FadeIn(self.info_bg),
            Create(tracker_dot),
            Write(self.time_display),
            Write(self.voltage_display)
        )
        self.add(trail)
        
        self.clock_time = 0
        
        def update_tracker(mob, dt):
            self.clock_time += dt
            t = self.clock_time * 2
            cycle = int(t / period) % cycles
            phase = (t % period) / period
            
            x = axes.c2p(t % (cycles * period), 0)[0]
            
            if phase < 0.05:
                progress = phase / 0.05
                y = axes.c2p(0, v_low + smooth(progress) * (v_high - v_low))[1]
            elif phase < 0.45:
                y = axes.c2p(0, v_high)[1]
            elif phase < 0.5:
                progress = (phase - 0.45) / 0.05
                y = axes.c2p(0, v_high - smooth(progress) * (v_high - v_low))[1]
            else:
                y = axes.c2p(0, v_low)[1]
            
            mob.move_to([x, y, 0])
        
        tracker_dot.add_updater(update_tracker)
        
        self.wait(6)
        tracker_dot.remove_updater(update_tracker)
        
        self.play(FadeOut(trail))
        
    def show_period_frequency(self, axes, period):
        """Show period and frequency with visual emphasis"""
        
        elements_to_hide = [self.info_bg, self.time_display, self.voltage_display, self.tracker_dot]
        self.play(
            *[mob.animate.set_opacity(0.2) for mob in elements_to_hide],
            run_time=0.5
        )
        
        period_line = Line(
            axes.c2p(0, -0.3),
            axes.c2p(period, -0.3),
            color=YELLOW,
            stroke_width=3
        )
        period_arrows = VGroup(
            Arrow(axes.c2p(0, -0.3), axes.c2p(0, -0.1), buff=0, color=YELLOW),
            Arrow(axes.c2p(period, -0.3), axes.c2p(period, -0.1), buff=0, color=YELLOW)
        )
        
        period_label = VGroup(
            Text(self.t('period'), font_size=24, color=YELLOW),
            Text(f"{period} {self.t('time_unit')}", font_size=32, color=WHITE)
        ).arrange(DOWN, buff=0.1)
        period_label.next_to(period_line, DOWN, buff=0.3)
        
        freq_formula = MathTex(
            f"f = \\frac{{1}}{{T}} = \\frac{{1}}{{{period}\\text{{ ns}}}} = {1000/period:.0f}\\text{{ MHz}}",
            font_size=28
        )
        freq_formula.next_to(period_label, DOWN, buff=0.5)
        
        self.play(
            Create(period_line),
            Create(period_arrows)
        )
        self.play(Write(period_label))
        self.play(Write(freq_formula))
        
        cpu_info = VGroup(
            Text(f"{self.t('modern_cpu')}: 3-5 {self.t('freq_unit')}", font_size=24),
            Text(f"= 3-5 {self.t('cycles_per_second')}", font_size=20, color=GRAY)
        ).arrange(DOWN, buff=0.1)
        cpu_info.next_to(freq_formula, DOWN, buff=0.5)
        
        self.play(FadeIn(cpu_info, shift=UP))
        self.wait(2)
        
        self.play(
            *[FadeOut(mob) for mob in [period_line, period_arrows, period_label, freq_formula, cpu_info]],
            run_time=1.5
        )
        
        self.play(
            *[mob.animate.set_opacity(1) for mob in elements_to_hide],
            run_time=0.5
        )
        
    def demonstrate_edges(self, axes, period, v_high, v_low):
        """Demonstrate rising and falling edges"""
        focus_rect = Rectangle(
            width=1.5,
            height=4.5,
            stroke_color=YELLOW,
            stroke_width=2,
            fill_opacity=0
        ).move_to(axes.c2p(0, v_high/2))
        
        self.play(Create(focus_rect))
        
        rising_arrow = Arrow(
            axes.c2p(0, v_low),
            axes.c2p(0, v_high),
            color=GREEN,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        rising_label = Text(self.t('rising_edge'), font_size=28, color=GREEN)
        rising_label.next_to(rising_arrow, RIGHT, buff=0.3)
        
        trigger_pulse = Circle(radius=0.3, color=GREEN)
        trigger_pulse.move_to(axes.c2p(0, v_high/2))
        
        self.play(GrowArrow(rising_arrow))
        self.play(Write(rising_label))
        self.play(
            Create(trigger_pulse),
            trigger_pulse.animate.scale(3).set_opacity(0),
            run_time=1
        )
        
        edge_info = Text(
            self.t('edge_trigger'),
            font_size=20,
            color=WHITE
        ).next_to(rising_label, DOWN, buff=0.3)
        
        self.play(FadeIn(edge_info))
        self.wait(2)
        
        self.play(
            *[FadeOut(mob) for mob in [rising_arrow, rising_label, edge_info, focus_rect]],
            run_time=1
        )
        
        focus_rect2 = Rectangle(
            width=1.5,
            height=4.5,
            stroke_color=YELLOW,
            stroke_width=2,
            fill_opacity=0
        ).move_to(axes.c2p(period/2, v_high/2))
        
        self.play(Create(focus_rect2))
        
        falling_arrow = Arrow(
            axes.c2p(period/2, v_high),
            axes.c2p(period/2, v_low),
            color=RED,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        falling_label = Text(self.t('falling_edge'), font_size=28, color=RED)
        falling_label.next_to(falling_arrow, RIGHT, buff=0.3)
        
        self.play(GrowArrow(falling_arrow))
        self.play(Write(falling_label))
        self.wait(2)
        
        self.play(
            *[FadeOut(mob) for mob in [falling_arrow, falling_label, focus_rect2]],
            run_time=1
        )
        


class CPUClockEN(CPUClock):
    """English version of CPU Clock animation"""
    def __init__(self):
        super().__init__(language="en")


class CPUClockTR(CPUClock):
    """Turkish version of CPU Clock animation"""
    def __init__(self):
        super().__init__(language="tr")