import customtkinter as ctk

from gui.widgets import (
    PrimaryButton,
    CustomEntry,
)

from backend.auth import register_master
from gui.dialogs import show_error, show_info


def setup_window():

    setup = ctk.CTk()

    setup.title("First Time Setup")
    setup.geometry("420x340")
    setup.resizable(False, False)

    # ---------------- Heading ----------------

    ctk.CTkLabel(
        setup,
        text="First Time Setup",
        font=("Arial", 22, "bold")
    ).pack(pady=(20, 20))

    # ---------------- Entries ----------------

    password_entry = CustomEntry(
        setup,
        width=280,
        show="*",
        placeholder_text="Create a Password"
    )
    password_entry.pack(pady=10)

    confirm_entry = CustomEntry(
        setup,
        width=280,
        show="*",
        placeholder_text="Confirm Password"
    )
    confirm_entry.pack(pady=10)

    # ---------------- Status ----------------

    status = ctk.CTkLabel(
        setup,
        text="",
        text_color="#E74C3C",
        font=("Arial", 12)
    )
    status.pack()

    # ---------------- Create Password ----------------

    def create_password():

        status.configure(text="")

        password = password_entry.get().strip()
        confirm = confirm_entry.get().strip()

        if not password or not confirm:
            show_error(
                "Error",
                "Please fill in all fields."
            )
            return

        if password != confirm:

            status.configure(
                text="Passwords do not match.",
                text_color="#E74C3C"
            )

            show_error(
                "Password Mismatch",
                "Passwords do not match."
            )
            return

        register_master(password)

        show_info(
            "Success",
            "Password created successfully."
        )

        setup.destroy()

        from gui.windows.login_window import login_window

        login_window()

    # ---------------- Back ----------------

    def back():

        setup.destroy()

        from gui.windows.login_window import login_window

        login_window()

    # ---------------- Buttons ----------------

    PrimaryButton(
        setup,
        text="Create Password",
        width=250,
        command=create_password
    ).pack(pady=(20, 10))

    PrimaryButton(
        setup,
        text="Back",
        width=250,
        command=back
    ).pack()

    setup.mainloop()