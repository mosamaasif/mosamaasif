# Setup Guide for Terminal-Styled GitHub Profile

This guide will walk you through setting up your terminal-styled GitHub profile README.

## Step 1: Create GitHub Personal Access Token

1. Go to GitHub Settings: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Profile README Generator")
4. Select the following scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:user` (Read user profile data)
   - ✅ `read:org` (Read org and team membership)
5. Click "Generate token"
6. **Important**: Copy the token immediately (you won't be able to see it again)

## Step 2: Configure Your Profile

1. Open `CONFIG.yaml` in a text editor
2. Replace the placeholder values with your information:

```yaml
github:
  username: YOUR_GITHUB_USERNAME
  token: YOUR_PERSONAL_ACCESS_TOKEN  # Paste the token from Step 1

personal:
  name: Your Full Name
  role: Your Role/Title
  location: Your Location
  bio: A brief bio about yourself

tech_stack:
  languages:
    - Python
    - JavaScript
    # Add your languages
  frameworks:
    - React
    - Node.js
    # Add your frameworks
  tools:
    - Git
    - Docker
    # Add your tools
  databases:
    - PostgreSQL
    - MongoDB
    # Add your databases

social:
  email: your.email@example.com
  linkedin: https://linkedin.com/in/yourprofile
  twitter: https://twitter.com/yourhandle
  website: https://yourwebsite.com
```

3. Save the file

⚠️ **Security Note**: `CONFIG.yaml` is gitignored by default to keep your token safe. Never commit this file to GitHub!

## Step 3: Add Your Portrait

1. Choose a portrait image (headshot, avatar, logo, etc.)
2. Save it as `assets/portrait.png`
3. Recommended specifications:
   - Format: PNG or JPG
   - Size: 500x500 to 1000x1000 pixels
   - Clear, high-contrast image works best for ASCII conversion
   - Face/subject should be centered and well-lit

## Step 4: Install Dependencies

```bash
# Make sure you have Python 3.11+ installed
python --version

# Install required packages
pip install -r requirements.txt
```

## Step 5: Test Locally

```bash
# Generate SVG files
cd scripts
python generate_svg.py
```

This will:
1. Fetch your GitHub statistics
2. Convert your portrait to colored ASCII art
3. Generate `assets/dark_mode.svg` and `assets/light_mode.svg`

Open the SVG files in a web browser to preview them.

## Step 6: Push to GitHub

1. Create a new repository on GitHub named after your username (e.g., `username/username`)
2. Initialize and push:

```bash
git init
git add .
git commit -m "feat: Add terminal-styled profile README"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_USERNAME.git
git push -u origin main
```

## Step 7: Set Up GitHub Actions

### Option A: Use GITHUB_TOKEN (Recommended for testing)

The workflow will use the automatic `GITHUB_TOKEN` provided by GitHub Actions. This works but has lower rate limits.

### Option B: Use Personal Access Token (Recommended for production)

1. Go to your repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `GH_TOKEN`
4. Value: Paste your Personal Access Token from Step 1
5. Click "Add secret"

Then update `.github/workflows/update_readme.yml` to use it:

```yaml
- name: Generate SVG files
  env:
    GH_TOKEN: ${{ secrets.GH_TOKEN }}
  run: |
    cd scripts
    python generate_svg.py
```

## Step 8: Enable GitHub Actions

1. Go to your repository on GitHub
2. Click the "Actions" tab
3. If prompted, click "I understand my workflows, go ahead and enable them"
4. You should see the "Update GitHub Profile README" workflow

## Step 9: Test the Workflow

1. Go to Actions tab
2. Click "Update GitHub Profile README"
3. Click "Run workflow" → "Run workflow"
4. Wait for the workflow to complete (should take 30-60 seconds)
5. Check the repository - you should see a new commit from github-actions bot

## Step 10: Verify the Profile

1. Go to your profile: https://github.com/YOUR_USERNAME
2. You should see the terminal-styled README
3. Try switching your system between dark and light mode to see both themes

---

## Customization Ideas

### Change ASCII Art Width

In `CONFIG.yaml`:
```yaml
ascii:
  width: 60  # Increase for more detail, decrease for faster generation
```

### Adjust SVG Dimensions

In `scripts/config.py`:
```python
SVG_WIDTH = 1200  # Make wider
SVG_HEIGHT = 600  # Make taller
```

### Modify Update Schedule

In `.github/workflows/update_readme.yml`:
```yaml
schedule:
  - cron: '0 */12 * * *'  # Run every 12 hours instead of daily
```

### Change Color Scheme

While this project uses Gruvbox, you can modify colors in `scripts/config.py`:
```python
DARK_COLORS = {
    'bg': '#1e1e1e',  # Your background
    'fg': '#d4d4d4',  # Your foreground
    # ... modify other colors
}
```

---

## Troubleshooting

### "CONFIG.yaml not found" error

Make sure you're running the script from the correct directory and CONFIG.yaml exists in the project root.

### GitHub API errors

- Verify your token has correct scopes
- Check if token is expired
- Ensure token is set in CONFIG.yaml or as GH_TOKEN environment variable

### Portrait not converting properly

- Try a different image with better contrast
- Adjust the ASCII_WIDTH (try 40, 50, 60, 70)
- Ensure image is in supported format (PNG, JPG)

### Workflow fails with permission error

- Go to Settings → Actions → General
- Under "Workflow permissions", select "Read and write permissions"
- Save changes and re-run workflow

### SVG looks broken

- Validate SVG syntax using an online validator
- Check for special characters that need escaping
- Ensure file is valid UTF-8 encoded

---

## Support

If you encounter issues:

1. Check the [Troubleshooting section in README.md](README.md#troubleshooting)
2. Review workflow logs in the Actions tab
3. Look for similar issues in the original inspiration project

---

## Next Steps

- ⭐ Star the repository if you find it useful
- 🍴 Fork it to create your own version
- 🐛 Report bugs or suggest features
- 📢 Share your terminal-styled profile!

Happy coding! 🚀
