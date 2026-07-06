import customtkinter as ctk

from gui.assets.themes.dark_theme import (
    ENTRY,
    ENTRY_BORDER,
    TEXT,
    BORDER_RADIUS,
    FONT,
    TEXT_SIZE,
)

class CustomEntry(ctk.CTkEntry):
    """
    Reusable entry widget for the application.
    """

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color=ENTRY,
            border_color=ENTRY_BORDER,
            text_color=TEXT,
            corner_radius=BORDER_RADIUS,
            height=42,
            font=(FONT, TEXT_SIZE),
            border_width=1,
            **kwargs
        )