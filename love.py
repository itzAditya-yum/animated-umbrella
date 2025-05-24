#!/usr/bin/env python3
"""
Love Message Generator - Creates a text file with 'i loveee youuu' in various stylish patterns
"""

import random
import os
from datetime import datetime

def heart_pattern(message, width=40):
    """Generate a heart shape using a message"""
    lines = []
    
    # Create the top of the heart
    for i in range(3):
        spaces = abs(i - 1)
        middle = width - 2 * (spaces + 2)
        line = '\u00A0' * spaces + message[:2] * (i + 1) + '\u00A0' * middle + message[:2] * (i + 1)
        lines.append(line[:width])
    
    # Create the body of the heart
    for i in range(width // 2 - 3):
        padded_message = message * (width // len(message) + 1)
        lines.append(padded_message[:width])
    
    # Create the bottom point of the heart
    for i in range(width // 2):
        spaces = i
        content_width = width - 2 * spaces
        if content_width <= 0:
            break
        padded_message = message * (content_width // len(message) + 1)
        lines.append('\u00A0' * spaces + padded_message[:content_width])
    
    return lines

def diagonal_pattern(message, height=10, width=40):
    """Generate a diagonal pattern using a message"""
    lines = []
    
    for i in range(height):
        spaces = i % (width - len(message))
        line = '\u00A0' * spaces + message + '\u00A0' * (width - spaces - len(message))
        lines.append(line[:width])
    
    return lines

def wave_pattern(message, height=10, width=50):
    """Generate a wave pattern using a message"""
    lines = []
    
    for i in range(height):
        pos = int((width - len(message)) * (0.5 + 0.5 * (i / height) * (-1 if i % 2 else 1)))
        pos = max(0, min(width - len(message), pos))
        line = '\u00A0' * pos + message + '\u00A0' * (width - pos - len(message))
        lines.append(line[:width])
    
    return lines

def random_case_message(message, count=20):
    """Generate the message with random case letters"""
    lines = []
    
    for _ in range(count):
        random_message = ''.join(
            c.upper() if random.choice([True, False]) else c.lower()
            for c in message
        )
        lines.append(random_message)
    
    return lines

def main():
    message = "i loveee youuu\u00A0"
    
    # Create a filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"love_message_{timestamp}.txt"
    
    # Generate all patterns
    patterns = []
    patterns.extend(["-" * 50])
    patterns.extend(["❤️ HEART PATTERN ❤️".center(50)])
    patterns.extend(["-" * 50])
    patterns.extend(heart_pattern(message))
    
    patterns.extend(["\n" + "-" * 50])
    patterns.extend(["✨ DIAGONAL PATTERN ✨".center(50)])
    patterns.extend(["-" * 50])
    patterns.extend(diagonal_pattern(message))
    
    patterns.extend(["\n" + "-" * 50])
    patterns.extend(["〰️ WAVE PATTERN 〰️".center(50)])
    patterns.extend(["-" * 50])
    patterns.extend(wave_pattern(message))
    
    patterns.extend(["\n" + "-" * 50])
    patterns.extend(["🔡 RANDOM CASE PATTERN 🔡".center(50)])
    patterns.extend(["-" * 50])
    patterns.extend(random_case_message(message))
    
    # Add a border to the top and bottom
    border = "♥" * 50
    full_content = [border + "\n"] + patterns + ["\n" + border]
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(full_content))
    
    print(f"Love message created in '{filename}'")
    
    # Display a preview
    print("\nPreview:")
    for i, line in enumerate(full_content):
        if i < 5 or i > len(full_content) - 5:
            print(line)
        elif i == 5:
            print("...")

if __name__ == "__main__":
    main()