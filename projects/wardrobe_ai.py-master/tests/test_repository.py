import pytest
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

# Используем тестовую БД чтобы не трогать реальную
os.environ["WARDROBE_DB_PATH"] = "data/test_wardrobe.db"

from src.db.schema import create_tables, get_connection, DB_PATH
from src.db.repository import (
    add_garment,
    get_all_garments,
    filter_garments,
    delete_garment,
)

TEST_ITEM = {
    "image_path": "data/raw_images/test.jpg",
    "category": "top",
    "subtype": "hoodie",
    "color": "black",
    "secondary_color": None,
    "fit": "oversized",
    "season": "autumn",
    "style": "casual",
    "formality": "low",
    "description_raw": "a black oversized hoodie",
    "notes": None,
}


@pytest.fixture(autouse=True)
def setup_db():
    """Создаём чистую БД перед каждым тестом."""
    create_tables()
    yield
    # Чистим таблицу после теста
    conn = get_connection()
    conn.execute("DELETE FROM garments")
    conn.commit()
    conn.close()


def test_add_garment():
    """Вещь добавляется и возвращает валидный id."""
    new_id = add_garment(TEST_ITEM)
    assert isinstance(new_id, int)
    assert new_id > 0


def test_get_all_garments():
    """После добавления вещь должна быть в списке."""
    add_garment(TEST_ITEM)
    items = get_all_garments()
    assert len(items) >= 1
    assert items[0]["category"] == "top"
    assert items[0]["color"] == "black"


def test_filter_by_color():
    """Фильтрация по цвету работает корректно."""
    add_garment(TEST_ITEM)
    results = filter_garments(color="black")
    assert len(results) >= 1
    assert all(r["color"] == "black" for r in results)


def test_filter_no_results():
    """Фильтрация без совпадений возвращает пустой список."""
    add_garment(TEST_ITEM)
    results = filter_garments(color="pink")
    assert results == []


def test_filter_multiple_fields():
    """Комбинированная фильтрация работает."""
    add_garment(TEST_ITEM)
    results = filter_garments(color="black", style="casual")
    assert len(results) >= 1


def test_delete_garment():
    """Удаление вещи работает корректно."""
    new_id = add_garment(TEST_ITEM)
    deleted = delete_garment(new_id)
    assert deleted is True

    items = get_all_garments()
    ids = [item["id"] for item in items]
    assert new_id not in ids


def test_delete_nonexistent():
    """Удаление несуществующей вещи возвращает False."""
    result = delete_garment(99999)
    assert result is False
