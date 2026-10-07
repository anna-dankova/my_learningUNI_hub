import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.parsing.parser import parse_caption


def test_all_fields_present():
    """Если все поля переданы — ничего не меняется."""
    data = {
        "category": "top",
        "subtype": "hoodie",
        "color": "black",
        "secondary_color": None,
        "fit": "oversized",
        "season": "autumn",
        "style": "casual",
        "formality": "low",
        "description_raw": "a black hoodie",
        "notes": None,
    }
    result = parse_caption(data)
    assert result["category"] == "top"
    assert result["subtype"] == "hoodie"
    assert result["color"] == "black"


def test_missing_fields_become_unknown():
    """Если поля нет — должно стать 'unknown'."""
    data = {
        "category": "top",
        "description_raw": "a shirt",
    }
    result = parse_caption(data)
    assert result["subtype"] == "unknown"
    assert result["fit"] == "unknown"
    assert result["season"] == "unknown"
    assert result["style"] == "unknown"
    assert result["formality"] == "unknown"


def test_empty_string_becomes_unknown():
    """Пустая строка тоже должна стать 'unknown'."""
    data = {
        "category": "",
        "subtype": "",
        "color": "",
        "description_raw": "test",
    }
    result = parse_caption(data)
    assert result["category"] == "unknown"
    assert result["subtype"] == "unknown"
    assert result["color"] == "unknown"


def test_secondary_color_can_be_none():
    """secondary_color и notes могут быть None — это норма."""
    data = {
        "description_raw": "a white shirt",
    }
    result = parse_caption(data)
    assert result["secondary_color"] is None
    assert result["notes"] is None
