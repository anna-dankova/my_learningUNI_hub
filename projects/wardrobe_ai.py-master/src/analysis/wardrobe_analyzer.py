import sys
from pathlib import Path
from collections import Counter

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from src.db.repository import get_all_garments, update_garment_notes



def analyze_wardrobe() -> dict:
    garments = get_all_garments()

    if not garments:
        return {"error": "Гардероб пуст. Сначала добавь вещи."}

    total = len(garments)

    categories  = Counter(g["category"]  for g in garments)
    subtypes    = Counter(g["subtype"]   for g in garments)
    colors      = Counter(g["color"]     for g in garments if g["color"]     and g["color"]     != "unknown")
    styles      = Counter(g["style"]     for g in garments if g["style"]     and g["style"]     != "unknown")
    seasons     = Counter(g["season"]    for g in garments if g["season"]    and g["season"]    != "unknown")
    formalities = Counter(g["formality"] for g in garments if g["formality"] and g["formality"] != "unknown")

    dominant_color     = colors.most_common(1)[0][0]      if colors      else "нет данных"
    dominant_style     = styles.most_common(1)[0][0]      if styles      else "нет данных"
    dominant_season    = seasons.most_common(1)[0][0]     if seasons     else "нет данных"
    dominant_formality = formalities.most_common(1)[0][0] if formalities else "нет данных"

    tops    = categories.get("top", 0)
    bottoms = categories.get("bottom", 0)
    balance_ok = tops > 0 and bottoms > 0

    tips = []
    if tops == 0:
        tips.append("❗ Нет верхней одежды — добавь футболки, свитера или рубашки.")
    if bottoms == 0:
        tips.append("❗ Нет нижней одежды — добавь джинсы, брюки или юбки.")
    if len(colors) == 0:
        tips.append("⚠️ Цвета не определены — попробуй переобработать фото.")
    if dominant_formality == "low" and formalities.get("high", 0) == 0:
        tips.append("💡 Гардероб полностью casual — возможно, стоит добавить формальные вещи.")
    if not tips:
        tips.append("✅ Гардероб сбалансирован!")

    return {
        "total":              total,
        "categories":         dict(categories),
        "subtypes":           dict(subtypes),
        "colors":             dict(colors),
        "styles":             dict(styles),
        "seasons":            dict(seasons),
        "formalities":        dict(formalities),
        "dominant_color":     dominant_color,
        "dominant_style":     dominant_style,
        "dominant_season":    dominant_season,
        "dominant_formality": dominant_formality,
        "balance_ok":         balance_ok,
        "tips":               tips,
    }


def print_report(report: dict):
    if "error" in report:
        print(report["error"])
        return

    print("\n" + "="*45)
    print("       👗 АНАЛИЗ ГАРДЕРОБА")
    print("="*45)

    print(f"\n📦 Всего вещей: {report['total']}")

    print("\n📂 По категориям:")
    for cat, count in report["categories"].items():
        print(f"   {cat:<12} — {count} шт.")

    print("\n👕 По подтипам:")
    for sub, count in report["subtypes"].items():
        print(f"   {sub:<12} — {count} шт.")

    print("\n🎨 По цветам:")
    if report["colors"]:
        for color, count in sorted(report["colors"].items(), key=lambda x: -x[1]):
            print(f"   {color:<12} — {count} шт.")
    else:
        print("   нет данных")

    print("\n🎭 По стилям:")
    if report["styles"]:
        for style, count in report["styles"].items():
            print(f"   {style:<12} — {count} шт.")
    else:
        print("   нет данных")

    print("\n🌤 По сезонам:")
    if report["seasons"]:
        for season, count in report["seasons"].items():
            print(f"   {season:<12} — {count} шт.")
    else:
        print("   нет данных")

    print("\n🔑 Доминанты гардероба:")
    print(f"   Цвет:         {report['dominant_color']}")
    print(f"   Стиль:        {report['dominant_style']}")
    print(f"   Сезон:        {report['dominant_season']}")
    print(f"   Формальность: {report['dominant_formality']}")

    print("\n💬 Советы:")
    for tip in report["tips"]:
        print(f"   {tip}")

    print("\n" + "="*45 + "\n")


def generate_smart_name(garment: dict) -> str:
    parts = []
    color   = garment.get("color", "")
    subtype = garment.get("subtype", "")

    if color   and color   != "unknown":
        parts.append(color)
    if subtype and subtype != "unknown":
        parts.append(subtype)

    return " ".join(parts) if parts else garment.get("filename", "item")


def rename_garments():
    garments = get_all_garments()
    if not garments:
        print("⚠️ Гардероб пуст.")
        return

    name_counter = Counter(generate_smart_name(g) for g in garments)
    name_seen    = {}

    print("\n🏷 Переименование вещей:\n")

    for g in garments:
        base_name = generate_smart_name(g)
        total     = name_counter[base_name]

        if total == 1:
            new_name = base_name
        else:
            name_seen[base_name]  = name_seen.get(base_name, 0) + 1
            new_name = f"{base_name} {name_seen[base_name]}"

        old = g.get("filename") or g.get("image_path", "без имени")
        print(f"   {old}  →  {new_name}")
        # Сохраняем красивое имя в notes, не трогаем image_path
        update_garment_notes(g["id"], new_name)


    print("\n✅ Готово!")


if __name__ == "__main__":
    report = analyze_wardrobe()
    print_report(report)



