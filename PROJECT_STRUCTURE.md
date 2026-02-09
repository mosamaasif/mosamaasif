# Project Structure

This document describes the organization and purpose of each file in this project.

## Directory Tree

```
mosamaasif/
├── README.md                       # Main profile README (shown on GitHub profile)
├── SETUP.md                        # Detailed setup instructions
├── CONTRIBUTING.md                 # Contribution guidelines
├── PROJECT_STRUCTURE.md            # This file - project organization
├── LICENSE                         # MIT License
├── requirements.txt                # Python dependencies
├── CONFIG.yaml                     # User configuration (gitignored)
├── CONFIG.yaml.example             # Example configuration template
├── .gitignore                      # Git ignore rules
├── quickstart.sh                   # Quick start setup script
├── create_placeholder.py           # Script to create placeholder portrait
│
├── assets/                         # Generated and static assets
│   ├── portrait.png                # User's portrait image (user-provided)
│   ├── dark_mode.svg               # Generated dark theme terminal (auto-updated)
│   └── light_mode.svg              # Generated light theme terminal (auto-updated)
│
├── scripts/                        # Python modules and scripts
│   ├── config.py                   # Configuration loader and color schemes
│   ├── github_stats.py             # GitHub API client and statistics fetcher
│   ├── ascii_converter.py          # Image to colored ASCII converter
│   ├── generate_svg.py             # Main SVG generator (orchestrator)
│   └── cache.json                  # API response cache (auto-generated)
│
└── .github/                        # GitHub-specific files
    └── workflows/                  # GitHub Actions workflows
        └── update_readme.yml       # Daily stats update automation
```

## File Descriptions

### Root Files

#### `README.md`
- **Purpose**: Main GitHub profile README displayed on your profile page
- **Content**: Terminal-styled SVG showcase, features, setup instructions, customization guide
- **Updates**: Manually edited, references auto-updated SVG files
- **User Action**: Customize the "About" sections as needed

#### `SETUP.md`
- **Purpose**: Step-by-step setup guide for new users
- **Content**: Detailed instructions from token creation to deployment
- **Updates**: Manually edited when setup process changes
- **User Action**: Follow this guide for initial setup

#### `CONTRIBUTING.md`
- **Purpose**: Guidelines for contributors
- **Content**: Code style, testing guidelines, PR process
- **Updates**: Manually edited when contribution process changes
- **User Action**: Read before contributing to the project

#### `LICENSE`
- **Purpose**: Software license (MIT License)
- **Content**: Copyright and usage terms
- **Updates**: Rarely changed
- **User Action**: Keep as-is or modify for your needs

#### `requirements.txt`
- **Purpose**: Python package dependencies
- **Content**: List of required packages with versions
- **Updates**: Manually edited when dependencies change
- **User Action**: Run `pip install -r requirements.txt` to install

#### `CONFIG.yaml`
- **Purpose**: User-specific configuration and secrets
- **Content**: GitHub credentials, personal info, tech stack, social links
- **Updates**: Manually edited by user
- **User Action**: Create from `CONFIG.yaml.example` and customize
- **Security**: Gitignored - never commit this file!

#### `CONFIG.yaml.example`
- **Purpose**: Template for creating CONFIG.yaml
- **Content**: Example configuration with placeholders
- **Updates**: Manually edited when new config options are added
- **User Action**: Copy to `CONFIG.yaml` and fill in your details

#### `.gitignore`
- **Purpose**: Specify files Git should ignore
- **Content**: Patterns for secrets, cache, and generated files
- **Updates**: Manually edited when new ignore patterns needed
- **User Action**: Keep as-is, add custom patterns if needed

#### `quickstart.sh`
- **Purpose**: Automated setup and generation script
- **Content**: Bash script to check dependencies, install packages, generate SVGs
- **Updates**: Manually edited when setup process changes
- **User Action**: Run `./quickstart.sh` for quick setup

#### `create_placeholder.py`
- **Purpose**: Generate a placeholder portrait image
- **Content**: Python script using Pillow to create a simple avatar
- **Updates**: Manually edited to improve placeholder design
- **User Action**: Run once if you don't have a portrait yet

### Assets Directory

#### `assets/portrait.png`
- **Purpose**: Source portrait image for ASCII art conversion
- **Content**: User's photo, avatar, or logo (PNG or JPG)
- **Updates**: Manually replaced by user
- **User Action**: Add your own portrait (500x500 to 1000x1000 pixels recommended)
- **Requirement**: Required for ASCII art generation

#### `assets/dark_mode.svg`
- **Purpose**: Dark theme terminal-styled profile display
- **Content**: Auto-generated SVG with Gruvbox dark colors
- **Updates**: Auto-updated by GitHub Actions or manual script run
- **User Action**: Reference in README.md, don't edit manually
- **Version Control**: Commit to repository

#### `assets/light_mode.svg`
- **Purpose**: Light theme terminal-styled profile display
- **Content**: Auto-generated SVG with Gruvbox light colors
- **Updates**: Auto-updated by GitHub Actions or manual script run
- **User Action**: Reference in README.md, don't edit manually
- **Version Control**: Commit to repository

### Scripts Directory

#### `scripts/config.py`
- **Purpose**: Configuration management and color scheme definitions
- **Content**:
  - `Config` class that loads settings from CONFIG.yaml
  - Gruvbox dark and light color palettes
  - SVG dimension and font constants
  - Layout settings
- **Updates**: Manually edited to modify colors or add new settings
- **User Action**: Customize colors or dimensions if needed
- **Dependencies**: PyYAML

#### `scripts/github_stats.py`
- **Purpose**: Fetch GitHub statistics via GraphQL API
- **Content**:
  - `GitHubStats` class for API communication
  - GraphQL queries for user data, repositories, contributions
  - Caching mechanism for lines of code calculations
  - Number formatting utilities
- **Updates**: Manually edited to fetch additional stats
- **User Action**: Generally don't need to modify
- **Dependencies**: requests, json
- **Rate Limiting**: Uses cache to minimize API calls

#### `scripts/ascii_converter.py`
- **Purpose**: Convert images to colored ASCII art
- **Content**:
  - `ColoredASCIIConverter` class
  - Image processing and resizing logic
  - ASCII character mapping (brightness to character)
  - Color distance calculation (RGB to nearest Gruvbox color)
  - Helper functions for placeholder generation
- **Updates**: Manually edited to improve conversion algorithm
- **User Action**: Adjust ASCII_CHARS for different styles
- **Dependencies**: Pillow, numpy

#### `scripts/generate_svg.py`
- **Purpose**: Main orchestrator for SVG generation
- **Content**:
  - `SVGGenerator` class for dark/light modes
  - SVG DOM construction using lxml
  - Two-column layout rendering
  - System information section generation
  - Colored ASCII art rendering
  - Main execution flow
- **Updates**: Manually edited to modify layout or add features
- **User Action**: This is the main file you run to generate SVGs
- **Dependencies**: lxml, config, github_stats, ascii_converter
- **Execution**: `python scripts/generate_svg.py`

#### `scripts/cache.json`
- **Purpose**: Cache for API responses (especially lines of code)
- **Content**: JSON dictionary with cached data and timestamps
- **Updates**: Auto-generated and updated by scripts
- **User Action**: Don't edit manually, delete to clear cache
- **Version Control**: Commit to preserve cache between runs
- **Cache Key**: Includes username and date for daily refresh

### GitHub Directory

#### `.github/workflows/update_readme.yml`
- **Purpose**: GitHub Actions workflow for automatic updates
- **Content**:
  - Workflow triggers (schedule, manual, push)
  - Job steps (checkout, Python setup, dependency install, script run)
  - Git configuration and commit logic
  - Change detection to avoid empty commits
- **Updates**: Manually edited to change schedule or workflow
- **User Action**: Customize cron schedule or add steps
- **Schedule**: Runs daily at 4:00 AM UTC by default
- **Secrets**: Uses GITHUB_TOKEN (or GH_TOKEN if configured)

## File Relationships

### Data Flow

```
CONFIG.yaml
    ↓
config.py (loads configuration)
    ↓
github_stats.py (fetches data from GitHub API)
    ↓
ascii_converter.py (processes portrait image)
    ↓
generate_svg.py (orchestrates and generates SVGs)
    ↓
assets/dark_mode.svg, assets/light_mode.svg
    ↓
README.md (displays SVGs)
```

### Update Flow

```
GitHub Actions Workflow (scheduled)
    ↓
Checkout repository
    ↓
Run generate_svg.py
    ↓
Check for changes
    ↓
Commit and push (if changes detected)
    ↓
Updated profile visible on GitHub
```

## Key Design Patterns

### Separation of Concerns
- **Configuration**: `config.py` - centralized settings
- **Data Fetching**: `github_stats.py` - API communication
- **Image Processing**: `ascii_converter.py` - ASCII conversion
- **Rendering**: `generate_svg.py` - SVG generation

### Caching Strategy
- **Purpose**: Reduce API calls and avoid rate limiting
- **Implementation**: `cache.json` stores computed values
- **Key Format**: `{metric}_{username}_{date}`
- **Expiration**: Daily refresh (keyed by date)

### Color Management
- **Gruvbox Palette**: Defined in `config.py`
- **Two Modes**: Separate color dictionaries for dark/light
- **Color Mapping**: Euclidean distance in RGB space
- **Consistency**: Same palette used across all components

### Error Handling
- **Graceful Degradation**: Falls back to placeholder when portrait missing
- **API Errors**: Uses cached data or placeholder values
- **User Feedback**: Clear error messages and troubleshooting hints

## Customization Points

### Easy Customizations (CONFIG.yaml)
- Personal information
- Tech stack lists
- Social links
- ASCII art width

### Moderate Customizations (config.py)
- Color schemes (while keeping Gruvbox aesthetic)
- SVG dimensions
- Font settings
- Layout proportions

### Advanced Customizations (generate_svg.py)
- Section layout and positioning
- New information sections
- Animation effects
- Additional visualizations

## Version Control Strategy

### Commit Files
- All `.py` scripts
- `requirements.txt`
- Documentation (`.md` files)
- `CONFIG.yaml.example`
- Generated SVG files in `assets/`
- Workflow files in `.github/`
- `cache.json` (for persistence)

### Ignore Files
- `CONFIG.yaml` (contains secrets)
- `__pycache__/` (Python bytecode)
- `.DS_Store` (macOS metadata)
- `venv/` (virtual environment)

## Testing Checklist

When making changes, test:
- [ ] Configuration loads correctly
- [ ] GitHub API calls succeed
- [ ] Portrait converts to ASCII
- [ ] SVGs generate without errors
- [ ] Dark mode looks correct
- [ ] Light mode looks correct
- [ ] Colors match Gruvbox palette
- [ ] Text is readable and aligned
- [ ] Workflow runs successfully

## Maintenance Tasks

### Regular Maintenance
- Update dependencies in `requirements.txt`
- Refresh GitHub API token when expired
- Update personal information in `CONFIG.yaml`
- Add new skills to tech stack

### Occasional Maintenance
- Update portrait image for fresh look
- Adjust colors if Gruvbox palette changes
- Optimize performance (caching, API calls)
- Add new features or sections

### Emergency Maintenance
- Fix API breaking changes
- Address rate limiting issues
- Resolve workflow failures
- Debug rendering problems

---

For questions about specific files or components, refer to the inline documentation in each file's docstrings and comments.
