import customtkinter as ctk

from gui.widgets import PrimaryButton
from gui.assets.icon_loader import load_icon


def create_details_panel(parent):

    # =====================================
    # Panel
    # =====================================

    panel = ctk.CTkFrame(
        parent,
        width=300,
        corner_radius=15
    )

    panel.pack(
        side="right",
        fill="y"
    )

    panel.pack_propagate(False)

    # =====================================
    # Load Icons
    # =====================================

    copy_icon = load_icon("copy")
    edit_icon = load_icon("edit")
    delete_icon = load_icon("delete")
    visibility_icon = load_icon("visibility")

    # =====================================
    # Title
    # =====================================

    title = ctk.CTkLabel(
        panel,
        text="Password Details",
        font=("Arial", 20, "bold")
    )

    title.pack(
        pady=(20, 25)
    )

    # =====================================
    # Details Label
    # =====================================

    details = ctk.CTkLabel(
        panel,
        text="Select a password\nfrom the table.",
        justify="left"
    )

    details.pack(
        padx=20,
        anchor="w"
    )

    # =====================================
    # Show Password Button
    # =====================================

    show_button = PrimaryButton(
        panel,
        text="Show Password",
        image=visibility_icon,
        compound="left"
    )

    show_button.pack(
        fill="x",
        padx=20,
        pady=(30, 10)
    )

    # =====================================
    # Copy Button
    # =====================================

    copy_button = PrimaryButton(
        panel,
        text="Copy Password",
        image=copy_icon,
        compound="left"
    )

    copy_button.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # =====================================
    # Edit Button
    # =====================================

    edit_button = PrimaryButton(
        panel,
        text="Edit Password",
        image=edit_icon,
        compound="left"
    )

    edit_button.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # =====================================
    # Delete Button
    # =====================================

    delete_button = PrimaryButton(
        panel,
        text="Delete Password",
        image=delete_icon,
        compound="left"
    )

    delete_button.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # =====================================
    # Return Widgets
    # =====================================

    return {
        "panel": panel,
        "details": details,
        "show": show_button,
        "copy": copy_button,
        "edit": edit_button,
        "delete": delete_button,
    }