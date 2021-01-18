def extract_int(s) -> int:
    return int("".join(digit for digit in s if digit.isdigit()))
