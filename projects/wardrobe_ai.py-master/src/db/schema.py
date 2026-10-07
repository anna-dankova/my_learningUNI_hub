import sqlite3
from pathlib import Path

DB_PATH = Path("data/wardrobe.db")


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # результаты как словари
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS garments (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path       TEXT NOT NULL,
            category         TEXT,
            subtype          TEXT,
            color            TEXT,
            secondary_color  TEXT,
            fit              TEXT,
            season           TEXT,
            style            TEXT,
            formality        TEXT,
            description_raw  TEXT,
            notes            TEXT,
            created_at       DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS outfits (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            query_text  TEXT,
            result_text TEXT,
            created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS outfit_items (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            outfit_id  INTEGER NOT NULL,
            garment_id INTEGER NOT NULL,
            FOREIGN KEY (outfit_id)  REFERENCES outfits(id),
            FOREIGN KEY (garment_id) REFERENCES garments(id)
        );
    """)

    conn.commit()
    conn.close()
    print("✅ Таблицы созданы (или уже существуют)")
