"""
Create a simple placeholder portrait image.
Run this script to generate a placeholder if you don't have a portrait yet.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_portrait(output_path: str, size: int = 800):
    """Create a simple placeholder portrait."""

    # Create image with Gruvbox background
    bg_color = (40, 40, 40)  # Gruvbox dark bg
    img = Image.new('RGB', (size, size), bg_color)
    draw = ImageDraw.Draw(img)

    # Draw a simple avatar-like shape
    center = size // 2

    # Outer circle (head)
    head_radius = size // 3
    draw.ellipse(
        [center - head_radius, center - head_radius - 50,
         center + head_radius, center + head_radius - 50],
        fill=(235, 219, 178),  # Gruvbox fg
        outline=(251, 189, 47),  # Gruvbox yellow
        width=5
    )

    # Eyes
    eye_y = center - 70
    eye_spacing = 60
    eye_size = 20

    # Left eye
    draw.ellipse(
        [center - eye_spacing - eye_size, eye_y - eye_size,
         center - eye_spacing + eye_size, eye_y + eye_size],
        fill=(69, 133, 136)  # Gruvbox blue
    )

    # Right eye
    draw.ellipse(
        [center + eye_spacing - eye_size, eye_y - eye_size,
         center + eye_spacing + eye_size, eye_y + eye_size],
        fill=(69, 133, 136)  # Gruvbox blue
    )

    # Smile
    mouth_y = center - 10
    draw.arc(
        [center - 80, mouth_y - 40,
         center + 80, mouth_y + 40],
        start=0, end=180,
        fill=(251, 73, 52),  # Gruvbox red
        width=5
    )

    # Body (shoulders)
    draw.arc(
        [center - head_radius - 50, center + head_radius - 100,
         center + head_radius + 50, center + head_radius + 150],
        start=180, end=0,
        fill=(142, 192, 124),  # Gruvbox aqua
        width=8
    )

    # Add text
    try:
        # Try to use a nice font
        font_size = 40
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()

    text = "PLACEHOLDER"

    # Get text size for centering (use textbbox instead of textsize)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = (size - text_width) // 2
    text_y = size - 100

    # Draw text with outline
    outline_color = (40, 40, 40)  # Dark outline
    text_color = (250, 189, 47)  # Gruvbox yellow

    # Draw outline
    for offset_x in [-2, 0, 2]:
        for offset_y in [-2, 0, 2]:
            draw.text((text_x + offset_x, text_y + offset_y), text,
                     font=font, fill=outline_color)

    # Draw text
    draw.text((text_x, text_y), text, font=font, fill=text_color)

    # Save
    img.save(output_path)
    print(f"✓ Created placeholder portrait: {output_path}")


if __name__ == "__main__":
    output_path = "assets/portrait.png"

    # Create assets directory if it doesn't exist
    os.makedirs("assets", exist_ok=True)

    # Check if portrait already exists
    if os.path.exists(output_path):
        response = input(f"⚠️  {output_path} already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Cancelled.")
            exit(0)

    create_placeholder_portrait(output_path)
    print("\n💡 Replace this placeholder with your own portrait for better results!")
