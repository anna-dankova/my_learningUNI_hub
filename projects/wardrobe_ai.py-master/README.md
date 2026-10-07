## README.md

Создай файл `README.md` в корне проекта и вставь:

```markdown
# 👗 Wardrobe AI

An intelligent wardrobe assistant that analyzes clothing photos using computer vision and generates stylish outfit suggestions via a local LLM.

## ✨ Features

- 📸 **Photo Analysis** — automatically recognizes clothing type, color, style, and season using BLIP
- 🗃 **Wardrobe Database** — stores all items in a local SQLite database
- ✨ **Outfit Generation** — creates personalized outfit suggestions via LM Studio (local LLM)
- 🔍 **Smart Filtering** — search by color, style, season, or category
- 📊 **Wardrobe Analytics** — detailed report with dominant colors, styles, and balance tips
- 🏷 **Auto Renaming** — renames items to readable names like `black hoodie`, `blue jeans`

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Computer Vision | BLIP (Salesforce) via HuggingFace Transformers |
| Local LLM | LM Studio + OpenAI-compatible API |
| Database | SQLite |
| Language | Python 3.11+ |
| Interface | CLI (Streamlit UI in progress) |

## 📁 Project Structure

```
wardrobe-ai/
├── data/
│   ├── raw_images/         # Drop new photos here
│   └── processed_images/   # Auto-moved after processing
├── src/
│   ├── ingestion/          # Image loading & validation
│   ├── vision/             # BLIP captioning & attribute extraction
│   ├── parsing/            # Text parsing & normalization
│   ├── db/                 # SQLite schema & repository
│   ├── llm/                # LM Studio client & outfit generator
│   ├── analysis/           # Wardrobe analyzer & renaming
│   └── services/           # Processing pipeline
├── prompts/                # LLM prompt templates
├── tests/                  # Pytest test suite
├── main.py                 # Entry point
└── requirements.txt
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/wardrobe-ai.git
cd wardrobe-ai
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up LM Studio
- Download [LM Studio](https://lmstudio.ai/)
- Load any chat model (e.g. Mistral, LLaMA)
- Go to **Developer → Start Server**

### 5. Run the app
```bash
python main.py
```

## 📋 Menu Options

```
1 — 📸 Process new photos
2 — 👗 Show wardrobe
3 — 📊 Wardrobe analytics
4 — 🔍 Filter items
5 — ✨ Generate outfit
6 — 🏷  Rename items
7 — 🗑  Clear wardrobe
0 — 🚪 Exit
```

## ⚙️ Requirements

- Python 3.11+
- LM Studio running locally
- ~4GB RAM for BLIP base model
```

***

## Как загрузить через PyCharm

### Шаг 1 — Создай репозиторий на GitHub
- Зайди на **github.com** → **New repository**
- Название: `wardrobe-ai`
- Поставь **Public**
- **НЕ** ставь галочку на README (у нас свой)
- Нажми **Create repository**

### Шаг 2 — Подключи через PyCharm
- В PyCharm: **VCS → Enable Version Control Integration → Git → OK**

### Шаг 3 — Проверь `.gitignore`
Убедись что в `.gitignore` есть эти строки (чтобы не загружать лишнее):
```
.venv/
__pycache__/
*.pyc
.env
data/raw_images/*
data/processed_images/*
*.db
```

### Шаг 4 — Первый коммит
- В PyCharm внизу нажми вкладку **Git**
- **VCS → Commit** (или `Ctrl+K`)
- Отметь все файлы галочкой
- Напиши сообщение: `Initial commit — Wardrobe AI MVP`
- Нажми **Commit**

### Шаг 5 — Push на GitHub
- **VCS → Git → Push** (или `Ctrl+Shift+K`)
- Нажми **Define remote** → вставь ссылку с GitHub (она вида `https://github.com/твой_ник/wardrobe-ai.git`)
- Нажми **Push**

Готово — проект на GitHub! 🚀
