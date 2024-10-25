# SeedML

A machine learning project template with a clean, modular structure.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/seedml.git
cd seedml

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Project Structure

```
seedml/
├── data/           # Dataset storage
├── models/         # Trained models
├── notebooks/      # Jupyter notebooks
├── src/           # Source code
│   ├── data/      # Data processing scripts
│   ├── models/    # Model implementations
│   └── utils/     # Utility functions
└── tests/         # Unit tests
```

## Development

- Use `black` for code formatting
- Run tests with `pytest`
- Follow PEP 8 style guidelines

## License

MIT License
