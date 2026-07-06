import customtkinter as ctk

from gui.assets.icon_loader import load_icon
from gui.widgets.custom_button import PrimaryButton


def create_header(parent):

    header = ctk.CTkFrame(
        parent,
        height=70,
        corner_radius=0
    )
    header.pack(fill="x")

    # ==========================
    # Logo
    # ==========================

    logo = ctk.CTkLabel(
        header,
        text="🔐",
        font=("Segoe UI Emoji", 28)
    )
    logo.pack(
        side="left",
        padx=(20, 10),
        pady=15
    )

    # ==========================
    # Title
    # ==========================

    title = ctk.CTkLabel(
        header,
        text="Secure Password Manager",
        font=("Arial", 24, "bold")
    )
    title.pack(
        side="left",
        pady=15
    )

    # ==========================
    # Logout Button
    # ==========================

    logout_icon = load_icon("logout")

    logout_button = PrimaryButton(
        header,
        text="Logout",
        image=logout_icon,
        compound="left"
    )

    logout_button.pack(
        side="right",
        padx=20,
        pady=15
    )

    return logout_button