# Contributing Guide

Thank you for your interest in contributing to this terminal-styled GitHub profile project! 🎉

## How to Contribute

### Reporting Issues

If you encounter bugs or have feature requests:

1. Check if the issue already exists in the Issues tab
2. If not, create a new issue with:
   - Clear, descriptive title
   - Detailed description of the problem or feature
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Screenshots (if applicable)
   - Your environment (OS, Python version, etc.)

### Suggesting Enhancements

We welcome ideas for improvements! When suggesting enhancements:

1. Explain the use case and benefits
2. Provide examples or mockups if possible
3. Consider backward compatibility
4. Think about performance implications

### Code Contributions

#### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/mosamaasif/mosamaasif.git
cd mosamaasif

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create your CONFIG.yaml
cp CONFIG.yaml.example CONFIG.yaml
# Edit CONFIG.yaml with your details
```

#### Making Changes

1. **Fork the repository** on GitHub

2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**:
   - Follow existing code style
   - Add comments for complex logic
   - Keep functions focused and single-purpose
   - Use descriptive variable names

4. **Test your changes**:
   ```bash
   cd scripts
   python3 generate_svg.py
   ```
   - Verify SVG files are generated correctly
   - Check both dark and light modes
   - Test with different configurations

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: Add your feature description"
   ```

   Follow conventional commit format:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `style:` for code style changes
   - `refactor:` for code refactoring
   - `test:` for test additions
   - `chore:` for maintenance tasks

6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request** on GitHub:
   - Provide clear description of changes
   - Reference any related issues
   - Include screenshots for visual changes
   - Ensure CI checks pass

## Code Style Guidelines

### Python

- Follow PEP 8 style guide
- Use type hints where appropriate
- Maximum line length: 100 characters
- Use docstrings for classes and functions:

```python
def example_function(param: str) -> Dict[str, Any]:
    """
    Brief description of function.

    Args:
        param: Description of parameter

    Returns:
        Description of return value
    """
    pass
```

### File Organization

- Keep related functionality in the same module
- Use clear, descriptive file names
- Organize imports: stdlib, third-party, local
- Separate concerns (config, stats, rendering, etc.)

### Naming Conventions

- Classes: `PascalCase`
- Functions/methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private methods: `_leading_underscore`

## Testing Guidelines

Before submitting a PR, test:

1. **Functionality**:
   - SVG generation works correctly
   - GitHub API calls succeed
   - ASCII art conversion produces good output
   - Color mapping is accurate

2. **Edge Cases**:
   - Missing portrait image
   - Empty tech stack
   - API rate limiting
   - Invalid configuration

3. **Performance**:
   - Generation completes in reasonable time
   - No memory leaks
   - Efficient API usage

4. **Compatibility**:
   - Works on different Python versions (3.11+)
   - Cross-platform (Linux, macOS, Windows)
   - Various image formats

## Areas for Contribution

### Priority Areas

1. **Performance Optimization**:
   - Faster ASCII art generation
   - Better caching strategies
   - Reduced API calls

2. **New Features**:
   - Activity graphs/charts
   - Language statistics visualization
   - Recent activity timeline
   - Multiple portrait support
   - Animation effects

3. **Customization**:
   - More color schemes
   - Layout variations
   - Font options
   - Size presets

4. **Documentation**:
   - Video tutorials
   - More examples
   - Troubleshooting guides
   - API documentation

5. **Testing**:
   - Unit tests
   - Integration tests
   - Test fixtures
   - CI/CD improvements

### Good First Issues

Looking to contribute but not sure where to start? Try these:

- Add more ASCII character sets
- Improve error messages
- Add configuration validation
- Create example configurations
- Expand documentation
- Add command-line arguments
- Improve color contrast in light mode

## Review Process

1. **Automated Checks**: GitHub Actions will run basic checks
2. **Code Review**: Maintainers will review your code
3. **Feedback**: Address any requested changes
4. **Approval**: Once approved, your PR will be merged

## Getting Help

- 💬 Ask questions in issue discussions
- 📧 Contact maintainers directly
- 📖 Check existing documentation
- 🔍 Search closed issues and PRs

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information
- Unprofessional conduct

## Attribution

Contributors will be acknowledged in:
- GitHub contributors page
- Release notes (for significant contributions)
- Special thanks section (for exceptional contributions)

## Questions?

Don't hesitate to ask! We're here to help you contribute successfully.

---

Thank you for contributing to this project! Your efforts help make this tool better for everyone. 🚀
