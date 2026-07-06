from pathlib import Path
from PIL import Image
import customtkinter as ctk

# Folder containing all icons
ICON_DIR = Path(__file__).parent / "icons"


def load_icon(name: str, size=(20, 20)):
    """
    Load an icon from gui/assets/icons.

    Example:
        load_icon("save")
        load_icon("generate")
        load_icon("visibility")
    """

    icon_path = ICON_DIR / f"{name}.png"

    return ctk.CTkImage(
        light_image=Image.open(icon_path),
        dark_image=Image.open(icon_path),
        size=size,
    )