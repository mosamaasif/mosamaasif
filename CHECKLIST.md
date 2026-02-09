# Getting Started Checklist

Follow this checklist to get your terminal-styled GitHub profile up and running.

## Pre-Deployment Checklist

### 1. Prerequisites ✅
- [ ] Python 3.11+ installed (`python3 --version`)
- [ ] Git installed (`git --version`)
- [ ] GitHub account created
- [ ] Text editor ready (VS Code, vim, etc.)

### 2. GitHub Setup 🔑
- [ ] Create GitHub Personal Access Token
  - Go to: https://github.com/settings/tokens
  - Click "Generate new token (classic)"
  - Select scopes: `repo`, `read:user`, `read:org`
  - Copy token (save it securely!)
- [ ] Create repository named `USERNAME/USERNAME` (replace with your username)
  - Go to: https://github.com/new
  - Repository name: YOUR_GITHUB_USERNAME
  - Make it public
  - Don't initialize with README (we already have one)

### 3. Configuration 📝
- [ ] Edit `CONFIG.yaml`:
  - [ ] Replace `YOUR_GITHUB_USERNAME` with your username
  - [ ] Replace `YOUR_GITHUB_PERSONAL_ACCESS_TOKEN` with token from step 2
  - [ ] Update `name` with your full name
  - [ ] Update `role` with your title/role
  - [ ] Update `location` with your location
  - [ ] Update `bio` with your bio
  - [ ] Update `languages` list with your languages
  - [ ] Update `frameworks` list with your frameworks
  - [ ] Update `tools` list with your tools
  - [ ] Update `databases` list with your databases
  - [ ] Update `email` with your email
  - [ ] Update `linkedin` URL
  - [ ] Update `twitter` URL
  - [ ] Update `website` URL

### 4. Portrait Image 🖼️
Choose one option:
- [ ] **Option A**: Use placeholder
  ```bash
  python3 create_placeholder.py
  ```
- [ ] **Option B**: Add your own photo
  ```bash
  cp /path/to/your/photo.png assets/portrait.png
  ```
  - Recommended size: 500x500 to 1000x1000 pixels
  - Use high-contrast, centered image

### 5. Local Testing 🧪
- [ ] Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- [ ] Generate SVG files:
  ```bash
  cd scripts
  python3 generate_svg.py
  cd ..
  ```
  - Or use: `./quickstart.sh`
- [ ] Verify files created:
  - [ ] `assets/dark_mode.svg` exists
  - [ ] `assets/light_mode.svg` exists
- [ ] Open SVG files in browser to preview:
  - [ ] Dark mode looks good
  - [ ] Light mode looks good
  - [ ] Text is readable
  - [ ] ASCII art is recognizable
  - [ ] Colors match Gruvbox theme

### 6. Git Setup 📦
- [ ] Initialize git (if not already done):
  ```bash
  git init
  ```
- [ ] Add files:
  ```bash
  git add .
  ```
- [ ] Check that `CONFIG.yaml` is NOT staged (it's in .gitignore):
  ```bash
  git status | grep CONFIG.yaml
  # Should show nothing (file is ignored)
  ```
- [ ] Commit:
  ```bash
  git commit -m "feat: Add terminal-styled profile with Gruvbox theme"
  ```
- [ ] Add remote (replace USERNAME):
  ```bash
  git branch -M main
  git remote add origin https://github.com/USERNAME/USERNAME.git
  ```
- [ ] Push:
  ```bash
  git push -u origin main
  ```

### 7. GitHub Actions Setup ⚙️
- [ ] Go to repository settings:
  - URL: `https://github.com/USERNAME/USERNAME/settings`
- [ ] Configure secrets:
  - [ ] Click "Secrets and variables" → "Actions"
  - [ ] Click "New repository secret"
  - [ ] Name: `GH_TOKEN`
  - [ ] Value: Your Personal Access Token
  - [ ] Click "Add secret"
- [ ] Configure permissions:
  - [ ] Click "Actions" → "General"
  - [ ] Under "Workflow permissions"
  - [ ] Select "Read and write permissions"
  - [ ] Click "Save"
- [ ] Enable Actions:
  - [ ] Go to "Actions" tab
  - [ ] If prompted, click "I understand my workflows, go ahead and enable them"

### 8. First Workflow Run 🚀
- [ ] Trigger workflow manually:
  - [ ] Go to "Actions" tab
  - [ ] Click "Update GitHub Profile README"
  - [ ] Click "Run workflow" → "Run workflow"
- [ ] Wait for completion (30-60 seconds)
- [ ] Check workflow result:
  - [ ] Workflow completed successfully (green checkmark)
  - [ ] New commit created by github-actions bot
  - [ ] SVG files updated in repository
  - [ ] No errors in workflow logs

### 9. Verification ✅
- [ ] Check your profile:
  - URL: `https://github.com/USERNAME`
- [ ] Verify terminal display:
  - [ ] Terminal-styled SVG is visible
  - [ ] Your information is displayed correctly
  - [ ] ASCII art portrait is showing
  - [ ] Stats are populated with real data
- [ ] Test theme switching:
  - [ ] Switch OS to dark mode → see dark theme
  - [ ] Switch OS to light mode → see light theme
  - [ ] Both themes look good

## Post-Deployment Checklist

### Immediate Tasks
- [ ] Star your repository ⭐
- [ ] Pin repository to profile (optional)
- [ ] Share profile with friends
- [ ] Update bio/status if needed

### Regular Maintenance
- [ ] Check workflow runs weekly
- [ ] Update tech stack when learning new skills
- [ ] Replace portrait if desired
- [ ] Monitor API rate limits
- [ ] Update dependencies periodically

### Optional Enhancements
- [ ] Customize colors in `scripts/config.py`
- [ ] Adjust SVG dimensions
- [ ] Change ASCII art width
- [ ] Modify update schedule
- [ ] Add custom sections

## Troubleshooting Checklist

If something goes wrong, check these:

### Configuration Issues
- [ ] `CONFIG.yaml` exists in project root
- [ ] Token is valid and not expired
- [ ] Token has correct scopes
- [ ] All required fields are filled

### Generation Issues
- [ ] Python 3.11+ is installed
- [ ] All dependencies are installed
- [ ] Portrait image exists and is valid format
- [ ] No syntax errors in Python files

### GitHub Issues
- [ ] Repository name matches username
- [ ] Repository is public (or profile is public)
- [ ] `GH_TOKEN` secret is set correctly
- [ ] Workflow permissions are set to read/write
- [ ] Actions are enabled in repository

### Display Issues
- [ ] SVG files are in `assets/` directory
- [ ] File names are exactly `dark_mode.svg` and `light_mode.svg`
- [ ] README.md references correct file paths
- [ ] SVG files are valid XML (check with validator)

### Workflow Issues
- [ ] `.github/workflows/update_readme.yml` exists
- [ ] Workflow file syntax is correct (YAML)
- [ ] No merge conflicts in workflow file
- [ ] Workflow has proper indentation

## Success Indicators

You know everything is working when:
- ✅ Terminal display shows on your profile
- ✅ Stats are populated with real numbers
- ✅ ASCII art portrait is visible
- ✅ Theme switching works automatically
- ✅ Workflow runs successfully
- ✅ Profile updates daily at 4:00 AM UTC
- ✅ No errors in Actions logs

## Getting Help

If you're stuck:
1. Check `QUICK_REFERENCE.md` for commands
2. Review `SETUP.md` for detailed steps
3. See `PROJECT_STRUCTURE.md` for file info
4. Read `TROUBLESHOOTING.md` (in README.md)
5. Check workflow logs in Actions tab
6. Open an issue on GitHub

## Time Estimate

Total setup time: **30-60 minutes**
- Configuration: 10-15 minutes
- Local testing: 5-10 minutes
- Git setup: 5-10 minutes
- GitHub Actions: 10-15 minutes
- Verification: 5-10 minutes

## Next Steps After Completion

1. **Customize Your Profile**
   - Experiment with colors
   - Try different portrait styles
   - Adjust layout and spacing

2. **Explore Advanced Features**
   - Add contribution graphs
   - Include language charts
   - Show recent activity

3. **Share Your Work**
   - Tweet your profile
   - Post on LinkedIn
   - Share in developer communities

4. **Contribute Back**
   - Report bugs you find
   - Suggest improvements
   - Submit pull requests

---

## Quick Start (TL;DR)

For experienced users:
```bash
# 1. Configure
cp CONFIG.yaml.example CONFIG.yaml
vim CONFIG.yaml  # Add token and personal info

# 2. Add portrait or create placeholder
python3 create_placeholder.py

# 3. Generate
./quickstart.sh

# 4. Push
git add .
git commit -m "feat: Add terminal-styled profile"
git branch -M main
git remote add origin https://github.com/USERNAME/USERNAME.git
git push -u origin main

# 5. Configure GitHub Actions
# - Add GH_TOKEN secret in repository settings
# - Enable read/write permissions for Actions
# - Run workflow manually from Actions tab
```

---

**Congratulations!** 🎉 Once you complete this checklist, you'll have an awesome terminal-styled GitHub profile that updates automatically!

Happy coding! 🚀
