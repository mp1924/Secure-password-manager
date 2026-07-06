from backend.database import (
    insert_password,
    load_data,
    delete_password,
)

from backend.crypto_utils import (
    encrypt_password,
    decrypt_password,
)


# =====================================
# Save Password
# =====================================

def save_password(cipher, site, username, password):
    """
    Encrypt and save a password.
    """

    if not site.strip():
        raise ValueError("Platform cannot be empty.")

    if not username.strip():
        raise ValueError("Username cannot be empty.")

    if not password.strip():
        raise ValueError("Password cannot be empty.")

    encrypted_password = encrypt_password(cipher, password)

    insert_password(
        site,
        username,
        encrypted_password,
    )


# =====================================
# Load Passwords
# =====================================

def load_passwords():
    """
    Return all passwords stored in the database.
    """
    return load_data()


# =====================================
# Delete Password
# =====================================

def remove_password(entry_id):
    """
    Delete a password by its database ID.
    """
    delete_password(entry_id)


# =====================================
# Decrypt Password
# =====================================

def get_decrypted_password(cipher, encrypted_password):
    """
    Decrypt and return a password.
    """
    return decrypt_password(cipher, encrypted_password)