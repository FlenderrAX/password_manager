import secrets
import string

CHAR_NUMBER: int = 15

def gen_password(uppercase=True, lowercase=True, numbers=True, symbols=True) -> str:
    """
    Generate a secure password following international norms
    Password options :
    - 15 chars
    - Alphanumeric Characters
    """
    chars: list = []
    password_options = {
        'lowercase': (lowercase, string.ascii_lowercase),
        'uppercase': (uppercase, string.ascii_uppercase),
        'numbers': (numbers, string.digits),
        'symbols': (symbols, string.punctuation)
    }

    for option_name, (option_value, option_chars) in password_options.items():
        if option_value:
            chars.extend(option_chars)

    password: str = ""
    for _ in range(CHAR_NUMBER + 1):
        char_type: int = chars[secrets.randbelow(len(chars))]
        selected_char: str = char_type[secrets.randbelow(len(char_type))]
        password += selected_char

    return password