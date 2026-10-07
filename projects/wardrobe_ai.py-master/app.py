import sys
from pathlib import Path
import streamlit as st

sys.path.append(str(Path(__file__).resolve().parent))

from src.db.repository import get_all_garments, filter_garments, delete_garment
from src.analysis.wardrobe_analyzer import analyze_wardrobe, rename_garments
from src.llm.outfit_generator import generate_outfits
from src.services.process_images_service import process_images
from src.db.schema import create_tables
from src.db.repository import get_all_garments, filter_garments, delete_garment, update_garment


create_tables()

# ──────────────────────────────────────────────
#  НАСТРОЙКИ
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Wardrobe AI",
    page_icon="👗",
    layout="wide"
)

st.markdown("""
<style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    h1 { font-size: 2rem; font-weight: 700; margin-bottom: 0; }
    h2 { font-size: 1.3rem; font-weight: 600; margin-top: 1.5rem; }
    .caption { color: #888; font-size: 0.85rem; }
    .card {
        background: #1a1a2e;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid #2a2a3e;
    }
    .tag {
        display: inline-block;
        background: #2a2a3e;
        border-radius: 6px;
        padding: 2px 10px;
        font-size: 0.78rem;
        margin-right: 4px;
        color: #ccc;
    }
    div[data-testid="stProgress"] > div { height: 6px; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


VALID_SUBTYPES = [
    "hoodie", "sweatshirt", "sweater", "zip-up", "t-shirt", "shirt", "blouse",
    "top", "long-sleeve", "jeans", "trousers", "sweatpants", "cargo-pants",
    "shorts", "skirt", "leggings", "dress", "jumpsuit", "jacket", "puffer",
    "coat", "blazer", "bomber", "denim-jacket", "leather-jacket", "fleece",
    "sneakers", "boots", "uggs", "heels", "sandals", "loafers", "platforms",
    "tote-bag", "backpack", "handbag", "clutch", "sunglasses", "glasses",
    "hat", "beanie", "scarf", "belt", "vest", "short-sleeve-shirt", "blazer",

]

VALID_CATEGORIES = ["top", "bottom", "dress", "outerwear", "shoes", "accessory"]
VALID_COLORS = ["black", "white", "grey", "beige", "cream", "brown", "red", "pink",
                "orange", "yellow", "green", "blue", "navy", "purple", "burgundy", "teal", "coral"]
VALID_STYLES = ["casual", "sporty", "minimal", "y2k", "downtown", "old_money", "romantic", "grunge"]
VALID_SEASONS = ["winter", "summer", "spring", "autumn", "all-season", "spring-summer", "autumn-winter"]



# ──────────────────────────────────────────────
#  ЗАГОЛОВОК
# ──────────────────────────────────────────────
st.markdown("# Wardrobe AI")
st.markdown('<p class="caption">Умный помощник по гардеробу</p>', unsafe_allow_html=True)
st.divider()

# ──────────────────────────────────────────────
#  ВКЛАДКИ
# ──────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "Загрузка",
    "Гардероб",
    "Аналитика",
    "Образы"
])

# ──────────────────────────────────────────────
#  СЛОВАРИ ЭМОДЗИ
# ──────────────────────────────────────────────
COLOR_EMOJI = {
    "black": "⚫", "white": "⚪", "grey": "🩶", "gray": "🩶",
    "red": "🔴", "blue": "🔵", "navy": "🔵", "green": "🟢",
    "yellow": "🟡", "orange": "🟠", "pink": "🩷", "purple": "🟣",
    "brown": "🟤", "beige": "🟤",
}
SEASON_EMOJI = {
    "spring": "🌸", "summer": "☀️", "autumn": "🍂", "winter": "❄️",
    "all-season": "🔄","spring-summer": "🌸☀️", "autumn-winter": "🍂❄️",

}
CATEGORY_EMOJI = {
    "top": "👕", "bottom": "👖", "dress": "👗", "outerwear": "🧥",
    "shoes": "👟", "accessories": "👜", "bag": "👜",
}


# ──────────────────────────────────────────────
#  ВКЛАДКА 1 — ЗАГРУЗКА
# ──────────────────────────────────────────────
with tab1:
    st.markdown("## Добавить новые вещи")
    st.markdown('<p class="caption">Загрузи фото — система определит тип, цвет и стиль автоматически.</p>', unsafe_allow_html=True)

    uploaded_files = st.file_uploader(
        "Выбери фото",
        type=["jpg", "jpeg", "png", "webp","heic"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    if uploaded_files:
        st.markdown(f'<p class="caption">Выбрано файлов: {len(uploaded_files)}</p>', unsafe_allow_html=True)

        if st.button("Обработать фото", type="primary", use_container_width=True):
            raw_dir = Path("data/raw_images")
            raw_dir.mkdir(exist_ok=True)

            for f in uploaded_files:
                with open(raw_dir / f.name, "wb") as out:
                    out.write(f.getbuffer())

            with st.spinner("Анализирую фото..."):
                results = process_images()

            if results:
                st.success(f"Добавлено вещей: {len(results)}")
                for r in results:
                    st.markdown(f"- **{r.get('subtype', '?')}** — {r.get('color', '?')}, {r.get('style', '?')}")
            else:
                st.info("Новых вещей не найдено — все фото уже в гардеробе.")


# ──────────────────────────────────────────────
#  ВКЛАДКА 2 — ГАРДЕРОБ
# ──────────────────────────────────────────────
with tab2:
    st.markdown("## Мой гардероб")

    with st.expander("Фильтры"):
        col1, col2, col3, col4 = st.columns(4)
        f_color    = col1.text_input("Цвет",      placeholder="black")
        f_style    = col2.text_input("Стиль",     placeholder="casual")
        f_season   = col3.text_input("Сезон",     placeholder="autumn")
        f_category = col4.text_input("Категория", placeholder="top")

    kwargs = {}
    if f_color:    kwargs["color"]    = f_color
    if f_style:    kwargs["style"]    = f_style
    if f_season:   kwargs["season"]   = f_season
    if f_category: kwargs["category"] = f_category

    garments = filter_garments(**kwargs) if kwargs else get_all_garments()


    if not garments:
        st.info("Гардероб пуст. Добавь фото на вкладке Загрузка.")
    else:
        st.markdown(f'<p class="caption">Всего вещей: {len(garments)}</p>', unsafe_allow_html=True)
        cols = st.columns(4)


        for idx, g in enumerate(garments):
            with cols[idx % 4]:
                with st.container():
                    image_path = Path(g.get("image_path", ""))
                    if image_path.exists():
                        st.image(str(image_path), use_container_width=True)
                    else:
                        st.markdown("*фото недоступно*")

                    name = g.get("notes") or image_path.stem or g.get("image_path", "—")
                    st.markdown(f"**{name}**")

                    color_e    = COLOR_EMOJI.get(g["color"], "🎨")
                    season_e   = SEASON_EMOJI.get(g["season"], "📅")
                    category_e = CATEGORY_EMOJI.get(g["category"], "👔")

                    st.markdown(
                        f'<span class="tag">{category_e} {g["category"]}</span>'
                        f'<span class="tag">{color_e} {g["color"]}</span>'
                        f'<span class="tag">{season_e} {g["season"]}</span>',
                        unsafe_allow_html=True
                    )
                    st.markdown("")
                    col_del, col_edit = st.columns(2)

                    with col_del:
                        if st.button("Удалить", key=f"del_{g['id']}", use_container_width=True):
                            delete_garment(g["id"])
                            st.rerun()

                    with col_edit:
                        if st.button("✏️ Изменить", key=f"edit_btn_{g['id']}", use_container_width=True):
                            st.session_state[f"editing_{g['id']}"] = True

                    if st.session_state.get(f"editing_{g['id']}"):
                        with st.form(key=f"form_{g['id']}"):
                            new_category = st.selectbox("Категория", VALID_CATEGORIES,
                                index=VALID_CATEGORIES.index(g["category"]) if g["category"] in VALID_CATEGORIES else 0)
                            new_subtype = st.selectbox("Подтип", VALID_SUBTYPES,
                                index=VALID_SUBTYPES.index(g["subtype"]) if g["subtype"] in VALID_SUBTYPES else 0)
                            new_color = st.selectbox("Цвет", VALID_COLORS,
                                index=VALID_COLORS.index(g["color"]) if g["color"] in VALID_COLORS else 0)
                            new_season = st.selectbox("Сезон", VALID_SEASONS,
                                                      index=VALID_SEASONS.index(g["season"]) if g[
                                                                                                    "season"] in VALID_SEASONS else 0)
                            new_name = st.text_input("Название", value=g.get("notes") or "")

                            saved = st.form_submit_button("💾 Сохранить", use_container_width=True)
                            if saved:
                                update_garment(g["id"], {
                                    "category": new_category,
                                    "subtype": new_subtype,
                                    "color": new_color,
                                    "style": g["style"],
                                    "season": new_season,
                                    "notes": new_name,
                                })

                                st.session_state[f"editing_{g['id']}"] = False
                                st.rerun()



# ──────────────────────────────────────────────
#  ВКЛАДКА 3 — АНАЛИТИКА
# ──────────────────────────────────────────────
with tab3:
    st.markdown("## Аналитика")

    report = analyze_wardrobe()

    if "error" in report:
        st.info(report["error"])
    else:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Вещей в гардеробе", report["total"])
        col2.metric("Основной цвет",     report["dominant_color"])
        col3.metric("Основной стиль",    report["dominant_style"])
        col4.metric("Основной сезон",    report["dominant_season"])

        st.divider()

        col_l, col_r = st.columns(2)

        with col_l:
            st.markdown("**Категории**")
            for k, v in report["categories"].items():
                e = CATEGORY_EMOJI.get(k, "👔")
                st.caption(f"{e} {k} — {v} шт.")
                st.progress(v / report["total"])

            st.markdown("**Цвета**")
            for k, v in report["colors"].items():
                e = COLOR_EMOJI.get(k, "🎨")
                st.caption(f"{e} {k} — {v} шт.")
                st.progress(v / report["total"])

        with col_r:
            st.markdown("**Низ 👖**")
            bottoms = {k: v for k, v in report["subtypes"].items()
                       if k in ["jeans", "trousers", "sweatpants", "cargo-pants",
                                 "shorts", "skirt", "leggings"]}
            if bottoms:
                for k, v in bottoms.items():
                    st.caption(f"👖 {k} — {v} шт.")
                    st.progress(v / report["total"])
            else:
                st.caption("нет данных")

            st.markdown("**Сезоны**")
            for k, v in report["seasons"].items():
                e = SEASON_EMOJI.get(k, "📅")
                st.caption(f"{e} {k} — {v} шт.")
                st.progress(v / report["total"])

            st.markdown("**Стили**")
            for k, v in report["styles"].items():
                st.caption(f"✨ {k} — {v} шт.")
                st.progress(v / report["total"])

        st.divider()

        st.markdown("**Советы**")
        for tip in report["tips"]:
            st.info(tip)

        if st.button("Переименовать вещи", use_container_width=False):
            rename_garments()
            st.success("Вещи переименованы!")
            st.rerun()


# ──────────────────────────────────────────────
#  ВКЛАДКА 4 — ОБРАЗЫ
# ──────────────────────────────────────────────
with tab4:
    st.markdown("## Генератор образов")

    all_garments = get_all_garments()

    st.markdown("### 📌 Составить образ вокруг вещи")
    st.caption("Выбери одну или несколько вещей — образ будет строиться вокруг них")

    pinned_items = []
    if all_garments:
        garment_labels = {
            f"{g.get('color', '')} {g.get('fit', '')} {g.get('subtype', '')} ({g.get('category', '')})".strip(): g
            for g in all_garments
        }
        selected_labels = st.multiselect(
            "Выбери вещи (необязательно)",
            options=list(garment_labels.keys()),
            placeholder="Оставь пустым для случайного образа",
            label_visibility="collapsed"
        )
        pinned_items = [garment_labels[label] for label in selected_labels]

        if pinned_items:
            st.markdown("**Закреплено:** " + " · ".join(
                f"📌 {g.get('color', '')} {g.get('subtype', '')}".strip()
                for g in pinned_items
            ))

    st.divider()

    occasion = st.text_input("Повод", placeholder="... на учебу, прогулка, свидание...")
    col1, col2 = st.columns(2)
    with col1:
        style = st.selectbox("Стиль", ["любой", "casual", "formal", "streetwear", "sport"])
    with col2:
        season = st.selectbox("Сезон", ["любой", "весна", "лето", "осень", "зима"])

    if st.button("Создать образ", type="primary", use_container_width=True):
        if not occasion:
            st.warning("Введи повод!")
        else:
            request = f"Create outfits for: {occasion}"
            if style != "любой":
                request += f", style: {style}"
            if season != "любой":
                request += f", season: {season}"

            with st.spinner("Генерирую образ..."):
                try:
                    result = generate_outfits(
                        user_request=request,
                        pinned_items=pinned_items if pinned_items else None
                    )
                    st.divider()
                    st.markdown(result)
                except ConnectionError:
                    st.error("LM Studio не запущен. Открой LM Studio → Developer → Start Server.")
