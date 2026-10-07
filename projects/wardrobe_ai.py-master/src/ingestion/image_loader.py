import logging
from pathlib import Path
from PIL import Image

# Настройка логгера для этого модуля
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# Разрешённые форматы
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def is_valid_image(path: Path) -> bool:
    """Проверяет что файл не повреждён через PIL."""
    try:
        with Image.open(path) as img:
            img.verify()  # Проверяет структуру файла без полной загрузки
        # verify() требует повторного открытия для дальнейшей работы
        with Image.open(path) as img:
            img.load()   # Финальная проверка — загружаем пиксели
        return True
    except Exception as e:
        logger.warning(f"Повреждённый файл: {path.name} — {e}")
        return False


def load_images(raw_images_dir: str = "data/raw_images") -> list[Path]:
    """
    Читает все изображения из папки raw_images_dir.
    Возвращает список Path к валидным изображениям.
    """
    folder = Path(raw_images_dir)

    if not folder.exists():
        logger.error(f"Папка не найдена: {folder.resolve()}")
        return []

    all_files = list(folder.iterdir())
    valid_paths = []
    skipped = []

    for file in all_files:
        if not file.is_file():
            continue

        # Проверка расширения (case-insensitive: .JPG тоже пройдёт)
        if file.suffix.lower() not in ALLOWED_EXTENSIONS:
            skipped.append((file.name, "неверный формат"))
            continue

        # Проверка что файл не повреждён
        if not is_valid_image(file):
            skipped.append((file.name, "повреждён"))
            continue

        valid_paths.append(file)

    # Логируем результат
    logger.info(f"✅ Найдено валидных фото: {len(valid_paths)}")

    if skipped:
        logger.info(f"⏭ Пропущено файлов: {len(skipped)}")
        for name, reason in skipped:
            logger.info(f"   — {name}: {reason}")

    return valid_paths


if __name__ == "__main__":
    images = load_images()
    for img_path in images:
        print(img_path)
