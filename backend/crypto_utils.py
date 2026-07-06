import base64
import hashlib
import logging
from cryptography.fernet import Fernet

logger = logging.getLogger(__name__)

# PBKDF2 Configuration
ITERATIONS = 200_000
HASH_NAME = "sha256"


def derive_key(password: str, salt_hex: str) -> bytes:
    """
    Derive a Fernet-compatible encryption key from the master password.
    """
    try:
        salt = bytes.fromhex(salt_hex)

        key = hashlib.pbkdf2_hmac(
            HASH_NAME,
            password.encode("utf-8"),
            salt,
            ITERATIONS,
        )

        return base64.urlsafe_b64encode(key)

    except Exception:
        logger.exception("Failed to derive encryption key.")
        raise


def create_cipher(key: bytes) -> Fernet:
    """
    Create a Fernet cipher instance.
    """
    return Fernet(key)


def encrypt_password(cipher: Fernet, password: str) -> str:
    """
    Encrypt a password.
    """
    try:
        return cipher.encrypt(password.encode("utf-8")).decode("utf-8")
    except Exception:
        logger.exception("Password encryption failed.")
        raise


def decrypt_password(cipher: Fernet, encrypted_password: str) -> str:
    """
    Decrypt an encrypted password.
    """
    try:
        return cipher.decrypt(
            encrypted_password.encode("utf-8")
        ).decode("utf-8")
    except Exception:
        logger.exception("Password decryption failed.")
        raise