# Advent of Code 2025

## Requirements

- Python 3.x

### Optional (but highly recommended)

- Bash (for running `init-day.sh`)
- virtualenv (for keeping python dependencies contained)
- direnv (to automatically activate/deactivate virtualenv)

## Setup

```bash
# Install OS dependencies (in Arch Linux -- will vary by OS)
pacman -S --needed bash base-devel python python-virtualenv direnv evince

# Create virtual environment
virtualenv venv

# ensure you have something like this in .bashrc: `if command -v direnv > /dev/null; eval "$(direnv hook bash)"`

direnv allow .

# you may need to reload your shell now and cd back into this directory
# you should see output from 'direnv' when you enter the directory
# Test with `which pip`. It should say '/path/to/this/repo/venv/bin/pip'

pip install -r requirements.txt
```

