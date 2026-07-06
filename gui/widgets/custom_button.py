import customtkinter as ctk

from gui.assets.themes.dark_theme import (
    PRIMARY,
    PRIMARY_HOVER,
    TEXT,
    BORDER_RADIUS,
    FONT,
    TEXT_SIZE,
)

import customtkinter as ctk

class PrimaryButton(ctk.CTkButton):
    def __init__(self, *args, icon=None, **kwargs):

        if icon is not None:
            kwargs["image"] = icon
            kwargs["compound"] = "left"  # icon + text side by side

        super().__init__(*args, **kwargs)

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color=PRIMARY,
            hover_color=PRIMARY_HOVER,
            text_color=TEXT,
            corner_radius=BORDER_RADIUS,
            height=42,
            font=(FONT, TEXT_SIZE, "bold"),
            cursor="hand2",
            **kwargs
        )