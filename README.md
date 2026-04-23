# SecurePass-Gen 🛡️

A lightweight, cryptographically secure Command Line Interface (CLI) random password generator built with Python.

## Features
- **Secure Randomness**: Uses Python's `secrets` module, which provides access to the most secure source of randomness that your operating system provides.
- **Customizable**: Choose password length and toggle uppercase, digits, and symbols.
- **Simple Syntax**: Clean CLI interface for quick generation.

## How It Works
Modern password generation requires high-entropy randomness to prevent brute-force attacks. This tool avoids the standard `random` module (which is pseudo-random and predictable) and instead utilizes `secrets.choice()` to ensure each character is selected with cryptographic strength.

### Password Logic
1. **Character Pools**: The script constructs a pool of characters based on user input (Lowercase, Uppercase, Numbers, Special Symbols).
2. **Entropy Selection**: It draws characters from the pool using the OS-level CSPRNG (Cryptographically Secure Pseudo-Random Number Generator).
3. **Validation**: Ensures the length meets user requirements.

## Usage

### Basic Generation (16 characters, all types)
```bash
python passgen.py
```

### Custom Length
```bash
python passgen.py --length 24
```

### Exclude Specific Sets
```bash
# Generate a password without symbols
python passgen.py --no-symbols

# Generate only lowercase and numbers
python passgen.py --no-upper --no-symbols
```

## Options
| Flag | Short | Description | Default |
|------|-------|-------------|---------|
| `--length` | `-l` | Length of password | 16 |
| `--no-upper`| `-u` | Exclude uppercase | Included |
| `--no-digits`| `-d` | Exclude numbers | Included |
| `--no-symbols`| `-s` | Exclude special characters | Included |

## Requirements
- Python 3.6+
