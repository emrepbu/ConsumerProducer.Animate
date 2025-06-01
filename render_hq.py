#!/usr/bin/env python3.10
"""
High quality rendering script for Producer-Consumer animation
"""

import os
import sys

os.environ['DISABLE_MANIM_PLUGINS'] = '1'

from manim import *

if __name__ == "__main__":
    from producer_consumer_animation import ProducerConsumer
    
    config.quality = "high_quality"
    config.frame_rate = 60
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.preview = True
    config.write_to_movie = True
    
    language = "tr"
    
    scene = ProducerConsumer(language=language)
    scene.render()
    
    print(f"\nRendering complete!")
    print(f"Video saved to: {config.output_file}")
    print(f"Resolution: {config.pixel_width}x{config.pixel_height} @ {config.frame_rate}fps")