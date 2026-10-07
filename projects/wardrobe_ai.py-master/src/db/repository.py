import sqlite3
from src.db.schema import get_connection


# ──────────────────────────────────────────────
#  GARMENTS
# ──────────────────────────────────────────────

def add_garment(data: dict) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO garments (
            image_path, category, subtype, color, secondary_color,
            fit, season, style, formality, description_raw, notes
        ) VALUES (
            :image_path, :category, :subtype, :color, :secondary_color,
            :fit, :season, :style, :formality, :description_raw, :notes
        )
    """, data)
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def get_all_garments() -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM garments ORDER BY created_at DESC")
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows


def filter_garments(**kwargs) -> list[dict]:
    if not kwargs:
        return get_all_garments()
    conditions = " AND ".join([f"{key} = :{key}" for key in kwargs])
    query = f"SELECT * FROM garments WHERE {conditions}"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, kwargs)
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows


def delete_garment(garment_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM garments WHERE id = ?", (garment_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted


def update_garment_filename(garment_id: int, new_name: str):
    conn = get_connection()
    conn.execute(
        "UPDATE garments SET image_path = ? WHERE id = ?",
        (new_name, garment_id)
    )
    conn.commit()
    conn.close()

def update_garment_notes(garment_id: int, notes: str):
    conn = get_connection()
    conn.execute(
        "UPDATE garments SET notes = ? WHERE id = ?",
        (notes, garment_id)
    )
    conn.commit()
    conn.close()

def update_garment(garment_id: int, data: dict):
    conn = get_connection()
    conn.execute(
        "UPDATE garments SET category=?, subtype=?, color=?, style=?, season=?, notes=? WHERE id=?",
        (data["category"], data["subtype"], data["color"], data["style"], data["season"], data["notes"], garment_id)
    )
    conn.commit()
    conn.close()


# ──────────────────────────────────────────────
#  OUTFITS
# ──────────────────────────────────────────────

def add_outfit(query_text: str, result_text: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO outfits (query_text, result_text) VALUES (?, ?)",
        (query_text, result_text)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def get_all_outfits() -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM outfits ORDER BY created_at DESC")
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows


# ──────────────────────────────────────────────
#  OUTFIT ITEMS
# ──────────────────────────────────────────────

def add_outfit_item(outfit_id: int, garment_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO outfit_items (outfit_id, garment_id) VALUES (?, ?)",
        (outfit_id, garment_id)
    )
    conn.commit()
    conn.close()


# ──────────────────────────────────────────────
#  ПОИСК И ФИЛЬТРАЦИЯ
# ──────────────────────────────────────────────

def search_by_description(keyword: str) -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM garments WHERE description_raw LIKE ?",
        (f"%{keyword.lower()}%",)
    )
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows


def get_wardrobe_stats() -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    stats = {}
    for field in ("category", "color", "style", "season", "formality", "fit"):
        cursor.execute(f"""
            SELECT {field}, COUNT(*) as count
            FROM garments
            WHERE {field} != 'unknown' AND {field} IS NOT NULL
            GROUP BY {field}
            ORDER BY count DESC
        """)
        stats[field] = {row[0]: row[1] for row in cursor.fetchall()}
    conn.close()
    return stats

def garment_exists(image_path: str) -> bool:
    """Проверяет есть ли уже такое фото в БД."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM garments WHERE image_path = ?",
        (image_path,)
    )
    exists = cursor.fetchone() is not None
    conn.close()
    return exists
def garment_exists(image_path: str) -> bool:
    """Проверяет есть ли уже такое фото в БД."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM garments WHERE image_path = ?",
        (image_path,)
    )
    exists = cursor.fetchone() is not None
    conn.close()
    return exists
