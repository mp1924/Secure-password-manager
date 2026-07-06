import customtkinter as ctk

from gui.assets.icon_loader import load_icon
from gui.widgets import PrimaryButton, CustomEntry
from backend.password_generator import generate_password


def create_add_password_panel(parent):

    panel = ctk.CTkFrame(
        parent,
        width=320,
        corner_radius=15
    )

    panel.pack(
        side="left",
        fill="y",
        padx=(0, 15)
    )

    panel.pack_propagate(False)

    # =====================================
    # Title
    # =====================================

    title = ctk.CTkLabel(
        panel,
        text="Add Password",
        font=("Arial", 22, "bold")
    )

    title.pack(pady=(20, 25))

    # =====================================
    # Platform
    # =====================================

    platform_label = ctk.CTkLabel(
        panel,
        text="Platform",
        anchor="w"
    )

    platform_label.pack(fill="x", padx=20)

    platform_entry = CustomEntry(
        panel,
        placeholder_text="Google, GitHub..."
    )

    platform_entry.pack(
        fill="x",
        padx=20,
        pady=(5, 15)
    )

    # =====================================
    # Username
    # =====================================

    username_label = ctk.CTkLabel(
        panel,
        text="Username / Email",
        anchor="w"
    )

    username_label.pack(fill="x", padx=20)

    username_entry = CustomEntry(
        panel,
        placeholder_text="example@email.com"
    )

    username_entry.pack(
        fill="x",
        padx=20,
        pady=(5, 15)
    )

    # =====================================
    # Password
    # =====================================

    password_label = ctk.CTkLabel(
        panel,
        text="Password",
        anchor="w"
    )

    password_label.pack(fill="x", padx=20)

    password_entry = CustomEntry(
        panel,
        placeholder_text="Enter Password",
        show="*"
    )

    password_entry.pack(
        fill="x",
        padx=20,
        pady=(5, 15)
    )

    # =====================================
    # Password Length
    # =====================================

    length_label = ctk.CTkLabel(
        panel,
        text="Password Length",
        anchor="w"
    )

    length_label.pack(fill="x", padx=20)

    length_combo = ctk.CTkComboBox(
        panel,
        values=[
            "8",
            "12",
            "16",
            "20",
            "24",
            "32"
        ]
    )

    length_combo.set("16")

    length_combo.pack(
        fill="x",
        padx=20,
        pady=(5, 15)
    )

    # =====================================
    # Password Options
    # =====================================

    upper_var = ctk.BooleanVar(value=True)
    lower_var = ctk.BooleanVar(value=True)
    number_var = ctk.BooleanVar(value=True)
    symbol_var = ctk.BooleanVar(value=True)

    ctk.CTkCheckBox(
        panel,
        text="Uppercase",
        variable=upper_var
    ).pack(anchor="w", padx=20)

    ctk.CTkCheckBox(
        panel,
        text="Lowercase",
        variable=lower_var
    ).pack(anchor="w", padx=20)

    ctk.CTkCheckBox(
        panel,
        text="Numbers",
        variable=number_var
    ).pack(anchor="w", padx=20)

    ctk.CTkCheckBox(
        panel,
        text="Symbols",
        variable=symbol_var
    ).pack(
        anchor="w",
        padx=20,
        pady=(0, 20)
    )

    # =====================================
    # Generate Password
    # =====================================

    def on_generate_password():
        print("Generate button clicked")
        try:

            password = generate_password(
                length=int(length_combo.get()),
                use_upper=upper_var.get(),
                use_lower=lower_var.get(),
                use_numbers=number_var.get(),
                use_symbols=symbol_var.get(),
            )

            password_entry.delete(0, "end")
            password_entry.insert(0, password)

        except Exception as error:
            print(error)
    
    # =====================================
    # Load Icons
    # =====================================

    generate_icon = load_icon("generate")
    save_icon = load_icon("save")

    # =====================================
    # Buttons
    # =====================================

    generate_button = PrimaryButton(
        panel,
        text="Generate Password",
        image=generate_icon,
        compound="left",
        command=on_generate_password
    )
    generate_button.pack(
        fill="x",
        padx=20,
        pady=(0, 10)
    )

    save_button = PrimaryButton(
        panel,
        text="Save Password",
        image=save_icon,
        compound="left"
)

    save_button.pack(
        fill="x",
        padx=20
    )

    return {
        "panel": panel,
        "platform": platform_entry,
        "username": username_entry,
        "password": password_entry,
        "length": length_combo,
        "uppercase": upper_var,
        "lowercase": lower_var,
        "numbers": number_var,
        "symbols": symbol_var,
        "generate": generate_button,
        "save": save_button,
    }