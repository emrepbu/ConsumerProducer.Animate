#!/usr/bin/env python3.10
"""
High quality rendering script for Producer-Consumer animation
"""

import os
import sys

# Disable plugin loading if needed
os.environ['DISABLE_MANIM_PLUGINS'] = '1'

# Import manim after setting environment variable
from manim import *

# Run the scene
if __name__ == "__main__":
    # Import the scene class
    from producer_consumer_animation import ProducerConsumer
    
    # Configure for high quality rendering (1080p60)
    config.quality = "high_quality"
    config.frame_rate = 60
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.preview = True
    config.write_to_movie = True
    
    # Set language (default is "tr" for Turkish, can be "en" for English)
    language = "tr"  # Change to "en" for English version
    
    # Create and render the scene
    scene = ProducerConsumer(language=language)
    scene.render()
    
    print(f"\nRendering complete!")
    print(f"Video saved to: {config.output_file}")
    print(f"Resolution: {config.pixel_width}x{config.pixel_height} @ {config.frame_rate}fps")