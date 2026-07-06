import hashlib
import hmac
import logging
import os

from backend.database import get_master, store_master

logger = logging.getLogger(__name__)


# ---------------- REGISTER ----------------
def register_master(password: str) -> None:
    """
    Register a new master password.

    A random salt is generated and stored along with the
    SHA-256 hash of the password and salt.
    """
    try:
        salt = os.urandom(16).hex()

        master_hash = hashlib.sha256(
            (password + salt).encode("utf-8")
        ).hexdigest()

        store_master(master_hash, salt)

    except Exception:
        logger.exception("Failed to register master password.")
        raise


# ---------------- VERIFY ----------------
def verify_master(password: str) -> tuple[bool, str | None]:
    """
    Verify the entered master password.

    Returns:
        (True, salt) if authentication succeeds.
        (False, None) otherwise.
    """
    try:
        data = get_master()

        if data is None:
            return False, None

        stored_hash, salt = data

        test_hash = hashlib.sha256(
            (password + salt).encode("utf-8")
        ).hexdigest()

        if hmac.compare_digest(test_hash, stored_hash):
            return True, salt

        return False, None

    except Exception:
        logger.exception("Master password verification failed.")
        return False, None