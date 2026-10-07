import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from src.services.process_images_service import process_images
from src.analysis.wardrobe_analyzer import analyze_wardrobe, print_report, rename_garments
from src.db.repository import get_all_garments, filter_garments
from src.llm.outfit_generator import generate_outfits


def menu():
    print("\n" + "="*45)
    print("        👗 WARDROBE AI — ГЛАВНОЕ МЕНЮ")
    print("="*45)
    print("  1 — 📸 Обработать новые фото")
    print("  2 — 👗 Показать весь гардероб")
    print("  3 — 📊 Анализ гардероба")
    print("  4 — 🔍 Фильтрация вещей")
    print("  5 — ✨ Сгенерировать образ")
    print("  6 — 🏷  Переименовать вещи")
    print("  7 — 🗑  Очистить гардероб")
    print("  0 — 🚪 Выйти")
    print("="*45)
    return input("  Выбери действие: ").strip()


def show_wardrobe():
    garments = get_all_garments()
    if not garments:
        print("\n⚠️  Гардероб пуст. Сначала обработай фото (пункт 1).")
        return
    print(f"\n📦 Всего вещей: {len(garments)}\n")
    for g in garments:
        print(f"  {g.get('image_path', 'без имени')}")
        print(f"       Категория:    {g['category']} / {g['subtype']}")
        print(f"       Цвет:         {g['color']}")
        print(f"       Стиль:        {g['style']}")
        print(f"       Сезон:        {g['season']}")
        print(f"       Формальность: {g['formality']}")
        print()


def clear_wardrobe():
    confirm = input("\n⚠️  Удалить ВСЕ вещи из гардероба? (да / нет): ").strip().lower()
    if confirm != "да":
        print("❌ Отменено.")
        return
    from src.db.schema import get_connection
    conn = get_connection()
    conn.execute("DELETE FROM garments")
    conn.execute("DELETE FROM outfits")
    conn.execute("DELETE FROM outfit_items")
    conn.commit()
    conn.close()
    print("✅ Гардероб полностью очищен!")


def filter_menu():
    print("\n🔍 Фильтрация — введи параметры (Enter = пропустить):")
    color    = input("   Цвет (black/white/...):      ").strip() or None
    style    = input("   Стиль (casual/formal/...):   ").strip() or None
    season   = input("   Сезон (spring/autumn/...):   ").strip() or None
    category = input("   Категория (top/bottom/...):  ").strip() or None

    results = filter_garments(color=color, style=style, season=season, category=category)

    if not results:
        print("\n⚠️  Ничего не найдено по этим фильтрам.")
        return

    print(f"\n✅ Найдено: {len(results)} шт.\n")
    for g in results:
        print(f"  {g.get('image_path', 'без имени')} — {g['category']}/{g['subtype']}, {g['color']}, {g['style']}")


def generate_menu():
    print("\n✨ Генерация образа — введи параметры (Enter = пропустить):")
    occasion = input("   Повод (прогулка/работа/вечеринка/...): ").strip() or "повседневный выход"
    style    = input("   Стиль (casual/formal/...):              ").strip() or None
    season   = input("   Сезон (spring/summer/autumn/winter):    ").strip() or None

    garments = filter_garments(style=style, season=season)
    if not garments:
        garments = get_all_garments()

    if not garments:
        print("\n⚠️  Гардероб пуст. Сначала обработай фото (пункт 1).")
        return

    print("\n⏳ Генерирую образ, подожди...\n")
    result = generate_outfits(user_request=occasion)
    print("✨ Готовый образ:\n")
    print(result)


def main():
    print("\n🚀 Добро пожаловать в Wardrobe AI!")

    while True:
        choice = menu()

        if choice == "1":
            print("\n📸 Обрабатываю фото из data/raw_images/ ...")
            process_images()
            print("✅ Готово!")

        elif choice == "2":
            show_wardrobe()

        elif choice == "3":
            report = analyze_wardrobe()
            print_report(report)

        elif choice == "4":
            filter_menu()

        elif choice == "5":
            generate_menu()

        elif choice == "6":
            rename_garments()

        elif choice == "7":
            clear_wardrobe()

        elif choice == "0":
            print("\n👋 До встречи!\n")
            break

        else:
            print("\n⚠️  Неверный выбор, попробуй снова.")


if __name__ == "__main__":
    main()
