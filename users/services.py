from random import choices
from string import ascii_letters, digits


def generate_invite_code() -> str:
    """
    Generates a random invite code of length 6.

    Returns:
        str: The generated invite code.
    """
    code = ''.join(
        choices(ascii_letters + digits, k=6))
    return code
