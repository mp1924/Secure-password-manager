import string


def check_strength(password: str) -> str:
    """
    Evaluate the strength of a password.

    Returns:
        "Weak", "Medium", or "Strong"
    """

    if not password:
        return "Weak"

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"

    if score <= 4:
        return "Medium"

    return "Strong"