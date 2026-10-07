import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.parsing.normalizer import normalize, normalize_value


def test_aliases_work():
    """Алиасы должны правильно конвертироваться."""
    assert normalize_value("color", "gray") == "grey"
    assert normalize_value("fit", "baggy") == "oversized"
    assert normalize_value("fit", "loose") == "oversized"
    assert normalize_value("season", "fall") == "autumn"
    assert normalize_value("style", "streetwear") == "downtown"
    assert normalize_value("subtype", "hoody") == "hoodie"
    assert normalize_value("subtype", "pants") == "trousers"


def test_valid_values_pass_through():
    """Правильные значения должны остаться без изменений."""
    assert normalize_value("category", "top") == "top"
    assert normalize_value("color", "black") == "black"
    assert normalize_value("fit", "oversized") == "oversized"
    assert normalize_value("season", "autumn") == "autumn"


def test_unknown_value_becomes_unknown():
    """Неизвестное значение → 'unknown'."""
    assert normalize_value("category", "underwear") == "unknown"
    assert normalize_value("color", "rainbow") == "unknown"
    assert normalize_value("fit", "ultra-baggy") == "unknown"


def test_case_insensitive():
    """Регистр не должен влиять на результат."""
    assert normalize_value("color", "BLACK") == "black"
    assert normalize_value("fit", "OVERSIZED") == "oversized"
    assert normalize_value("season", "AUTUMN") == "autumn"


def test_full_normalize_dict():
    """Полный словарь нормализуется корректно."""
    data = {
        "category": "top",
        "subtype": "hoody",
        "color": "gray",
        "secondary_color": "blue",
        "fit": "baggy",
        "season": "fall",
        "style": "streetwear",
        "formality": "low",
        "description_raw": "a gray baggy hoody",
        "notes": None,
    }
    result = normalize(data)
    assert result["subtype"] == "hoodie"
    assert result["color"] == "grey"
    assert result["fit"] == "oversized"
    assert result["season"] == "autumn"
    assert result["style"] == "downtown"
    assert result["description_raw"] == "a gray baggy hoody"  # не трогаем
