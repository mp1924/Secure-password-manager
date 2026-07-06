import customtkinter as ctk
from tkinter import messagebox

from controllers.vault_controller import (
    save_password,
    load_passwords,
)

from gui.panels.header import create_header
from gui.panels.add_password_panel import create_add_password_panel
from gui.panels.vault_panel import create_vault_panel
from gui.panels.details_panel import create_details_panel


def main_window(cipher):

    # =====================================
    # Main Window
    # =====================================

    app = ctk.CTk()

    app.title("Secure Password Manager")
    app.geometry("1280x720")
    app.minsize(1100, 700)

    ctk.set_appearance_mode("dark")

    # =====================================
    # Header
    # =====================================

    create_header(app)

    # =====================================
    # Dashboard
    # =====================================

    dashboard = ctk.CTkFrame(
        app,
        fg_color="transparent"
    )

    dashboard.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # =====================================
    # Panels
    # =====================================

    add_password_panel = create_add_password_panel(dashboard)

    vault_panel = create_vault_panel(dashboard)

    details_panel = create_details_panel(dashboard)

    table = vault_panel["table"]

    # =====================================
    # Refresh Table
    # =====================================

    def refresh_table():

        # Clear old rows
        for row in table.get_children():
            table.delete(row)

        # Load data
        rows = load_passwords()

        for row in rows:

            entry_id, site, username, password = row

            table.insert(
                "",
                "end",
                iid=entry_id,
                values=(
                    site,
                    username,
                    "••••••••"
                )
            )

    # =====================================
    # Save Password
    # =====================================

    def on_save_password():

        try:

            site = add_password_panel["platform"].get().strip()
            username = add_password_panel["username"].get().strip()
            password = add_password_panel["password"].get().strip()

            save_password(
                cipher,
                site,
                username,
                password,
            )

            messagebox.showinfo(
                "Success",
                "Password saved successfully!"
            )

            add_password_panel["platform"].delete(0, "end")
            add_password_panel["username"].delete(0, "end")
            add_password_panel["password"].delete(0, "end")

            # Refresh the vault
            refresh_table()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e))

    # =====================================
    # Button Commands
    # =====================================

    add_password_panel["save"].configure(
        command=on_save_password
    )

    # =====================================
    # Initial Load
    # =====================================

    refresh_table()

    # =====================================
    # Main Loop
    # =====================================

    app.mainloop()