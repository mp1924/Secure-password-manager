import customtkinter as ctk

from backend.database import init_db
from gui.windows.login_window import login_window


def run_app() -> None:
    """
    Initialize the application and launch the login window.
    """
    init_db()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    login_window()