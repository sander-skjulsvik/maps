def extract_int(s: str) -> int:
    """
    Lopping over a string and extracts all chars where char.isdigit() is true
    """
    return int("".join(digit for digit in s if digit.isdigit()))
