import logging
import sys
import re
from pathlib import Path
import shutil


sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from src.ingestion.image_loader import load_images
from src.vision.captioner import generate_caption
from src.vision.attribute_extractor import extract_attributes
from src.parsing.parser import parse_caption
from src.parsing.normalizer import normalize
from src.db.repository import add_garment, garment_exists, get_all_garments



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# ──────────────────────────────────────────────
#  ПОДСКАЗКИ ИЗ ИМЕНИ ФАЙЛА
# ──────────────────────────────────────────────

FILENAME_HINTS = {
    "hoodie": "hoodie", "hood": "hoodie",
    "sweatshirt": "sweatshirt",
    "sweater": "sweater",
    "zip": "zip-up",
    "tshirt": "t-shirt", "tee": "t-shirt",
    "shirt": "shirt",
    "top": "top", "crop": "top",
    "blouse": "blouse",
    "jeans": "jeans", "denim": "jeans",
    "trousers": "trousers", "pants": "trousers",
    "sweatpants": "sweatpants", "joggers": "sweatpants",
    "shorts": "shorts",
    "skirt": "skirt",
    "dress": "dress",
    "jumpsuit": "jumpsuit",
    "jacket": "jacket",
    "puffer": "puffer",
    "coat": "coat",
    "blazer": "blazer",
    "bomber": "bomber",
    "denim_jacket": "denim-jacket", "jeansjacket": "denim-jacket",
    "leather": "leather-jacket",
    "fleece": "fleece",
    "sneakers": "sneakers", "snkrs": "sneakers",
    "boots": "boots",
    "ugg": "uggs", "uggs": "uggs",
    "heels": "heels",
    "sandals": "sandals",
    "loafers": "loafers",
    "bag": "handbag", "handbag": "handbag",
    "tote": "tote-bag",
    "backpack": "backpack",
    "clutch": "clutch",
    "sunglasses": "sunglasses", "glasses": "glasses",
    "hat": "hat", "cap": "hat",
    "beanie": "beanie",
    "scarf": "scarf",
    "belt": "belt",
}


def extract_hint_from_filename(filename: str) -> str:
    """
    Извлекает подсказку из имени файла.
    'hoodie1.jpg' → 'hoodie'
    'jeans_blue.jpg' → 'jeans'
    """
    name = filename.lower()
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        name = name.replace(ext, "")
    name = name.replace("_", " ").replace("-", " ")
    name = re.sub(r'\d+', '', name).strip()

    for keyword, hint in FILENAME_HINTS.items():
        if keyword in name:
            return hint
    return ""


# ──────────────────────────────────────────────
#  PIPELINE
# ──────────────────────────────────────────────

def process_images(raw_images_dir: str = "data/raw_images") -> list[dict]:
    logger.info("=" * 50)
    logger.info("🚀 Запуск pipeline обработки изображений")
    logger.info("=" * 50)

    logger.info("📁 Шаг 1: Загрузка изображений...")
    image_paths = load_images(raw_images_dir)

    if not image_paths:
        logger.warning("❌ Нет изображений для обработки.")
        return []

    logger.info(f"   Найдено фото: {len(image_paths)}")

    results = []
    errors = []

    for i, image_path in enumerate(image_paths, start=1):
        logger.info("-" * 40)
        logger.info(f"🖼 Обрабатываем [{i}/{len(image_paths)}]: {image_path.name}")

        if garment_exists(str(image_path)):
            logger.info(f"⏭ Пропускаю (уже в БД): {image_path.name}")
            continue

        try:
            # Шаг 2: BLIP описывает фото
            logger.info("   🧠 Генерируем описание через BLIP...")
            caption = generate_caption(image_path)
            logger.info(f"   📝 Описание BLIP: {caption}")

            # Шаг 2.5: Подсказка из имени файла
            filename_hint = extract_hint_from_filename(image_path.name)
            if filename_hint:
                caption = f"{filename_hint}, {caption}"
                logger.info(f"   💡 Подсказка из имени: {filename_hint} → итог: {caption}")

            # Шаг 3: Извлекаем атрибуты
            logger.info("   🏷 Извлекаем атрибуты...")
            raw_attrs = extract_attributes(caption)

            # Шаг 4: Парсим
            logger.info("   🔍 Парсинг...")
            parsed = parse_caption(raw_attrs)

            # Шаг 5: Нормализуем
            logger.info("   ✨ Нормализация...")
            clean = normalize(parsed)

            # Перемещаем фото СНАЧАЛА
            processed_dir = Path("data/processed_images")
            processed_dir.mkdir(exist_ok=True)
            new_path = processed_dir / image_path.name
            shutil.move(str(image_path), str(new_path))
            logger.info(f"   📦 Перемещено в processed_images: {image_path.name}")

            # Шаг 6: Добавляем ПРАВИЛЬНЫЙ путь (уже после перемещения)
            clean["image_path"] = str(new_path)

            # Шаг 7: Сохраняем в БД
            logger.info("   💾 Сохраняем в базу...")
            new_id = add_garment(clean)
            logger.info(f"   ✅ Сохранено с id: {new_id}")

            results.append({"id": new_id, **clean})



        except Exception as e:
            logger.error(f"   ❌ Ошибка: {image_path.name}: {e}")
            errors.append(image_path.name)
            continue

    logger.info("=" * 50)
    logger.info(f"🎯 Готово! Обработано: {len(results)}, ошибок: {len(errors)}")
    logger.info("=" * 50)

    return results


def print_wardrobe():
    items = get_all_garments()
    if not items:
        print("👗 Гардероб пуст.")
        return

    print(f"\n{'=' * 60}")
    print(f"👗 ГАРДЕРОБ — всего вещей: {len(items)}")
    print(f"{'=' * 60}")

    for item in items:
        print(f"\n[{item['id']}] {Path(item['image_path']).name}")
        print(f"  Категория:    {item['category']} / {item['subtype']}")
        print(f"  Цвет:         {item['color']}", end="")
        if item['secondary_color']:
            print(f" + {item['secondary_color']}", end="")
        print()
        print(f"  Фит:          {item['fit']}")
        print(f"  Сезон:        {item['season']}")
        print(f"  Стиль:        {item['style']}")
        print(f"  Формальность: {item['formality']}")
        print(f"  Описание:     {item['description_raw']}")


if __name__ == "__main__":
    process_images()
    print_wardrobe()
