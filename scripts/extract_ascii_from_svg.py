"""
One-time script to extract ASCII art data from an existing SVG file.
Parses right-column <text> elements and saves as JSON for reuse.
"""

import json
from lxml import etree
from pathlib import Path


def extract_ascii_art(svg_path: str, x_threshold: int = 560) -> list:
    """
    Extract ASCII art characters from SVG text elements.
    Reconstructs spaces from x-position gaps.
    Returns list of [char, color] pairs with ["\n", null] as row separators.
    """
    tree = etree.parse(svg_path)
    root = tree.getroot()

    # Collect all right-column text elements with fill (ASCII art)
    elements = []
    for text_el in root.iter('{http://www.w3.org/2000/svg}text'):
        x = float(text_el.get('x', '0'))
        y = float(text_el.get('y', '0'))
        fill = text_el.get('fill')
        char = text_el.text or ''

        if x >= x_threshold and fill:
            elements.append((x, y, char, fill))

    if not elements:
        print("No ASCII art elements found!")
        return []

    # Sort by y then x
    elements.sort(key=lambda e: (e[1], e[0]))

    # Determine char_width from consistent spacing (font_size * 0.6)
    # We'll detect it from the data: find minimum x gap between consecutive chars in a row
    char_width = 8.4  # 14 * 0.6 default

    # Group by y to get rows
    rows = {}
    for x, y, char, fill in elements:
        y_key = round(y, 1)
        if y_key not in rows:
            rows[y_key] = []
        rows[y_key].append((x, char, fill))

    # Find the minimum x for start position
    start_x = min(x for x, _, _, _ in elements)

    # Build ascii_data with spaces reconstructed
    ascii_data = []
    for y_key in sorted(rows.keys()):
        row_chars = sorted(rows[y_key], key=lambda e: e[0])

        current_x = start_x
        for x, char, fill in row_chars:
            # Insert spaces for gaps
            spaces = round((x - current_x) / char_width)
            for _ in range(spaces):
                ascii_data.append([" ", None])
            ascii_data.append([char, fill])
            current_x = x + char_width

        ascii_data.append(["\n", None])

    return ascii_data


def main():
    assets_dir = Path(__file__).parent.parent / 'assets'
    svg_path = assets_dir / 'dark_mode.svg'
    output_path = assets_dir / 'portrait_ascii.json'

    print(f"Extracting ASCII art from {svg_path}...")
    ascii_data = extract_ascii_art(str(svg_path))

    if not ascii_data:
        print("Failed to extract ASCII art.")
        return

    rows = sum(1 for c, _ in ascii_data if c == '\n')
    chars = sum(1 for c, _ in ascii_data if c not in ('\n', ' '))
    spaces = sum(1 for c, _ in ascii_data if c == ' ')
    print(f"Extracted {chars} visible chars, {spaces} spaces, {rows} rows")

    with open(output_path, 'w') as f:
        json.dump(ascii_data, f)

    print(f"Saved to {output_path}")
    print(f"File size: {output_path.stat().st_size / 1024:.1f} KB")


if __name__ == '__main__':
    main()
