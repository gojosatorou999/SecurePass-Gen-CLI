import argparse
import secrets
import string
import sys

def generate_password(length, use_uppercase, use_digits, use_symbols):
    """Generates a secure random password."""
    # Base characters: lowercase is always included
    chars = string.ascii_lowercase
    
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    # Ensure we have characters to pick from
    if not chars:
        return ""

    # Generate password using secrets (cryptographically strong)
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Secure CLI Password Generator")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    parser.add_argument("-u", "--no-upper", action="store_false", dest="upper", help="Exclude uppercase letters")
    parser.add_argument("-d", "--no-digits", action="store_false", dest="digits", help="Exclude digits")
    parser.add_argument("-s", "--no-symbols", action="store_false", dest="symbols", help="Exclude symbols")
    
    # Set default values for selections
    parser.set_defaults(upper=True, digits=True, symbols=True)
    
    args = parser.parse_args()

    if args.length < 1:
        print("Error: Length must be at least 1.")
        sys.exit(1)

    password = generate_password(args.length, args.upper, args.digits, args.symbols)
    
    print("-" * 30)
    print(f"Generated Password: {password}")
    print("-" * 30)

if __name__ == "__main__":
    main()
