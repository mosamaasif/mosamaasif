"""
SVG generator for terminal-styled GitHub profile README.
Generates dark and light mode SVG files with Gruvbox theme.
"""

from lxml import etree
from pathlib import Path
from typing import Dict, Any, List, Tuple
import sys

from config import Config
from github_stats import GitHubStats
from ascii_converter import ColoredASCIIConverter, create_placeholder_ascii


class SVGGenerator:
    """Generate terminal-styled SVG with Gruvbox theme."""

    def __init__(self, mode: str = 'dark'):
        """
        Initialize SVG generator.

        Args:
            mode: 'dark' or 'light' theme mode
        """
        self.mode = mode
        self.colors = Config.get_colors(mode)
        self.palette = Config.get_palette(mode)

        # Dimensions
        self.width = Config.SVG_WIDTH
        self.height = Config.SVG_HEIGHT
        self.padding = Config.SVG_PADDING

        # Layout
        self.left_width = int(self.width * Config.LEFT_COLUMN_WIDTH)
        self.right_width = int(self.width * Config.RIGHT_COLUMN_WIDTH)

    def create_svg_base(self) -> etree.Element:
        """Create base SVG element with styling."""
        svg = etree.Element(
            'svg',
            width=str(self.width),
            height=str(self.height),
            xmlns='http://www.w3.org/2000/svg'
        )

        # Add CSS styling
        style = etree.SubElement(svg, 'style')
        style.text = f"""
            .terminal {{
                font-family: {Config.FONT_FAMILY};
                font-size: {Config.FONT_SIZE}px;
            }}
            .header {{
                fill: {self.colors['yellow']};
                font-weight: bold;
            }}
            .label {{
                fill: {self.colors['gray']};
            }}
            .value {{
                fill: {self.colors['blue']};
            }}
            .stat {{
                fill: {self.colors['green']};
                font-weight: bold;
            }}
            .tech {{
                fill: {self.colors['aqua']};
            }}
            .social {{
                fill: {self.colors['purple']};
            }}
            .divider {{
                fill: {self.colors['gray']};
            }}
        """

        # Background rectangle
        etree.SubElement(
            svg,
            'rect',
            width=str(self.width),
            height=str(self.height),
            rx=str(Config.SVG_BORDER_RADIUS),
            ry=str(Config.SVG_BORDER_RADIUS),
            fill=self.colors['bg']
        )

        return svg

    def add_text(
        self,
        parent: etree.Element,
        text: str,
        x: int,
        y: int,
        css_class: str = '',
        fill: str = None
    ) -> etree.Element:
        """Add text element to SVG."""
        attrs = {
            'x': str(x),
            'y': str(y),
            'class': f'terminal {css_class}' if css_class else 'terminal'
        }

        if fill:
            attrs['fill'] = fill

        text_elem = etree.SubElement(parent, 'text', **attrs)
        text_elem.text = text
        return text_elem

    def generate_system_info(
        self,
        parent: etree.Element,
        stats: Dict[str, Any],
        x: int,
        y: int
    ) -> int:
        """
        Generate system information section.

        Args:
            parent: Parent SVG element
            stats: GitHub statistics dictionary
            x: X position
            y: Y position

        Returns:
            Final Y position after rendering
        """
        line_height = Config.LINE_HEIGHT_INFO
        current_y = y

        # Header
        self.add_text(parent, f"{Config.GITHUB_USERNAME}@github", x, current_y, 'header')
        current_y += line_height

        # Divider
        divider = "─" * 40
        self.add_text(parent, divider, x, current_y, 'divider')
        current_y += line_height * 1.5

        # Personal Information
        self.add_text(parent, "Name", x, current_y, 'label')
        self.add_text(parent, f": {Config.PERSONAL_NAME}", x + 120, current_y, 'value')
        current_y += line_height

        self.add_text(parent, "Role", x, current_y, 'label')
        self.add_text(parent, f": {Config.PERSONAL_ROLE}", x + 120, current_y, 'value')
        current_y += line_height

        self.add_text(parent, "Location", x, current_y, 'label')
        self.add_text(parent, f": {Config.PERSONAL_LOCATION}", x + 120, current_y, 'value')
        current_y += line_height

        # Wrap bio text if too long
        self.add_text(parent, "Bio", x, current_y, 'label')

        bio_text = Config.PERSONAL_BIO
        max_line_length = 45
        bio_lines = []

        # Split bio into wrapped lines
        words = bio_text.split()
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 <= max_line_length:
                current_line += (word + " ")
            else:
                if current_line:
                    bio_lines.append(current_line.rstrip())
                current_line = word + " "
        if current_line:
            bio_lines.append(current_line.rstrip())

        # Render first line with ": " prefix
        if bio_lines:
            self.add_text(parent, f": {bio_lines[0]}", x + 120, current_y, 'value')
            current_y += line_height

            # Render remaining lines without prefix
            for bio_line in bio_lines[1:]:
                self.add_text(parent, bio_line, x + 120, current_y, 'value')
                current_y += line_height

        current_y += line_height * 0.5  # Small spacing after bio

        # GitHub Statistics
        self.add_text(parent, "GitHub Stats", x, current_y, 'header')
        current_y += line_height

        self.add_text(parent, "Repositories", x, current_y, 'label')
        self.add_text(parent, f": {stats['repositories']}", x + 120, current_y, 'stat')
        current_y += line_height

        self.add_text(parent, "Stars", x, current_y, 'label')
        self.add_text(parent, f": {stats['total_stars']}", x + 120, current_y, 'stat')
        current_y += line_height

        self.add_text(parent, "Commits", x, current_y, 'label')
        self.add_text(
            parent,
            f": {GitHubStats(Config.GITHUB_USERNAME, Config.GITHUB_TOKEN).format_number(stats['total_commits'])}",
            x + 120,
            current_y,
            'stat'
        )
        current_y += line_height

        self.add_text(parent, "Contributions", x, current_y, 'label')
        self.add_text(
            parent,
            f": {GitHubStats(Config.GITHUB_USERNAME, Config.GITHUB_TOKEN).format_number(stats['total_contributions'])}",
            x + 120,
            current_y,
            'stat'
        )
        current_y += line_height

        self.add_text(parent, "Followers", x, current_y, 'label')
        self.add_text(parent, f": {stats['followers']}", x + 120, current_y, 'stat')
        current_y += line_height * 1.5

        # Tech Stack
        self.add_text(parent, "Tech Stack", x, current_y, 'header')
        current_y += line_height

        self.add_text(parent, "Languages", x, current_y, 'label')
        languages = ", ".join(Config.TECH_LANGUAGES[:4])
        self.add_text(parent, f": {languages}", x + 120, current_y, 'tech')
        current_y += line_height

        self.add_text(parent, "Frameworks", x, current_y, 'label')
        frameworks = ", ".join(Config.TECH_FRAMEWORKS[:3])
        self.add_text(parent, f": {frameworks}", x + 120, current_y, 'tech')
        current_y += line_height

        self.add_text(parent, "Tools", x, current_y, 'label')
        tools = ", ".join(Config.TECH_TOOLS[:4])
        self.add_text(parent, f": {tools}", x + 120, current_y, 'tech')
        current_y += line_height

        self.add_text(parent, "Databases", x, current_y, 'label')
        databases = ", ".join(Config.TECH_DATABASES[:3])
        self.add_text(parent, f": {databases}", x + 120, current_y, 'tech')
        current_y += line_height * 1.5

        # Connect
        self.add_text(parent, "Connect", x, current_y, 'header')
        current_y += line_height

        # Extract social handles (handle trailing slashes)
        linkedin_handle = 'N/A'
        if Config.SOCIAL_LINKEDIN:
            # Remove trailing slash and extract username
            parts = [p for p in Config.SOCIAL_LINKEDIN.rstrip('/').split('/') if p]
            linkedin_handle = parts[-1] if parts else 'N/A'

        twitter_handle = None
        if hasattr(Config, 'SOCIAL_TWITTER') and Config.SOCIAL_TWITTER:
            parts = [p for p in Config.SOCIAL_TWITTER.rstrip('/').split('/') if p]
            twitter_handle = parts[-1].replace('@', '') if parts else None

        self.add_text(parent, "Email", x, current_y, 'label')
        self.add_text(parent, f": {Config.SOCIAL_EMAIL}", x + 120, current_y, 'social')
        current_y += line_height

        self.add_text(parent, "LinkedIn", x, current_y, 'label')
        self.add_text(parent, f": {linkedin_handle}", x + 120, current_y, 'social')
        current_y += line_height

        # Only show Twitter if it's configured
        if twitter_handle:
            self.add_text(parent, "Twitter", x, current_y, 'label')
            self.add_text(parent, f": @{twitter_handle}", x + 120, current_y, 'social')
            current_y += line_height

        return current_y

    def generate_ascii_art(
        self,
        parent: etree.Element,
        ascii_data: List[Tuple[str, str]],
        x: int,
        y: int
    ) -> int:
        """
        Generate colored ASCII art section.

        Args:
            parent: Parent SVG element
            ascii_data: List of (character, color) tuples
            x: X position
            y: Y position

        Returns:
            Final Y position after rendering
        """
        line_height = Config.LINE_HEIGHT_ASCII
        current_x = x
        current_y = y

        # Character width in pixels (approximate for monospace)
        char_width = Config.FONT_SIZE * 0.6

        for char, color in ascii_data:
            if char == '\n':
                current_y += line_height
                current_x = x
            elif char == ' ':
                current_x += char_width
            else:
                # Use provided color or default foreground
                fill_color = color if color else self.colors['fg']
                self.add_text(parent, char, int(current_x), int(current_y), fill=fill_color)
                current_x += char_width

        return current_y

    def generate_svg(self, stats: Dict[str, Any], ascii_data: List[Tuple[str, str]]) -> etree.Element:
        """
        Generate complete SVG with all sections.

        Args:
            stats: GitHub statistics dictionary
            ascii_data: ASCII art data

        Returns:
            Complete SVG element
        """
        svg = self.create_svg_base()

        # Create main group with padding
        main_group = etree.SubElement(
            svg,
            'g',
            transform=f'translate({self.padding}, {self.padding})'
        )

        # Generate left column (system info)
        left_x = 10
        left_y = 30
        self.generate_system_info(main_group, stats, left_x, left_y)

        # Calculate ASCII art height and center it vertically
        ascii_rows = sum(1 for char, _ in ascii_data if char == '\n')
        # Height is the span from first to last row (rows - 1 intervals)
        ascii_height = (ascii_rows - 1) * Config.LINE_HEIGHT_ASCII if ascii_rows > 0 else 0

        # Calculate center position (padding already applied via transform)
        available_height = self.height - (2 * self.padding)
        right_y = (available_height - ascii_height) / 2

        # Generate right column (ASCII art) - centered with proper spacing
        right_x = self.left_width + 20
        self.generate_ascii_art(main_group, ascii_data, right_x, right_y)

        return svg

    def save_svg(self, svg: etree.Element, output_path: Path):
        """Save SVG to file."""
        tree = etree.ElementTree(svg)
        tree.write(
            str(output_path),
            pretty_print=True,
            xml_declaration=True,
            encoding='utf-8'
        )
        print(f"✓ Generated {self.mode} mode SVG: {output_path}")


def main():
    """Main execution function."""
    print("🎨 Generating terminal-styled GitHub profile README...")

    # Initialize GitHub stats fetcher
    print(f"\n📊 Fetching GitHub statistics for {Config.GITHUB_USERNAME}...")
    try:
        stats_fetcher = GitHubStats(Config.GITHUB_USERNAME, Config.GITHUB_TOKEN)
        stats = stats_fetcher.fetch_user_stats()
        print(f"✓ Fetched stats: {stats['repositories']} repos, {stats['total_stars']} stars")
    except Exception as e:
        print(f"✗ Error fetching GitHub stats: {e}")
        print("Using placeholder data...")
        stats = {
            'name': Config.PERSONAL_NAME,
            'repositories': 0,
            'total_stars': 0,
            'total_commits': 0,
            'total_contributions': 0,
            'followers': 0,
            'following': 0,
        }

    # Generate ASCII art
    print(f"\n🖼️  Converting portrait to ASCII art...")
    assets_dir = Path(__file__).parent.parent / 'assets'
    assets_dir.mkdir(exist_ok=True)

    # Dark mode
    print("\n🌙 Generating dark mode...")
    dark_converter = ColoredASCIIConverter(Config.DARK_PALETTE)

    try:
        dark_ascii = dark_converter.convert_image(str(Config.PORTRAIT_PATH), Config.ASCII_WIDTH)
        print(f"✓ Converted portrait to {len(dark_ascii)} characters")
    except FileNotFoundError:
        print("⚠️  Portrait not found, using placeholder")
        dark_ascii = create_placeholder_ascii(50, 30, Config.DARK_COLORS['yellow'])

    dark_generator = SVGGenerator('dark')
    dark_svg = dark_generator.generate_svg(stats, dark_ascii)
    dark_generator.save_svg(dark_svg, assets_dir / 'dark_mode.svg')

    print("\n✨ Generation complete!")
    print(f"📁 SVG file saved to: {assets_dir}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Generation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
