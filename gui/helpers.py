"""
Helper functions for the GUI.
"""

import logging
import customtkinter as ctk
from tkinter import ttk

from backend.database import load_data
from backend.crypto_utils import decrypt_password

logger = logging.getLogger(__name__)


def refresh_table(table: ttk.Treeview, cipher) -> None:
    """
    Refresh the password table with decrypted passwords.
    """
    try:
        # Clear existing rows
        for item in table.get_children():
            table.delete(item)

        # Load records
        rows = load_data()

        for row in rows:
            try:
                password = decrypt_password(cipher, row[3])
            except Exception:
                password = "DECRYPT ERROR"

            table.insert(
                "",
                "end",
                iid=row[0],
                values=(row[1], row[2], password)
            )

    except Exception as e:
        logger.exception("Failed to refresh table: %s", e)


def clear_entries(*entries: ctk.CTkEntry) -> None:
    """
    Clear one or more CTkEntry widgets.
    """
    for entry in entries:
        entry.delete(0, "end")


def copy_to_clipboard(root, text: str) -> None:
    """
    Copy text to the clipboard.
    """
    try:
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()

    except Exception as e:
        logger.exception("Clipboard error: %s", e)


def validate_inputs(site: str, username: str, password: str) -> bool:
    """
    Validate user input.
    """
    return all([
        site.strip(),
        username.strip(),
        password.strip()
    ])


def selected_item(table: ttk.Treeview):
    """
    Return the selected Treeview item ID.
    """
    return table.focus()