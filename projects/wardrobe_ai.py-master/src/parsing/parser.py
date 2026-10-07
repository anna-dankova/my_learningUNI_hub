import logging

logger = logging.getLogger(__name__)

# Обязательные поля которые должны быть в каждой вещи
REQUIRED_FIELDS = [
    "category", "subtype", "color", "secondary_color",
    "fit", "season", "style", "formality", "description_raw", "notes"
]


def parse_caption(raw_attributes: dict) -> dict:
    """
    Принимает сырой словарь от attribute_extractor.
    Проверяет наличие всех обязательных полей.
    Если поля нет — подставляет None или 'unknown'.
    Возвращает чистый словарь готовый для записи в БД.
    """
    parsed = {}

    for field in REQUIRED_FIELDS:
        value = raw_attributes.get(field)

        # Пустая строка тоже считается отсутствием значения
        if value == "" or value is None:
            if field == "secondary_color" or field == "notes":
                parsed[field] = None  # эти поля могут быть пустыми
            else:
                parsed[field] = "unknown"
                logger.warning(f"⚠️ Поле '{field}' отсутствует → поставлено 'unknown'")
        else:
            parsed[field] = value

    logger.info(f"✅ Парсинг завершён: {parsed}")
    return parsed


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Тест с неполным словарём
    test_input = {
        "category": "top",
        "color": "white",
        "description_raw": "a white shirt with blue flowers on it",
    }

    result = parse_caption(test_input)
    print("\nРезультат парсинга:")
    for k, v in result.items():
        print(f"  {k:20} → {v}")
