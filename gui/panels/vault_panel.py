import customtkinter as ctk

from gui.widgets import create_password_table


def create_vault_panel(parent):

    panel = ctk.CTkFrame(
        parent,
        corner_radius=15
    )

    panel.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 15)
    )

    title = ctk.CTkLabel(
        panel,
        text="🔐 Stored Passwords",
        font=("Arial", 20, "bold")
    )

    title.pack(
        anchor="w",
        padx=20,
        pady=(20, 10)
    )

    table = create_password_table(panel)

    table.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 20)
    )

    return {
    "panel": panel,
    "table": table,
}