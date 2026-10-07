import re
import logging

logger = logging.getLogger(__name__)

# ──────────────────────────────────────────────────────────────
#  КАТЕГОРИИ + ПОДТИПЫ
# ──────────────────────────────────────────────────────────────

CATEGORIES = {
    "top": [
        "shirt", "t-shirt", "tshirt", "tee", "blouse", "top", "crop top",
        "tank top", "tank", "camisole", "tube top",
        "hoodie", "hoody", "sweatshirt", "sweater", "jumper", "pullover",
        "turtleneck", "polo", "zip", "zip-up", "half-zip",
        "knit", "knitwear", "ribbed top", "long sleeve",
        "shirt", "short sleeve shirt", "short sleeve",

    ],
    "bottom": [
        "pants", "jeans", "trousers", "shorts", "skirt", "leggings",
        "sweatpants", "joggers", "cargo", "cargo pants", "culottes",
        "wide leg", "flare", "straight leg", "mini skirt", "maxi skirt",
        "midi skirt", "long shorts", "bermuda",
    ],
    "dress": [
        "dress", "gown", "jumpsuit", "romper", "playsuit",
        "mini dress", "midi dress", "maxi dress", "sundress",
    ],
    "outerwear": [
        "jacket", "coat", "blazer", "parka", "windbreaker", "raincoat",
        "bomber", "trench coat", "trench", "duster", "overcoat",
        "denim jacket", "jean jacket", "leather jacket",
        "padded jacket", "puffer", "puffer jacket", "down jacket",
        "fleece", "vest", "gilet",
        "ugg coat", "wool coat", "longline coat",
        "blazer", "suit jacket", "tailored jacket",
        "tailored vest", "waistcoat",


    ],
    "shoes": [
        "sneakers", "sneaker", "trainers", "shoes", "boots", "boot",
        "heels", "heel", "sandals", "sandal", "loafers", "loafer",
        "mules", "mule", "oxfords", "oxford", "platforms", "platform",
        "slippers", "slides", "slide",
        "uggs", "ugg", "ugg boots",
        "converse", "vans", "nike", "adidas",
        "ankle boots", "chelsea boots", "knee-high boots",
    ],
    "accessory": [
        # сумки
        "bag", "bags", "handbag", "tote", "tote bag", "purse",
        "backpack", "clutch", "shoulder bag", "crossbody bag",
        "mini bag", "bucket bag", "hobo bag", "satchel",
        # очки
        "sunglasses", "glasses", "eyewear", "shades",
        "cat-eye glasses", "round glasses", "square glasses",
        # головные уборы
        "hat", "cap", "beanie", "beret", "bucket hat",
        "baseball cap", "snapback",
        # остальное
        "scarf", "belt", "gloves", "socks", "watch",
        "jewelry", "necklace", "bracelet", "earrings", "ring",
    ],
}

# ──────────────────────────────────────────────────────────────
#  ПОДТИПЫ — точные названия для БД
# ──────────────────────────────────────────────────────────────

SUBTYPES = {
    # топы
    "hoodie":      ["hoodie", "hoody", "hooded sweatshirt", "hooded sweater",
                    "hoodie sweater", "hooded top", "hood"],
    "sweatshirt":  ["sweatshirt", "crewneck", "crew neck", "pullover sweatshirt"],
    "sweater":     ["sweater", "jumper", "pullover", "knit", "knitwear",
                    "turtleneck", "wool sweater", "knitted"],
    "zip-up":      ["zip", "zip-up", "half-zip", "zipup"],
    "t-shirt":     ["t-shirt", "tshirt", "tee", "t shirt"],
    "shirt":       ["shirt", "button-up", "button down", "oxford shirt"],
    "blouse":      ["blouse"],
    "top":         ["top", "crop top", "tank top", "tank", "camisole", "tube top"],
    "long-sleeve": ["long sleeve", "longsleeve"],
    # низ
    "jeans":       ["jeans", "denim pants", "denim trousers"],
    "trousers":    ["trousers", "pants", "slacks", "wide leg", "straight leg", "flare"],
    "sweatpants":  ["sweatpants", "joggers", "trackpants", "track pants"],
    "cargo-pants": ["cargo", "cargo pants"],
    "shorts":      ["shorts", "long shorts", "bermuda", "mini shorts"],
    "skirt":       ["skirt", "mini skirt", "midi skirt", "maxi skirt", "culottes"],
    "leggings":    ["leggings"],
    # платья
    "dress":       ["dress", "mini dress", "midi dress", "maxi dress", "sundress"],
    "jumpsuit":    ["jumpsuit", "romper", "playsuit"],
    # верх
    "jacket":      ["jacket", "windbreaker", "raincoat", "padded jacket"],
    "puffer":      ["puffer", "puffer jacket", "down jacket", "quilted jacket"],
    "coat":        ["coat", "overcoat", "wool coat", "longline coat", "trench coat", "trench", "duster"],
    "blazer":      ["blazer"],
    "bomber":      ["bomber", "bomber jacket"],
    "denim-jacket":["denim jacket", "jean jacket", "jeans jacket"],
    "leather-jacket": ["leather jacket"],
    "fleece":      ["fleece", "gilet", "vest"],
    # обувь
    "sneakers":    ["sneakers", "sneaker", "trainers", "converse", "vans", "nike shoes", "adidas shoes"],
    "boots":       ["boots", "boot", "ankle boots", "chelsea boots", "knee-high boots"],
    "uggs":        ["uggs", "ugg", "ugg boots"],
    "heels":       ["heels", "heel", "pumps", "stilettos"],
    "sandals":     ["sandals", "sandal", "slides", "slide", "mules", "mule"],
    "loafers":     ["loafers", "loafer", "oxfords", "oxford"],
    "platforms":   ["platforms", "platform shoes", "platform boots"],
    # аксессуары
    "tote-bag":    ["tote", "tote bag"],
    "backpack":    ["backpack"],
    "handbag":     ["handbag", "shoulder bag", "crossbody bag", "mini bag", "bucket bag", "satchel", "hobo bag"],
    "clutch":      ["clutch", "purse"],
    "sunglasses":  ["sunglasses", "shades", "cat-eye glasses", "round glasses", "square glasses"],
    "glasses":     ["glasses", "eyewear", "spectacles"],
    "hat":         ["hat", "cap", "baseball cap", "snapback", "bucket hat"],
    "beanie":      ["beanie", "beret"],
    "scarf":       ["scarf"],
    "belt":        ["belt"],
    "vest": ["vest", "tailored vest", "waistcoat", "gilet"],
    "short-sleeve-shirt": ["short sleeve shirt", "short sleeve", "camp shirt"],

}

# ──────────────────────────────────────────────────────────────
#  ЦВЕТА — с учётом что у тебя много белого, серого, чёрного
# ──────────────────────────────────────────────────────────────

COLORS = {
    # основные нейтральные (твои главные)
    "black":   ["black", "jet black", "all black", "noir"],
    "white":   ["white", "bright white", "pure white", "snow white"],
    "grey":    ["grey", "gray", "light grey", "dark grey", "charcoal", "slate", "ash"],
    # нейтральные тёплые
    "beige":   ["beige", "sand", "stone", "camel", "khaki", "tan"],
    "cream":   ["cream", "ivory", "off-white", "off white", "ecru", "vanilla"],
    "brown":   ["brown", "chocolate", "coffee", "mocha", "caramel", "cognac"],
    # яркие
    "red":     ["red", "scarlet", "crimson"],
    "pink":    ["pink", "blush", "rose", "mauve", "dusty pink", "light pink", "hot pink", "fuchsia"],
    "orange":  ["orange", "rust", "terracotta", "amber", "peach"],
    "yellow":  ["yellow", "mustard", "lemon", "gold"],
    "green":   ["green", "olive", "sage", "mint", "forest green", "emerald", "lime"],
    "blue":    ["blue", "light blue", "sky blue", "cobalt", "cornflower", "denim blue"],
    "navy":    ["navy", "dark blue", "midnight blue", "indigo"],
    "purple":  ["purple", "violet", "lilac", "lavender", "plum"],
    "burgundy":["burgundy", "wine", "maroon", "oxblood", "dark red"],
    "teal":    ["teal", "turquoise", "aqua", "cyan"],
    "coral":   ["coral", "salmon"],
}

# ──────────────────────────────────────────────────────────────
#  ФИТ
# ──────────────────────────────────────────────────────────────

FITS = {
    "oversized": ["oversized", "baggy", "loose", "big", "large", "wide", "boxy", "chunky"],
    "slim":      ["slim", "tight", "fitted", "skinny", "form-fitting", "body-con", "bodycon"],
    "relaxed":   ["relaxed", "comfortable", "easy", "soft"],
    "regular":   ["regular", "classic", "normal", "straight", "standard"],
    "cropped":   ["cropped", "crop", "short"],
}

# ──────────────────────────────────────────────────────────────
#  СЕЗОН
# ──────────────────────────────────────────────────────────────

SEASONS = {
    "winter":     ["winter", "wool", "fur", "heavy", "thick", "warm", "knit", "padded", "down", "ugg"],
    "summer":     ["summer", "light", "thin", "sleeveless", "short sleeve", "linen", "cotton", "sundress"],
    "spring":     ["spring", "trench", "light jacket", "floral", "pastel"],
    "autumn":     ["autumn", "fall", "layered", "denim jacket", "bomber", "sweater", "hoodie", "boots"],
    "all-season": ["all-season", "versatile", "basic", "classic", "everyday"],
    "spring-summer": ["light layering", "transitional", "spring summer"],
    "autumn-winter": ["heavy layering", "cold weather", "autumn winter", "fall winter"],
}


# ──────────────────────────────────────────────────────────────
#  СТИЛЬ
# ──────────────────────────────────────────────────────────────

STYLES = {
    "casual":    ["casual", "everyday", "simple", "basic", "relaxed", "comfortable", "effortless"],
    "sporty":    ["sport", "athletic", "gym", "running", "workout", "active", "performance"],
    "minimal":   ["minimal", "minimalist", "clean", "simple", "monochrome", "monochromatic"],
    "y2k":       ["y2k", "2000s", "butterfly", "low rise", "rhinestone", "metallic", "glitter"],
    "downtown":  ["downtown", "urban", "street", "streetwear", "skate", "grunge", "edgy"],
    "old_money": ["old money", "preppy", "classic", "elegant", "polo", "tailored", "sophisticated"],
    "romantic":  ["romantic", "floral", "lace", "feminine", "delicate", "ruffle"],
    "grunge":    ["grunge", "dark", "punk", "rock", "distressed", "ripped"],
}

# ──────────────────────────────────────────────────────────────
#  ФОРМАЛЬНОСТЬ
# ──────────────────────────────────────────────────────────────

FORMALITY = {
    "low":    ["casual", "sporty", "gym", "hoodie", "sneakers", "jeans", "sweatpants",
               "joggers", "tee", "t-shirt", "shorts", "ugg"],
    "medium": ["smart", "office", "neat", "blazer", "trousers", "blouse", "loafers",
               "shirt", "skirt", "dress", "coat"],
    "high":   ["formal", "elegant", "suit", "gown", "heels", "dress shirt", "tailored",
               "evening", "cocktail"],
}

# Значения по умолчанию на основе подтипа
SUBTYPE_DEFAULTS = {
    # ── ТОПЫ ────────────────────────────────────────────
    "hoodie":       {"fit": "oversized", "season": "all-season", "style": "casual", "formality": "low"},
    "sweatshirt":   {"fit": "oversized", "season": "all-season", "style": "casual", "formality": "low"},
    "zip-up":       {"fit": "regular",   "season": "all-season", "style": "casual", "formality": "low"},
    "t-shirt":      {"fit": "regular",   "season": "summer",     "style": "casual", "formality": "low"},
    "shirt":        {"fit": "regular",   "season": "all-season", "style": "casual", "formality": "medium"},
    "sweater":      {"fit": "oversized", "season": "all-season", "style": "casual", "formality": "medium"},
    "top":          {"fit": "regular",   "season": "summer",     "style": "casual", "formality": "low"},
    "blouse":       {"fit": "regular",   "season": "all-season", "style": "casual", "formality": "medium"},
    "long-sleeve":  {"fit": "regular",   "season": "all-season", "style": "casual", "formality": "low"},

    # ── НИЗ ─────────────────────────────────────────────
    "jeans":        {"fit": "oversized", "season": "all-season", "style": "casual", "formality": "low"},
    "trousers":     {"fit": "regular",   "season": "all-season", "style": "casual", "formality": "medium"},
    "sweatpants":   {"fit": "oversized", "season": "all-season", "style": "sporty", "formality": "low"},
    "cargo-pants":  {"fit": "oversized", "season": "all-season", "style": "downtown", "formality": "low"},
    "shorts":       {"fit": "regular",   "season": "summer",     "style": "casual", "formality": "low"},
    "skirt":        {"fit": "regular",   "season": "spring",     "style": "casual", "formality": "medium"},
    "leggings":     {"fit": "slim",      "season": "all-season", "style": "sporty", "formality": "low"},

    # ── ПЛАТЬЯ ──────────────────────────────────────────
    "dress":        {"fit": "regular",   "season": "summer",     "style": "casual", "formality": "medium"},
    "jumpsuit":     {"fit": "regular",   "season": "summer",     "style": "casual", "formality": "medium"},

    # ── ВЕРХ ────────────────────────────────────────────
    "jacket":       {"fit": "regular",   "season": "autumn",     "style": "casual",   "formality": "medium"},
    "puffer":       {"fit": "oversized", "season": "winter",     "style": "casual",   "formality": "low"},
    "coat":         {"fit": "regular",   "season": "winter",     "style": "minimal",  "formality": "medium"},
    "blazer":       {"fit": "regular",   "season": "all-season", "style": "old_money","formality": "high"},
    "bomber":       {"fit": "regular",   "season": "autumn",     "style": "downtown", "formality": "low"},
    "denim-jacket": {"fit": "regular",   "season": "spring",     "style": "casual",   "formality": "low"},
    "leather-jacket":{"fit": "regular",  "season": "autumn",     "style": "downtown", "formality": "low"},
    "fleece":       {"fit": "oversized", "season": "autumn",     "style": "casual",   "formality": "low"},

    # ── ОБУВЬ ───────────────────────────────────────────
    "sneakers":     {"fit": "regular",   "season": "all-season", "style": "casual",   "formality": "low"},
    "boots":        {"fit": "regular",   "season": "autumn",     "style": "casual",   "formality": "medium"},
    "uggs":         {"fit": "regular",   "season": "winter",     "style": "casual",   "formality": "low"},
    "heels":        {"fit": "regular",   "season": "all-season", "style": "old_money","formality": "high"},
    "sandals":      {"fit": "regular",   "season": "summer",     "style": "casual",   "formality": "low"},
    "loafers":      {"fit": "regular",   "season": "all-season", "style": "old_money","formality": "medium"},
    "platforms":    {"fit": "regular",   "season": "all-season", "style": "y2k",      "formality": "medium"},

    # ── АКСЕССУАРЫ ──────────────────────────────────────
    "tote-bag":     {"fit": "regular",   "season": "all-season", "style": "minimal",  "formality": "low"},
    "backpack":     {"fit": "regular",   "season": "all-season", "style": "casual",   "formality": "low"},
    "handbag":      {"fit": "regular",   "season": "all-season", "style": "casual",   "formality": "medium"},
    "clutch":       {"fit": "regular",   "season": "all-season", "style": "old_money","formality": "high"},
    "sunglasses":   {"fit": "regular",   "season": "summer",     "style": "casual",   "formality": "low"},
    "glasses":      {"fit": "regular",   "season": "all-season", "style": "minimal",  "formality": "medium"},
    "hat":          {"fit": "regular",   "season": "summer",     "style": "casual",   "formality": "low"},
    "beanie":       {"fit": "regular",   "season": "winter",     "style": "casual",   "formality": "low"},
    "scarf":        {"fit": "regular",   "season": "winter",     "style": "casual",   "formality": "low"},
    "belt":         {"fit": "regular",   "season": "all-season", "style": "casual",   "formality": "medium"},
}



def apply_defaults(result: dict) -> dict:
    """Заполняет unknown поля на основе подтипа вещи."""


    subtype = result.get("subtype", "unknown")
    caption = result.get("description_raw", "").lower()

    # Если определил как sweater но в описании есть hood → это худи
    if subtype == "sweater" and "hood" in caption:
        result["subtype"] = "hoodie"
        subtype = "hoodie"

    # Если определил как sweater но есть zip → это зипка
    if subtype == "sweater" and ("zip" in caption or "zipper" in caption):
        result["subtype"] = "zip-up"
        subtype = "zip-up"

    defaults = SUBTYPE_DEFAULTS.get(subtype, {})
    for field, default_value in defaults.items():
        if result.get(field) == "unknown":
            result[field] = default_value

    # Цвет по умолчанию
    if subtype == "jeans" and result.get("color") == "unknown":
        result["color"] = "blue"
    if subtype in ("hoodie", "sweatshirt") and result.get("color") == "unknown":
        result["color"] = "grey"

    return result

# ──────────────────────────────────────────────────────────────
#  ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ──────────────────────────────────────────────────────────────

def _find_category(text: str) -> str:
    text = text.lower()
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in text:
                return category
    return "unknown"


def _find_subtype(text: str) -> str:
    text = text.lower()
    for subtype, keywords in SUBTYPES.items():
        for kw in keywords:
            if kw in text:
                return subtype
    return "unknown"


def _find_colors(text: str) -> tuple[str, str]:
    text = text.lower()
    found = []
    for color_name, keywords in COLORS.items():
        for kw in keywords:
            if kw in text and color_name not in found:
                found.append(color_name)
                break
    primary   = found[0] if len(found) > 0 else "unknown"
    secondary = found[1] if len(found) > 1 else None
    return primary, secondary


def _find_fit(text: str) -> str:
    text = text.lower()
    for fit, keywords in FITS.items():
        for kw in keywords:
            if kw in text:
                return fit
    return "unknown"


def _find_season(text: str) -> str:
    text = text.lower()
    for season, keywords in SEASONS.items():
        for kw in keywords:
            if kw in text:
                return season
    return "unknown"


def _find_style(text: str) -> str:
    text = text.lower()
    for style, keywords in STYLES.items():
        for kw in keywords:
            if kw in text:
                return style
    return "unknown"


def _find_formality(text: str) -> str:
    text = text.lower()
    for formality, keywords in FORMALITY.items():
        for kw in keywords:
            if kw in text:
                return formality
    return "unknown"


# ──────────────────────────────────────────────────────────────
#  ГЛАВНАЯ ФУНКЦИЯ
# ──────────────────────────────────────────────────────────────

def extract_attributes(caption: str) -> dict:
    """
    Принимает текстовое описание от BLIP.
    Возвращает словарь с признаками вещи.
    """
    color, secondary_color = _find_colors(caption)

    result = {
        "category":        _find_category(caption),
        "subtype":         _find_subtype(caption),
        "color":           color,
        "secondary_color": secondary_color,
        "fit":             _find_fit(caption),
        "season":          _find_season(caption),
        "style":           _find_style(caption),
        "formality":       _find_formality(caption),
        "description_raw": caption,
        "notes":           None,
    }

    result = apply_defaults(result)

    logger.info(f"🏷 Атрибуты: {result}")
    return result


# ──────────────────────────────────────────────────────────────
#  ТЕСТ
# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    test_captions = [
        "a black oversized hoodie on a white background",
        "white sneakers with grey sole",
        "dark grey puffer jacket with zipper",
        "black mini skirt with white top",
        "beige tote bag with long handles",
        "black cat-eye sunglasses",
        "brown ugg boots",
        "white cropped t-shirt",
        "navy blue wide leg trousers",
        "black denim jacket with buttons",
    ]

    for caption in test_captions:
        print(f"\n📝 '{caption}'")
        attrs = extract_attributes(caption)
        print(f"   category  → {attrs['category']}")
        print(f"   subtype   → {attrs['subtype']}")
        print(f"   color     → {attrs['color']}")
        print(f"   fit       → {attrs['fit']}")
        print(f"   season    → {attrs['season']}")
        print(f"   style     → {attrs['style']}")
