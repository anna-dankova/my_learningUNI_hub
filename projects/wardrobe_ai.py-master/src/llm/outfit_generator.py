import logging
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from src.db.repository import get_all_garments, add_outfit
from src.llm.client import chat, is_server_running

logger = logging.getLogger(__name__)

PROMPT_PATH = Path("prompts/generate_outfits.txt")


def load_prompt_template() -> str:
    if not PROMPT_PATH.exists():
        raise FileNotFoundError(f"Файл промпта не найден: {PROMPT_PATH}")
    return PROMPT_PATH.read_text(encoding="utf-8")


def format_wardrobe_for_prompt(garments: list) -> str:
    if not garments:
        return "No items in wardrobe."
    lines = []
    for i, item in enumerate(garments, start=1):
        # Берём notes как имя — это то как вещь сохранена в гардеробе
        name = item.get("notes", "").strip()
        # Если notes пустой — собираем из атрибутов как fallback
        if not name:
            parts = [
                item.get("color", "unknown"),
                item.get("fit", ""),
                item.get("subtype", "unknown"),
            ]
            name = " ".join(p for p in parts if p and p != "unknown")
        meta = ", ".join(filter(None, [
            item.get("style"),
            item.get("season"),
            item.get("category"),
        ]))
        lines.append(f"{i}. {name} ({meta})")
    return "\n".join(lines)



def generate_outfits(
    user_request: str = "Create stylish everyday outfits",
    pinned_items: list = None
) -> str:
    if not is_server_running():
        raise ConnectionError(
            "❌ LM Studio не запущен!\nОткрой LM Studio → Developer → Start Server"
        )

    logger.info("👗 Загружаем гардероб из базы данных...")
    garments = get_all_garments()

    if not garments:
        logger.warning("❌ Гардероб пуст.")
        return ""

    logger.info(f"Найдено вещей: {len(garments)}")
    wardrobe_text = format_wardrobe_for_prompt(garments)
    logger.info(f"📋 Гардероб для промпта:\n{wardrobe_text}")

    pinned_note = ""
    if pinned_items:
        pinned_names = "\n".join(
            f"- {g.get('color', '')} {g.get('fit', '')} {g.get('subtype', '')}".strip()
            for g in pinned_items
        )
        pinned_note = f"\n\n⚠️ PINNED ITEMS — you MUST include ALL of these in every outfit:\n{pinned_names}\n"

    template = load_prompt_template()
    prompt = template.format(
        wardrobe=wardrobe_text,
        user_request=user_request + pinned_note
    )

    logger.info(f"📋 Промпт отправленный в LLM:\n{prompt}")
    result = chat(
        prompt=prompt,
        system_prompt="You are a professional fashion stylist. Be creative and specific. Always follow all combination rules.",
        temperature=0.8,
        max_tokens=2048,
    )

    outfit_id = add_outfit(query_text=user_request, result_text=result)
    logger.info(f"💾 Образы сохранены в БД с id: {outfit_id}")

    return result


def print_outfits(result: str):
    print("\n" + "=" * 60)
    print("✨ СГЕНЕРИРОВАННЫЕ ОБРАЗЫ")
    print("=" * 60)
    print(result)
    print("=" * 60)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("👗 Wardrobe AI — Генератор образов")
    print("-" * 40)
    user_request = input("Введите запрос (или Enter для базового): ").strip()
    if not user_request:
        user_request = "Create 5 stylish casual everyday outfits"
    try:
        result = generate_outfits(user_request)
        print_outfits(result)
    except ConnectionError as e:
        print(e)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
