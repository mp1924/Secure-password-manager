import logging
import sqlite3
from pathlib import Path
from typing import List, Optional, Tuple

logger = logging.getLogger(__name__)

# Always create/use vault.db in the project root
DB_FILE = Path(__file__).resolve().parent.parent / "vault.db"


def get_connection() -> sqlite3.Connection:
    """
    Create and return a database connection.
    """

    print("=" * 60)
    print("Using Database:", DB_FILE)
    print("=" * 60)

    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# ==========================================================
# DATABASE INITIALIZATION
# ==========================================================

def init_db() -> None:
    """
    Create required database tables if they do not exist.
    """

    try:
        with get_connection() as conn:

            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS vault (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    site TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS auth (
                    id INTEGER PRIMARY KEY,
                    master_hash TEXT NOT NULL,
                    salt TEXT NOT NULL
                )
            """)

            conn.commit()

            print("Database initialized successfully.")

    except sqlite3.Error:
        logger.exception("Failed to initialize database.")
        raise


# ==========================================================
# VAULT OPERATIONS
# ==========================================================

def insert_password(site: str, username: str, password: str) -> None:
    """
    Store an encrypted password in the vault.
    """

    try:
        with get_connection() as conn:

            conn.execute(
                """
                INSERT INTO vault (site, username, password)
                VALUES (?, ?, ?)
                """,
                (
                    site,
                    username,
                    password,
                ),
            )

            conn.commit()

            print("Password inserted successfully.")

    except sqlite3.Error:
        logger.exception("Failed to insert password.")
        raise


def load_data() -> List[Tuple[int, str, str, str]]:
    """
    Retrieve all password entries.
    """

    try:
        with get_connection() as conn:

            cursor = conn.execute(
                """
                SELECT id, site, username, password
                FROM vault
                """
            )

            return cursor.fetchall()

    except sqlite3.Error:
        logger.exception("Failed to load vault data.")
        raise


def delete_password(entry_id: int) -> None:
    """
    Delete a password entry by its ID.
    """

    try:
        with get_connection() as conn:

            conn.execute(
                "DELETE FROM vault WHERE id = ?",
                (entry_id,),
            )

            conn.commit()

            print("Password deleted successfully.")

    except sqlite3.Error:
        logger.exception("Failed to delete password.")
        raise


# ==========================================================
# AUTH OPERATIONS
# ==========================================================

def store_master(master_hash: str, salt: str) -> None:
    """
    Store the master password hash and salt.
    """

    try:
        with get_connection() as conn:

            conn.execute("DELETE FROM auth")

            conn.execute(
                """
                INSERT INTO auth (id, master_hash, salt)
                VALUES (1, ?, ?)
                """,
                (
                    master_hash,
                    salt,
                ),
            )

            conn.commit()

    except sqlite3.Error:
        logger.exception("Failed to store master credentials.")
        raise


def get_master() -> Optional[Tuple[str, str]]:
    """
    Retrieve the stored master password hash and salt.
    """

    try:
        with get_connection() as conn:

            cursor = conn.execute(
                """
                SELECT master_hash, salt
                FROM auth
                WHERE id = 1
                """
            )

            return cursor.fetchone()

    except sqlite3.Error:
        logger.exception("Failed to retrieve master credentials.")
        raise