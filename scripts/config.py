"""
Configuration module for GitHub profile README generator.
Loads settings from CONFIG.yaml and defines Gruvbox color schemes.
"""

import yaml
import os
from pathlib import Path


class Config:
    """Configuration loader and color scheme definitions."""

    # Load configuration from YAML
    _config_path = Path(__file__).parent.parent / "CONFIG.yaml"

    try:
        with open(_config_path, 'r') as f:
            _config = yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"CONFIG.yaml not found at {_config_path}. "
            "Please create it from the template."
        )

    # GitHub settings
    GITHUB_USERNAME = _config['github']['username']
    GITHUB_TOKEN = os.environ.get('GH_TOKEN', _config['github']['token'])

    # Personal information
    PERSONAL_NAME = _config['personal']['name']
    PERSONAL_ROLE = _config['personal']['role']
    PERSONAL_LOCATION = _config['personal']['location']
    PERSONAL_BIO = _config['personal']['bio']

    # Tech stack
    TECH_LANGUAGES = _config['tech_stack']['languages']
    TECH_FRAMEWORKS = _config['tech_stack']['frameworks']
    TECH_TOOLS = _config['tech_stack']['tools']
    TECH_DATABASES = _config['tech_stack']['databases']

    # Social links
    SOCIAL_EMAIL = _config['social']['email']
    SOCIAL_LINKEDIN = _config['social']['linkedin']
    #SOCIAL_TWITTER = _config['social']['twitter']
    SOCIAL_WEBSITE = _config['social']['website']

    # ASCII art settings
    ASCII_WIDTH = _config['ascii']['width']
    PORTRAIT_PATH = Path(__file__).parent.parent / _config['ascii']['portrait_path']

    # SVG dimensions
    SVG_WIDTH = 1000
    SVG_HEIGHT = 600
    SVG_BORDER_RADIUS = 15
    SVG_PADDING = 20

    # Font settings
    FONT_FAMILY = "Consolas, Monaco, 'Courier New', monospace"
    FONT_SIZE = 14
    LINE_HEIGHT_INFO = 22
    LINE_HEIGHT_ASCII = 16

    # Layout settings
    LEFT_COLUMN_WIDTH = 0.55  # 55% of width
    RIGHT_COLUMN_WIDTH = 0.45  # 45% of width

    # Gruvbox Dark color scheme
    DARK_COLORS = {
        'bg': '#282828',           # Dark background
        'fg': '#fbf1c7',           # Light foreground
        'bg0': '#282828',          # Background 0
        'bg1': '#3c3836',          # Background 1
        'bg2': '#504945',          # Background 2
        'bg3': '#665c54',          # Background 3
        'bg4': '#7c6f64',          # Background 4
        'fg0': '#fbf1c7',          # Foreground 0
        'fg1': '#ebdbb2',          # Foreground 1
        'fg2': '#d5c4a1',          # Foreground 2
        'fg3': '#bdae93',          # Foreground 3
        'fg4': '#a89984',          # Foreground 4
        'gray': '#928374',         # Gray
        'red': '#fb4934',          # Bright red
        'green': '#b8bb26',        # Bright green
        'yellow': '#fabd2f',       # Bright yellow
        'blue': '#83a598',         # Bright blue
        'purple': '#d3869b',       # Bright purple
        'aqua': '#8ec07c',         # Bright aqua
        'orange': '#fe8019',       # Bright orange
        'red_dim': '#cc241d',      # Dim red
        'green_dim': '#98971a',    # Dim green
        'yellow_dim': '#d79921',   # Dim yellow
        'blue_dim': '#458588',     # Dim blue
        'purple_dim': '#b16286',   # Dim purple
        'aqua_dim': '#689d6a',     # Dim aqua
        'orange_dim': '#d65d0e',   # Dim orange
    }

    # Gruvbox Light color scheme
    LIGHT_COLORS = {
        'bg': '#fbf1c7',           # Light background
        'fg': '#282828',           # Dark foreground
        'bg0': '#fbf1c7',          # Background 0
        'bg1': '#ebdbb2',          # Background 1
        'bg2': '#d5c4a1',          # Background 2
        'bg3': '#bdae93',          # Background 3
        'bg4': '#a89984',          # Background 4
        'fg0': '#282828',          # Foreground 0
        'fg1': '#3c3836',          # Foreground 1
        'fg2': '#504945',          # Foreground 2
        'fg3': '#665c54',          # Foreground 3
        'fg4': '#7c6f64',          # Foreground 4
        'gray': '#928374',         # Gray
        'red': '#cc241d',          # Red
        'green': '#98971a',        # Green
        'yellow': '#d79921',       # Yellow
        'blue': '#458588',         # Blue
        'purple': '#b16286',       # Purple
        'aqua': '#689d6a',         # Aqua
        'orange': '#d65d0e',       # Orange
        'red_bright': '#fb4934',   # Bright red
        'green_bright': '#b8bb26', # Bright green
        'yellow_bright': '#fabd2f',# Bright yellow
        'blue_bright': '#83a598',  # Bright blue
        'purple_bright': '#d3869b',# Bright purple
        'aqua_bright': '#8ec07c',  # Bright aqua
        'orange_bright': '#fe8019',# Bright orange
    }

    # Color palette for ASCII art (used for color mapping)
    # These are the colors that will be used in the ASCII art
    DARK_PALETTE = [
        '#fb4934',  # Red
        '#b8bb26',  # Green
        '#fabd2f',  # Yellow
        '#83a598',  # Blue
        '#d3869b',  # Purple
        '#8ec07c',  # Aqua
        '#fe8019',  # Orange
        '#fbf1c7',  # Foreground
        '#928374',  # Gray
        '#cc241d',  # Dim red
        '#98971a',  # Dim green
        '#d79921',  # Dim yellow
        '#458588',  # Dim blue
        '#b16286',  # Dim purple
        '#689d6a',  # Dim aqua
        '#d65d0e',  # Dim orange
    ]

    LIGHT_PALETTE = [
        '#cc241d',  # Red
        '#98971a',  # Green
        '#d79921',  # Yellow
        '#458588',  # Blue
        '#b16286',  # Purple
        '#689d6a',  # Aqua
        '#d65d0e',  # Orange
        '#282828',  # Foreground
        '#928374',  # Gray
        '#fb4934',  # Bright red
        '#b8bb26',  # Bright green
        '#fabd2f',  # Bright yellow
        '#83a598',  # Bright blue
        '#d3869b',  # Bright purple
        '#8ec07c',  # Bright aqua
        '#fe8019',  # Bright orange
    ]

    @classmethod
    def get_colors(cls, mode='dark'):
        """Get color scheme for specified mode."""
        if mode == 'dark':
            return cls.DARK_COLORS
        elif mode == 'light':
            return cls.LIGHT_COLORS
        else:
            raise ValueError(f"Invalid mode: {mode}. Must be 'dark' or 'light'.")

    @classmethod
    def get_palette(cls, mode='dark'):
        """Get color palette for ASCII art."""
        if mode == 'dark':
            return cls.DARK_PALETTE
        elif mode == 'light':
            return cls.LIGHT_PALETTE
        else:
            raise ValueError(f"Invalid mode: {mode}. Must be 'dark' or 'light'.")
