import logging
import requests
import json

logger = logging.getLogger(__name__)

BASE_URL = "http://localhost:1234/v1"
DEFAULT_MODEL = "local-model"


def is_server_running() -> bool:
    try:
        response = requests.get(f"{BASE_URL}/models", timeout=5)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False


def get_available_models() -> list[str]:
    try:
        response = requests.get(f"{BASE_URL}/models", timeout=5)
        data = response.json()
        models = [m["id"] for m in data.get("data", [])]
        return models
    except Exception as e:
        logger.error(f"Ошибка получения моделей: {e}")
        return []


def chat(
    prompt: str,
    system_prompt: str = "You are a helpful fashion assistant.",
    temperature: float = 0.7,
    max_tokens: int = 1024,
) -> str:
    if not is_server_running():
        raise ConnectionError(
            "❌ LM Studio сервер не запущен!\n"
            "Открой LM Studio → вкладка Developer → Start Server"
        )

    payload = {
        "model": DEFAULT_MODEL,
        "messages": [
            {"role": "user", "content": f"{system_prompt}\n\n{prompt}"},
        ],

        "temperature": temperature,
        "max_tokens":  max_tokens,
        "stream": False,
    }

    logger.info("📤 Отправляем запрос в LLM...")

    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        timeout=120,
    )

    if response.status_code != 200:
        raise Exception(f"Ошибка LM Studio: {response.status_code} — {response.text}")

    result = response.json()
    answer = result["choices"][0]["message"]["content"]

    logger.info(f"📥 Ответ получен ({len(answer)} символов)")
    return answer.strip()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    print("🔍 Проверяем соединение с LM Studio...")

    if not is_server_running():
        print("❌ Сервер не запущен. Открой LM Studio и запусти сервер.")
        exit(1)

    models = get_available_models()
    print(f"✅ Сервер работает! Доступные модели: {models}")

    print("\n📤 Отправляем тестовый запрос...")
    answer = chat(
        prompt="Name 3 popular casual clothing styles in one sentence each.",
        system_prompt="You are a fashion expert. Be concise."
    )

    print(f"\n🤖 Ответ модели:\n{answer}")
