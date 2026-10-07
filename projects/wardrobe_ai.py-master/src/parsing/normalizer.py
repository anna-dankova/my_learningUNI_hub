import logging

logger = logging.getLogger(__name__)

# Фиксированные допустимые значения для каждого поля
VALID_VALUES = {
    "category":  {"top", "bottom", "shoes", "outerwear", "accessory", "dress", "unknown"},
"subtype": {
    "hoodie", "sweatshirt", "zip-up", "t-shirt", "shirt", "blouse",
    "top", "sweater", "long-sleeve",
    "jeans", "trousers", "sweatpants", "cargo-pants", "shorts", "skirt", "leggings",
    "dress", "jumpsuit",
    "jacket", "puffer", "coat", "blazer", "bomber", "denim-jacket",
    "leather-jacket", "fleece",
    "sneakers", "boots", "uggs", "heels", "sandals", "loafers", "platforms",
    "tote-bag", "backpack", "handbag", "clutch",
    "sunglasses", "glasses", "hat", "beanie", "scarf", "belt",
    "unknown"
    },
    "color": {
        "black", "white", "grey", "beige", "cream", "brown",
        "red", "pink", "orange", "yellow", "green", "blue", "purple",
        "navy", "olive", "khaki", "burgundy", "teal", "coral", "unknown"
    },
    "fit":       {"oversized", "slim", "relaxed", "regular", "unknown"},
    "season":    {"spring", "summer", "autumn", "winter", "all-season", "unknown"},
    "style":     {"casual", "y2k", "downtown", "old_money", "minimal", "sporty", "unknown"},
    "formality": {"low", "medium", "high", "unknown"},
}

# Синонимы → нормализованное значение
ALIASES = {
    # цвета
    "gray":         "grey",
    "charcoal":     "grey",
    "ivory":        "cream",
    "off-white":    "cream",
    "off white":    "cream",
    "dark blue":    "navy",
    "light blue":   "blue",
    "dark green":   "olive",
    "wine":         "burgundy",
    "maroon":       "burgundy",
    "lilac":        "purple",
    "violet":       "purple",
    "magenta":      "pink",
    "turquoise":    "teal",
    "rust":         "orange",
    "mustard":      "yellow",
    "sage":         "green",
    # fit
    "baggy":        "oversized",
    "loose":        "oversized",
    "tight":        "slim",
    "fitted":       "slim",
    "skinny":       "slim",
    "cropped":      "cropped",
    # сезон
    "fall":         "autumn",
    # стиль
    "minimalist":   "minimal",
    "street":       "downtown",
    "streetwear":   "downtown",
    "athletic":     "sporty",
    "sport":        "sporty",
    "preppy":       "old_money",
    "elegant":      "old_money",
    # subtype
    "tshirt":       "t-shirt",
    "t shirt":      "t-shirt",
    "hoody":        "hoodie",
    "pants":        "trousers",
    "trainers":     "sneakers",
    "purse":        "clutch",
    "handbag":      "handbag",
    "shades":       "sunglasses",
    "ugg":          "uggs",
    "puffer jacket":"puffer",
    "down jacket":  "puffer",
    "jean jacket":  "denim-jacket",
    "joggers":      "sweatpants",
    "trackpants":   "sweatpants",
}



def normalize_value(field: str, value: str) -> str:
    """
    Нормализует одно значение:
    1. Приводит к нижнему регистру
    2. Применяет алиасы (синонимы)
    3. Проверяет что значение входит в допустимые
    4. Если не входит → возвращает 'unknown'
    """
    if value is None:
        return None

    value = str(value).lower().strip()

    # Применяем алиас если есть
    value = ALIASES.get(value, value)

    # Проверяем допустимые значения (только для полей с ограничениями)
    if field in VALID_VALUES:
        if value not in VALID_VALUES[field]:
            logger.warning(f"⚠️ Неизвестное значение для '{field}': '{value}' → 'unknown'")
            return "unknown"

    return value


def normalize(parsed: dict) -> dict:
    """
    Принимает словарь после parser.py.
    Нормализует все поля к фиксированным классам.
    Возвращает финальный чистый словарь.
    """
    normalized = {}

    for field, value in parsed.items():
        # Поля которые нормализовать не нужно
        if field in ("description_raw", "notes", "image_path", "secondary_color"):
            normalized[field] = value
            continue

        normalized[field] = normalize_value(field, value)

    logger.info(f"✅ Нормализация завершена: {normalized}")
    return normalized


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    test_input = {
        "category":        "top",
        "subtype":         "hoody",       # алиас → hoodie
        "color":           "gray",        # алиас → grey
        "secondary_color": "blue",
        "fit":             "baggy",       # алиас → oversized
        "season":          "fall",        # алиас → autumn
        "style":           "streetwear",  # алиас → downtown
        "formality":       "low",
        "description_raw": "a gray baggy hoody",
        "notes":           None,
    }

    result = normalize(test_input)
    print("\nРезультат нормализации:")
    for k, v in result.items():
        print(f"  {k:20} → {v}")
