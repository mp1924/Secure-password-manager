import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from database import init_db, insert_password, load_data, delete_password
from auth import register_master, verify_master
from crypto_utils import derive_key, create_cipher, encrypt_password, decrypt_password

# ---------------- GLOBAL ----------------
cipher = None


# ---------------- APP UI ----------------
def run_app():
    global cipher

    init_db()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    login_window()


# ---------------- LOGIN ----------------
def login_window():
    login = ctk.CTk()
    login.title("Login")
    login.geometry("350x220")

    entry = ctk.CTkEntry(login, show="*")
    entry.pack(pady=10)

    status = ctk.CTkLabel(login, text="")
    status.pack()

    def do_login():
        global cipher

        ok, salt = verify_master(entry.get())

        if not ok:
            status.configure(text="Wrong password!", text_color="red")
            return

        key = derive_key(entry.get(), salt)
        cipher = create_cipher(key)

        login.destroy()
        main_window()

    def setup():
        register_master(entry.get())
        status.configure(text="Setup Done! Restart App", text_color="green")

    ctk.CTkButton(login, text="Login", command=do_login).pack(pady=5)
    ctk.CTkButton(login, text="First Time Setup", command=setup).pack(pady=5)

    login.mainloop()


# ---------------- MAIN WINDOW ----------------
def main_window():
    app = ctk.CTk()
    app.title("Password Manager")
    app.geometry("850x600")

    site = ctk.CTkEntry(app, placeholder_text="Site")
    site.pack()

    user = ctk.CTkEntry(app, placeholder_text="Username")
    user.pack()

    pwd = ctk.CTkEntry(app, placeholder_text="Password", show="*")
    pwd.pack()

    status = ctk.CTkLabel(app, text="")
    status.pack()

    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True)

    table = ttk.Treeview(frame, columns=("Site", "User", "Password"), show="headings")
    table.heading("Site", text="Site")
    table.heading("User", text="User")
    table.heading("Password", text="Password")
    table.pack(fill="both", expand=True)

    # ---------------- FUNCTIONS ----------------
    def refresh():
        for i in table.get_children():
            table.delete(i)

        for row in load_data():
            try:
                dec = decrypt_password(cipher, row[3])
            except:
                dec = "ERROR"

            table.insert("", "end", iid=row[0], values=(row[1], row[2], dec))

    def save():
        enc = encrypt_password(cipher, pwd.get())
        insert_password(site.get(), user.get(), enc)
        refresh()
        status.configure(text="Saved!", text_color="green")

    def remove():
        sel = table.focus()
        if sel:
            delete_password(sel)
            refresh()

    def copy():
        sel = table.focus()
        if sel:
            val = table.item(sel)["values"][2]
            app.clipboard_clear()
            app.clipboard_append(val)

    ctk.CTkButton(app, text="Save", command=save).pack()
    ctk.CTkButton(app, text="Refresh", command=refresh).pack()
    ctk.CTkButton(app, text="Delete", command=remove).pack()
    ctk.CTkButton(app, text="Copy", command=copy).pack()

    refresh()
    app.mainloop()
