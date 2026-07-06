import customtkinter as ctk

from gui.widgets import (
    PrimaryButton,
    CustomEntry,
)

from backend.auth import verify_master
from backend.crypto_utils import derive_key, create_cipher
from gui.dialogs import show_error
from gui.windows.main_window import main_window


def login_window():
    login = ctk.CTk()

    login.title("Secure Password Manager")
    login.geometry("420x280")
    login.resizable(False, False)

    ctk.CTkLabel(
        login,
        text="🔐 Secure Password Manager",
        font=("Arial", 22, "bold")
    ).pack(pady=(20, 20))

    password_entry = CustomEntry(
        login,
        width=280,
        show="*",
        placeholder_text="Enter Password"
    )
    password_entry.pack(pady=10)

    status = ctk.CTkLabel(
       login,
       text="",
       text_color="#E74C3C",
       font=("Arial", 12)
)
    status.pack()

    # ---------------- Login ----------------

    def login_user():

        password = password_entry.get().strip()
        status.configure(text="")

        if not password:
            show_error(
                "Login Failed",
                "Please enter your password."
            )
            return

        ok, salt = verify_master(password)

        if not ok:
         status.configure(
    text="Incorrect Password",
    text_color="#E74C3C"
)
         return

        key = derive_key(password, salt)

        cipher = create_cipher(key)

        login.destroy()

        main_window(cipher)

    # ---------------- Open Setup ----------------

    def open_setup():

        from gui.windows.setup_window import setup_window

        login.destroy()

        setup_window()

    login_button = PrimaryButton(
        login,
        text="Login",
        width=250,
        command=login_user
    )
    login_button.pack(pady=(20, 10))

    setup_button = PrimaryButton(
        login,
        text="First Time Setup",
        width=250,
        command=open_setup
    )
    setup_button.pack(pady=10)

    login.mainloop()