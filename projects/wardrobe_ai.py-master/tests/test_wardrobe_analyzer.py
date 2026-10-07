import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.analysis.wardrobe_analyzer import analyze_wardrobe, print_report
from unittest.mock import patch

MOCK_GARMENTS = [
    {"id": 1, "filename": "hoodie1.jpg", "category": "top", "subtype": "hoodie",
     "color": "black", "style": "casual", "season": "autumn", "formality": "low"},
    {"id": 2, "filename": "jeans1.jpg", "category": "bottom", "subtype": "jeans",
     "color": "blue", "style": "casual", "season": "autumn", "formality": "low"},
    {"id": 3, "filename": "hoodie2.jpg", "category": "top", "subtype": "sweater",
     "color": "white", "style": "casual", "season": "winter", "formality": "medium"},
]

def test_analyze_returns_dict():
    with patch("src.analysis.wardrobe_analyzer.get_all_garments", return_value=MOCK_GARMENTS):
        report = analyze_wardrobe()
    assert isinstance(report, dict)
    assert "error" not in report

def test_total_count():
    with patch("src.analysis.wardrobe_analyzer.get_all_garments", return_value=MOCK_GARMENTS):
        report = analyze_wardrobe()
    assert report["total"] == 3

def test_categories():
    with patch("src.analysis.wardrobe_analyzer.get_all_garments", return_value=MOCK_GARMENTS):
        report = analyze_wardrobe()
    assert report["categories"]["top"] == 2
    assert report["categories"]["bottom"] == 1

def test_dominant_color():
    with patch("src.analysis.wardrobe_analyzer.get_all_garments", return_value=MOCK_GARMENTS):
        report = analyze_wardrobe()
    assert report["dominant_color"] in ["black", "blue", "white"]

def test_balance_ok():
    with patch("src.analysis.wardrobe_analyzer.get_all_garments", return_value=MOCK_GARMENTS):
        report = analyze_wardrobe()
    assert report["balance_ok"] is True

def test_empty_wardrobe():
    with patch("src.analysis.wardrobe_analyzer.get_all_garments", return_value=[]):
        report = analyze_wardrobe()
    assert "error" in report

def test_print_report_no_crash(capsys):
    with patch("src.analysis.wardrobe_analyzer.get_all_garments", return_value=MOCK_GARMENTS):
        report = analyze_wardrobe()
    print_report(report)
    captured = capsys.readouterr()
    assert "АНАЛИЗ ГАРДЕРОБА" in captured.out
