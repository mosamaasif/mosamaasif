"""
Colored ASCII art converter using Gruvbox color palette.
Converts images to ASCII art with colors mapped to Gruvbox theme.
"""

from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from typing import List, Tuple


class ColoredASCIIConverter:
    """Convert images to colored ASCII art using Gruvbox palette."""

    # ASCII characters from dark to light (simplified for cleaner output)
    ASCII_CHARS = " .:;+=*#@$"

    def __init__(self, color_palette: List[str]):
        """
        Initialize converter with color palette.

        Args:
            color_palette: List of hex color codes for Gruvbox theme
        """
        self.color_palette = color_palette
        self.rgb_palette = [self._hex_to_rgb(color) for color in color_palette]

    @staticmethod
    def _hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def _rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
        """Convert RGB tuple to hex color."""
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

    def _color_distance(self, color1: Tuple[int, int, int], color2: Tuple[int, int, int]) -> float:
        """Calculate Euclidean distance between two RGB colors."""
        return np.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2)))

    def _find_nearest_color(self, rgb: Tuple[int, int, int]) -> str:
        """Find nearest Gruvbox color to given RGB value."""
        distances = [self._color_distance(rgb, palette_rgb) for palette_rgb in self.rgb_palette]
        nearest_idx = np.argmin(distances)
        return self.color_palette[nearest_idx]

    def _pixel_to_ascii(self, pixel_value: int) -> str:
        """Convert pixel brightness to ASCII character."""
        # Normalize pixel value to ASCII character index
        char_idx = int(pixel_value / 256 * len(self.ASCII_CHARS))
        char_idx = min(char_idx, len(self.ASCII_CHARS) - 1)
        return self.ASCII_CHARS[char_idx]

    def convert_image(self, image_path: str, width: int) -> List[Tuple[str, str]]:
        """
        Convert image to colored ASCII art.

        Args:
            image_path: Path to image file
            width: Width of ASCII art in characters

        Returns:
            List of (character, color_hex) tuples
        """
        try:
            # Load and process image
            img = Image.open(image_path)

            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Enhance image for better ASCII art
            # 1. Increase contrast
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.5)  # Increase contrast by 50%

            # 2. Sharpen the image
            img = img.filter(ImageFilter.SHARPEN)

            # 3. Increase brightness slightly
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.1)  # Increase brightness by 10%

            # Calculate height maintaining aspect ratio
            aspect_ratio = img.height / img.width
            # ASCII characters are taller than wide, so adjust aspect ratio
            height = int(width * aspect_ratio * 0.55)

            # Resize image
            img = img.resize((width, height), Image.Resampling.LANCZOS)

            # Convert to numpy array
            img_array = np.array(img)

            # Generate ASCII art with colors
            ascii_art = []

            for row in img_array:
                for pixel_rgb in row:
                    # Convert to tuple
                    rgb = tuple(pixel_rgb)

                    # Calculate grayscale value for character selection
                    gray = int(0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2])

                    # Get ASCII character
                    char = self._pixel_to_ascii(gray)

                    # Find nearest Gruvbox color
                    color = self._find_nearest_color(rgb)

                    ascii_art.append((char, color))

                # Add newline at end of row
                ascii_art.append(('\n', None))

            return ascii_art

        except FileNotFoundError:
            raise FileNotFoundError(f"Image file not found: {image_path}")
        except Exception as e:
            raise Exception(f"Failed to convert image: {e}")

    def convert_image_simple(self, image_path: str, width: int) -> str:
        """
        Convert image to simple ASCII art (no colors).

        Args:
            image_path: Path to image file
            width: Width of ASCII art in characters

        Returns:
            ASCII art as string
        """
        ascii_art = self.convert_image(image_path, width)
        return ''.join(char for char, _ in ascii_art)


def create_placeholder_ascii(width: int, height: int, color: str) -> List[Tuple[str, str]]:
    """
    Create a placeholder ASCII art pattern.

    Args:
        width: Width in characters
        height: Height in characters
        color: Hex color for the pattern

    Returns:
        List of (character, color_hex) tuples
    """
    ascii_art = []
    chars = "/@#*+"

    for row in range(height):
        for col in range(width):
            # Create a pattern
            char_idx = (row + col) % len(chars)
            ascii_art.append((chars[char_idx], color))
        ascii_art.append(('\n', None))

    return ascii_art


if __name__ == "__main__":
    # Test the module
    from config import Config

    converter = ColoredASCIIConverter(Config.DARK_PALETTE)

    try:
        ascii_art = converter.convert_image(str(Config.PORTRAIT_PATH), Config.ASCII_WIDTH)
        print(f"Generated ASCII art with {len(ascii_art)} characters")

        # Print first few lines
        current_line = ""
        line_count = 0
        for char, color in ascii_art[:200]:
            if char == '\n':
                print(current_line)
                current_line = ""
                line_count += 1
                if line_count >= 5:
                    break
            else:
                current_line += char

    except FileNotFoundError:
        print("Portrait image not found. Creating placeholder...")
        placeholder = create_placeholder_ascii(50, 30, Config.DARK_COLORS['yellow'])
        print(f"Created placeholder with {len(placeholder)} characters")
