# Hi there! 👋

![Terminal-styled profile with gruvbox theme](assets/dark_mode.svg)

---

## About This Profile

This terminal-styled profile is automatically updated daily with my latest GitHub statistics using GitHub Actions.

- **Theme**: Gruvbox Dark
- **Tech Stack**: Python, SVG, lxml, GitHub Actions
- **Inspiration**: [Andrew6rant](https://github.com/Andrew6rant/Andrew6rant)

### Features

✨ **Automatic Updates**: GitHub Actions runs daily to fetch and update statistics
🎨 **Dual Theme**: Automatically switches between dark and light mode based on system preferences
🖼️ **Colored ASCII Art**: Portrait rendered in ASCII with Gruvbox color palette
📊 **Live Stats**: Real-time repository, star, commit, and contribution counts
🛠️ **Tech Stack**: Displays languages, frameworks, tools, and databases
🔗 **Social Links**: Easy access to connect via email, LinkedIn, and Twitter

---

## Setup Instructions

Want to create your own terminal-styled profile? Follow these steps:

### 1. Prerequisites

- GitHub account
- GitHub Personal Access Token with `repo`, `read:user`, and `read:org` scopes
- A portrait image (PNG or JPG)

### 2. Repository Setup

1. Create a repository named after your GitHub username (e.g., `username/username`)
2. Clone this repository structure
3. Add your portrait image to `assets/portrait.png`

### 3. Configuration

1. Copy `CONFIG.yaml` and fill in your information:
   - GitHub username and token
   - Personal details (name, role, location, bio)
   - Tech stack (languages, frameworks, tools, databases)
   - Social links (email, LinkedIn, Twitter, website)

2. Update ASCII art settings if needed (width, portrait path)

### 4. Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Generate SVG files
cd scripts
python generate_svg.py
```

Check the generated files in `assets/dark_mode.svg` and `assets/light_mode.svg`.

### 5. GitHub Actions

1. Go to repository Settings → Secrets and variables → Actions
2. Add repository secret `GH_TOKEN` with your Personal Access Token
3. Enable GitHub Actions in repository settings
4. The workflow will run automatically daily at 4:00 AM UTC

### 6. Manual Update

To trigger an update manually:
- Go to Actions tab in your repository
- Select "Update GitHub Profile README" workflow
- Click "Run workflow"

---

## Customization

### Colors

Modify the Gruvbox color schemes in `scripts/config.py`:
- `DARK_COLORS`: Dark theme palette
- `LIGHT_COLORS`: Light theme palette

### Layout

Adjust dimensions and spacing in `scripts/config.py`:
- `SVG_WIDTH` and `SVG_HEIGHT`: Overall size
- `LEFT_COLUMN_WIDTH`: System info column width (0.0 - 1.0)
- `LINE_HEIGHT_INFO`: Spacing for text
- `LINE_HEIGHT_ASCII`: Spacing for ASCII art

### ASCII Art

Change ASCII art appearance:
- `ASCII_WIDTH`: Width in characters (default: 50)
- `ASCII_CHARS`: Character set for brightness mapping
- Replace `assets/portrait.png` with your own image

### Update Frequency

Modify the cron schedule in `.github/workflows/update_readme.yml`:
```yaml
schedule:
  - cron: '0 4 * * *'  # Daily at 4:00 AM UTC
```

---

## Troubleshooting

### SVG not displaying

- Ensure files are in `assets/` directory
- Check file names match: `dark_mode.svg` and `light_mode.svg`
- Verify SVG files are valid XML

### GitHub API rate limiting

- Use Personal Access Token (5,000 requests/hour)
- Reduce update frequency
- Check cache in `scripts/cache.json`

### Colors don't look right

- Verify hex codes in `config.py` against [official Gruvbox palette](https://github.com/morhetz/gruvbox)
- Test in incognito mode (browser extensions can affect colors)
- Check system color profile settings

### Workflow not running

- Verify GitHub Actions is enabled in repository settings
- Check workflow permissions (Settings → Actions → General → Workflow permissions)
- Ensure `GITHUB_TOKEN` secret exists
- Review workflow logs in Actions tab

---

## Technologies Used

- **Python**: Core logic and orchestration
- **lxml**: SVG generation and manipulation
- **Pillow**: Image processing for ASCII art
- **NumPy**: Color calculations and array operations
- **Requests**: GitHub GraphQL API client
- **PyYAML**: Configuration file parsing
- **GitHub Actions**: Automation and scheduling

---

## Credits

- **Gruvbox Theme**: [morhetz/gruvbox](https://github.com/morhetz/gruvbox)
- **Inspiration**: [Andrew6rant](https://github.com/Andrew6rant/Andrew6rant)
- **ASCII Art**: Pillow image processing library

---

## License

This project is open source and available under the MIT License.

---

*Last updated: Automatically via GitHub Actions*

<div align="center">
  <sub>Built with ❤️ using Claude Code</sub>
</div>
