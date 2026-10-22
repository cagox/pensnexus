import hmac, hashlib
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def hash_password(password: str, pepper: str) -> str:
    """
    Hashes a password using hmac and Argon2.

    Args:
        password (str): The password to hash.
        pepper (str): The pepper to use for hashing.

    Returns:
        str: The hashed password.
    """
    keyed_pw = hmac.new(pepper.encode(), password.encode(), hashlib.sha256).hexdigest()
    return ph.hash(keyed_pw)

def verify_password(hashed_password: str, password: str, pepper: str) -> bool:
    """
    Verifies a password against its hash using Argon2.

    Args:
        hashed_password (str): The hashed password.
        password (str): The password to verify.
        pepper (str): The pepper used for hashing.

    Returns:
        bool: True if the password is correct, False otherwise.
    """
    keyed_pw = hmac.new(pepper.encode(), password.encode(), hashlib.sha256).hexdigest()
    try:
        ph.verify(hashed_password, keyed_pw)
    except VerifyMismatchError:
        return False
    # TODO: Add rehashing logic if needed
    # Do other stuff if needed, like rehashing if the hash is outdated
    # if ph.check_needs_rehash(hashed_password):
    #   do rehash stuff.
    return True

