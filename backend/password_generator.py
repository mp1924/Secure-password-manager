import logging
import secrets
import string

logger = logging.getLogger(__name__)


def generate_password(
    length: int,
    use_upper: bool,
    use_lower: bool,
    use_numbers: bool,
    use_symbols: bool,
) -> str:
    """
    Generate a cryptographically secure password.

    Ensures the generated password contains at least one character
    from each selected character category.
    """

    if length < 4:
        raise ValueError("Password length must be at least 4.")

    selected_sets = []

    if use_upper:
        selected_sets.append(string.ascii_uppercase)

    if use_lower:
        selected_sets.append(string.ascii_lowercase)

    if use_numbers:
        selected_sets.append(string.digits)

    if use_symbols:
        selected_sets.append(string.punctuation)

    if not selected_sets:
        raise ValueError("Select at least one character type.")

    if length < len(selected_sets):
        raise ValueError(
            "Password length is too short for the selected character types."
        )

    try:
        # Ensure at least one character from each selected set
        password = [
            secrets.choice(char_set)
            for char_set in selected_sets
        ]

        all_characters = "".join(selected_sets)

        password.extend(
            secrets.choice(all_characters)
            for _ in range(length - len(password))
        )

        secrets.SystemRandom().shuffle(password)

        return "".join(password)

    except Exception:
        logger.exception("Failed to generate password.")
        raise