from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def hash_password(password: str) -> str:
    """
    Hashes a password using Argon2.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    return ph.hash(password)

def verify_password(hashed_password: str, password: str) -> bool:
    """
    Verifies a password against its hash using Argon2.

    Args:
        hashed_password (str): The hashed password.
        password (str): The password to verify.

    Returns:
        bool: True if the password is correct, False otherwise.
    """
    try:
        ph.verify(hashed_password, password)
    except VerifyMismatchError:
        return False
    # TODO: Add rehashing logic if needed
    # Do other stuff if needed, like rehashing if the hash is outdated
    # if ph.check_needs_rehash(hashed_password):
    #   do rehash stuff.
    return True

