import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.db.repository import (
    get_all_garments,
    filter_garments,
    search_by_description,
    get_wardrobe_stats,
)


def print_items(items: list[dict], label: str):
    print(f"\n{'─' * 50}")
    print(f"🔍 {label} — найдено: {len(items)}")
    print(f"{'─' * 50}")
    if not items:
        print("  (пусто)")
        return
    for item in items:
        color = item.get("color", "?")
        fit   = item.get("fit", "?")
        sub   = item.get("subtype", "?")
        style = item.get("style", "?")
        season= item.get("season", "?")
        name  = Path(item.get("image_path", "?")).name
        print(f"  [{item['id']}] {color} {fit} {sub} | {style} | {season} | {name}")


def print_stats(stats: dict):
    print(f"\n{'═' * 50}")
    print("📊 СТАТИСТИКА ГАРДЕРОБА")
    print(f"{'═' * 50}")
    labels = {
        "category":  "Категории",
        "color":     "Цвета",
        "style":     "Стили",
        "season":    "Сезоны",
        "formality": "Формальность",
        "fit":       "Фит",
    }
    for field, data in stats.items():
        print(f"\n  {labels.get(field, field)}:")
        for value, count in data.items():
            bar = "█" * count
            print(f"    {value:15} {bar} ({count})")


if __name__ == "__main__":
    # ── Все вещи ────────────────────────────────
    all_items = get_all_garments()
    print_items(all_items, "Весь гардероб")

    # ── Фильтры ─────────────────────────────────
    print_items(
        filter_garments(color="black"),
        "Все чёрные вещи"
    )

    print_items(
        filter_garments(style="casual"),
        "Все casual вещи"
    )

    print_items(
        filter_garments(season="autumn"),
        "Все осенние вещи"
    )

    print_items(
        filter_garments(category="top"),
        "Все топы"
    )

    # ── Комбинированный фильтр ───────────────────
    print_items(
        filter_garments(color="black", style="casual"),
        "Чёрные + casual"
    )

    # ── Поиск по описанию ────────────────────────
    print_items(
        search_by_description("shirt"),
        "Поиск по слову 'shirt'"
    )

    # ── Статистика ───────────────────────────────
    stats = get_wardrobe_stats()
    print_stats(stats)
