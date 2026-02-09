# Quick Reference Guide

Fast reference for common tasks and commands.

## Setup

```bash
# Quick setup (automated)
./quickstart.sh

# Manual setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Generate SVG Files

```bash
# From project root
cd scripts && python3 generate_svg.py && cd ..

# Or with quickstart
./quickstart.sh
```

## Configuration

### Edit Personal Info
```bash
# Edit CONFIG.yaml (never commit this file!)
vim CONFIG.yaml
```

### Update Portrait
```bash
# Replace with your image
cp /path/to/your/photo.png assets/portrait.png

# Or create placeholder
python3 create_placeholder.py
```

## Common Customizations

### Change Update Schedule

Edit `.github/workflows/update_readme.yml`:
```yaml
schedule:
  - cron: '0 */6 * * *'  # Every 6 hours
  - cron: '0 0 * * 0'    # Weekly (Sunday midnight)
  - cron: '0 0 1 * *'    # Monthly (1st of month)
```

### Adjust ASCII Art Width

Edit `CONFIG.yaml`:
```yaml
ascii:
  width: 60  # Try 40-70
```

### Modify Colors

Edit `scripts/config.py`:
```python
DARK_COLORS = {
    'bg': '#282828',     # Background
    'fg': '#fbf1c7',     # Foreground
    'yellow': '#fabd2f', # Headers
    # ... modify as needed
}
```

### Change SVG Size

Edit `scripts/config.py`:
```python
SVG_WIDTH = 1200   # Wider
SVG_HEIGHT = 600   # Taller
```

## File Locations

```
CONFIG.yaml              → Your configuration (gitignored)
assets/portrait.png      → Your portrait image
assets/dark_mode.svg     → Generated dark theme (auto-updated)
assets/light_mode.svg    → Generated light theme (auto-updated)
scripts/cache.json       → API cache (auto-generated)
```

## Git Commands

```bash
# Initial commit
git add .
git commit -m "feat: Initial terminal-styled profile"
git branch -M main
git remote add origin https://github.com/USERNAME/USERNAME.git
git push -u origin main

# Update after changes
git add .
git commit -m "chore: Update profile information"
git push
```

## GitHub Actions

```bash
# Trigger manual update (via GitHub UI)
# Go to: Actions → Update GitHub Profile README → Run workflow

# Check workflow status
# Go to: Actions tab → View latest run
```

## Troubleshooting

### Quick Fixes

```bash
# Clear cache
rm scripts/cache.json

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Reset virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Check Python version (need 3.11+)
python3 --version
```

### Common Errors

**"CONFIG.yaml not found"**
```bash
cp CONFIG.yaml.example CONFIG.yaml
# Edit CONFIG.yaml with your details
```

**"Portrait image not found"**
```bash
python3 create_placeholder.py
# Or add your own: cp photo.png assets/portrait.png
```

**"GitHub API error"**
- Check token has correct scopes (repo, read:user, read:org)
- Verify token not expired
- Check rate limits: https://api.github.com/rate_limit

**"Workflow permission denied"**
- Settings → Actions → General
- Workflow permissions → Read and write permissions
- Save

## Environment Variables

For GitHub Actions, set these secrets:

```bash
# Repository Settings → Secrets → Actions → New secret

Name: GH_TOKEN
Value: [Your Personal Access Token]
```

For local development:

```bash
# Option 1: Use CONFIG.yaml (recommended)
# Already configured in config.py

# Option 2: Use environment variable
export GH_TOKEN="your_token_here"
cd scripts && python3 generate_svg.py
```

## Testing

```bash
# Test configuration loading
python3 -c "from scripts.config import Config; print(f'User: {Config.GITHUB_USERNAME}')"

# Test GitHub API (requires token)
python3 -c "from scripts.github_stats import GitHubStats; from scripts.config import Config; \
stats = GitHubStats(Config.GITHUB_USERNAME, Config.GITHUB_TOKEN); \
print(f'Repos: {stats.fetch_user_stats()[\"repositories\"]}')"

# Test ASCII conversion
python3 -c "from scripts.ascii_converter import ColoredASCIIConverter; from scripts.config import Config; \
converter = ColoredASCIIConverter(Config.DARK_PALETTE); \
art = converter.convert_image(str(Config.PORTRAIT_PATH), 50); \
print(f'Generated {len(art)} characters')"
```

## Useful Links

- **GitHub Token**: https://github.com/settings/tokens
- **Repository Settings**: https://github.com/USERNAME/USERNAME/settings
- **Actions Dashboard**: https://github.com/USERNAME/USERNAME/actions
- **Gruvbox Colors**: https://github.com/morhetz/gruvbox
- **GraphQL Explorer**: https://docs.github.com/en/graphql/overview/explorer

## Color Reference

### Gruvbox Dark
```
Background:  #282828
Foreground:  #fbf1c7
Red:         #fb4934
Green:       #b8bb26
Yellow:      #fabd2f
Blue:        #83a598
Purple:      #d3869b
Aqua:        #8ec07c
Orange:      #fe8019
Gray:        #928374
```

### Gruvbox Light
```
Background:  #fbf1c7
Foreground:  #282828
Red:         #cc241d
Green:       #98971a
Yellow:      #d79921
Blue:        #458588
Purple:      #b16286
Aqua:        #689d6a
Orange:      #d65d0e
Gray:        #928374
```

## Performance Tips

1. **Reduce API calls**: Use cache effectively
2. **Optimize portrait**: Use smaller image (500x500 sufficient)
3. **Adjust ASCII width**: Lower width = faster generation
4. **Limit repos**: Modify `github_stats.py` if you have 100+ repos
5. **Cache LOC**: Lines of code calculation is cached daily

## Keyboard Shortcuts (GitHub)

- `t` - File finder
- `l` - Jump to line
- `w` - Switch branch
- `y` - Expand URL to canonical form
- `.` - Open in github.dev editor

## Support Resources

- **Documentation**: Check `SETUP.md` for detailed setup
- **Contributing**: See `CONTRIBUTING.md` for guidelines
- **Issues**: Open an issue on GitHub
- **Structure**: See `PROJECT_STRUCTURE.md` for file details

---

**Pro Tip**: Bookmark this file for quick access to commands and configurations!
