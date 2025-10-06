# Copilot Instructions for Kryptologie (Cryptography Education)

This is a JupyterLite-based cryptography education platform deployed as a static site to GitHub Pages. The project teaches cryptography concepts through interactive Jupyter notebooks in German.

## Project Architecture

### Content Structure
- `content/worksheets/` - Main educational notebooks (AB1-AB7 series + supplementary materials)
- `content/help/` - Progressive hint system with nested help files (help1_1a → help1_1aa → help1_1aaa)
- `content/code/` - Python utilities and validation functions
- `content/figs/` - Educational images and diagrams
- `content/printables/` - Downloadable materials

### Key Components

**Worksheet Pattern**: All main worksheets follow `AB{N}_{Topic}.ipynb` naming:
- AB1_Caesar.ipynb - Caesar cipher basics
- AB2_Hacker_Caesar.ipynb - Frequency analysis attacks
- AB3_Vigenere.ipynb - Vigenère cipher
- AB4-AB7 - RSA public key cryptography series

**Validation System**: `content/code/check.py` provides comprehensive validation functions:
- Answer checking (e.g., `caesar_code()`, `vigenere_code()`)
- Cryptographic utilities (RSA, modular arithmetic, prime testing)
- Interactive widgets for Jupyter environment

## Development Patterns

### Notebook Structure
Every worksheet starts with:
```python
import sys
sys.path.append("../code")  # Critical path setup
import check
from IPython.display import display, HTML
display(HTML('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">'))
```

### German Language Convention
- All content, variable names, and function names use German
- Educational feedback uses ✔ for correct, ❗ for incorrect answers
- Error messages written to `sys.stderr` for proper display

### Help System Pattern
Progressive hints with consistent naming: `help{worksheet}_{task}{subtask}.ipynb`
- Example: `help1_1a.ipynb` → `help1_1aa.ipynb` → `help1_1aaa.ipynb`
- Each help file links to the next level using relative paths

### Bootstrap Integration
All worksheets use Bootstrap 4.6.2 for styling with custom alert boxes:
```html
<div class="alert alert-info" style="background-color: #E0F2F7; border-color: #2E9AFE; color: #151515">
```

## JupyterLite Configuration

- **Deployment**: Static site via GitHub Pages using JupyterLite 0.6.4
- **Kernel**: Pyodide-based Python environment (no server required)
- **Content Directory**: `content/` mapped via `jupyter_lite_config.json`
- **Dependencies**: Managed through `requirements.txt` and `piplite/pyodide.json`

## Critical Development Notes

- Always use relative paths from notebook location (`../code`, `../figs`)
- Validation functions expect specific German text formats (case-insensitive)
- Images must be optimized for web delivery (referenced from `../figs/`)
- Interactive widgets work in JupyterLite but may have limitations vs. full Jupyter

When creating new content, follow the established AB{N}_{Topic} pattern and ensure all imports/paths align with the existing structure.