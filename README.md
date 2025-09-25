# PDF Password Remover and Decrypter

A powerful Python tool to remove password protection, unlock, and decrypt PDF files using `pikepdf`. This tool helps you remove passwords from protected PDF documents, unlock secured PDFs, and decrypt encrypted PDF files easily.

## Features

- Remove PDF passwords and security restrictions
- Unlock password-protected PDF files
- Decrypt secured PDF documents
- Simple and easy-to-use command-line interface
- Works with most PDF security methods
- Fast and efficient processing

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