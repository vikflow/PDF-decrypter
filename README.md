# PDF Decrypter

A simple Python tool to remove password protection from PDF files using `pikepdf`.

## Prerequisites

- Python 3.x
- pikepdf library

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
```

2. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On Unix or MacOS:
```bash
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install pikepdf
```

## Usage

1. Place your password-protected PDF file in the same directory as `unlocker.py`

2. Run the script:
```bash
python unlocker.py
```

3. The unlocked PDF will be saved in the `temp` folder as `unlocked.pdf`

## Notes

- Make sure your PDF file is named correctly as referenced in the script
- The script will create a `temp` directory if it doesn't exist
- The unlocked PDF will be saved as `unlocked.pdf` in the `temp` directory

## License

MIT License

## Author

vikflow