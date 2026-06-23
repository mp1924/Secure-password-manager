import sqlite3

DB_FILE = "vault.db"

# ---------------- INIT DB ----------------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS vault (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site TEXT,
            username TEXT,
            password TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS auth (
            id INTEGER PRIMARY KEY,
            master_hash TEXT,
            salt TEXT
        )
    """)

    conn.commit()
    conn.close()


# ---------------- VAULT OPERATIONS ----------------
def insert_password(site, username, password):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO vault (site, username, password) VALUES (?, ?, ?)",
        (site, username, password)
    )
    conn.commit()
    conn.close()


def load_data():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, site, username, password FROM vault")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_password(entry_id):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("DELETE FROM vault WHERE id=?", (entry_id,))
    conn.commit()
    conn.close()


# ---------------- AUTH TABLE ----------------
def store_master(master_hash, salt):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("DELETE FROM auth")
    cur.execute(
        "INSERT INTO auth (id, master_hash, salt) VALUES (1, ?, ?)",
        (master_hash, salt)
    )

    conn.commit()
    conn.close()


def get_master():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("SELECT master_hash, salt FROM auth WHERE id=1")
    row = cur.fetchone()

    conn.close()
    return row
