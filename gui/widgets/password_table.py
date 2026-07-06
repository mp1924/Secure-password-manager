from tkinter import ttk

from gui.assets.themes.dark_theme import (
    TABLE_HEADER,
    TABLE_ROW,
    TABLE_SELECTED,
    TEXT,
    FONT,
)


def create_password_table(parent) -> ttk.Treeview:
    """
    Create and return the password table.
    """

    style = ttk.Style()
    style.theme_use("default")

    # ==============================
    # Table Style
    # ==============================

    style.configure(
        "Treeview",
        background=TABLE_ROW,
        foreground=TEXT,
        fieldbackground=TABLE_ROW,
        borderwidth=0,
        rowheight=36,
        font=(FONT, 12)
    )

    # ==============================
    # Header Style
    # ==============================

    style.configure(
        "Treeview.Heading",
        background=TABLE_HEADER,
        foreground=TEXT,
        font=(FONT, 12, "bold"),
        relief="flat"
    )

    # ==============================
    # Selected Row
    # ==============================

    style.map(
        "Treeview",
        background=[
            ("selected", TABLE_SELECTED)
        ],
        foreground=[
            ("selected", TEXT)
        ]
    )

    # ==============================
    # Table
    # ==============================

    table = ttk.Treeview(
        parent,
        columns=(
            "ID",
            "Site",
            "Username",
        ),
        show="headings",
        selectmode="browse"
    )

    # ==============================
    # Headings
    # ==============================

    table.heading("ID", text="ID")
    table.heading("Site", text="Platform")
    table.heading("Username", text="Username / Email")

    # ==============================
    # Columns
    # ==============================

    # Hidden ID column
    table.column(
        "ID",
        width=0,
        stretch=False
    )

    table.column(
        "Site",
        width=220,
        anchor="center"
    )

    table.column(
        "Username",
        width=320,
        anchor="center"
    )

    return table