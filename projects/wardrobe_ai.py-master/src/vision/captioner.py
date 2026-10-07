import logging
from pathlib import Path
from PIL import Image, ImageEnhance
from transformers import BlipProcessor, BlipForConditionalGeneration
from pillow_heif import register_heif_opener
register_heif_opener()

logger = logging.getLogger(__name__)

MODEL_NAME = "Salesforce/blip-image-captioning-base"

processor = None
model = None

# Фразы про фон — удаляем из описания
BACKGROUND_PHRASES = [
    "on a wooden floor", "on the floor", "on a floor",
    "on a hanger", "on a clothes hanger", "hanging on",
    "on a white background", "on a background",
    "on a bed", "on a table", "on a chair",
    "on a mannequin", "laid flat", "laying on",
    "on a rack", "on a hook", "on a wall",
    "on a carpet", "on a rug",
]


def _load_model():
    global processor, model
    if model is None:
        logger.info("Загружаем модель BLIP...")
        processor = BlipProcessor.from_pretrained(MODEL_NAME)
        model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME)
        logger.info("Модель BLIP загружена")


def preprocess_image(image: Image.Image) -> Image.Image:
    image = image.resize((512, 512), Image.LANCZOS)
    image = ImageEnhance.Contrast(image).enhance(1.2)
    image = ImageEnhance.Sharpness(image).enhance(1.3)
    image = ImageEnhance.Brightness(image).enhance(1.1)
    return image


def clean_caption(caption: str) -> str:
    """Убирает описание фона и лишние детали из описания."""
    result = caption.lower()
    for phrase in BACKGROUND_PHRASES:
        result = result.replace(phrase, "")
    # Убираем двойные пробелы и лишние запятые
    result = " ".join(result.split())
    result = result.strip(" ,.")
    return result


def generate_caption(image_path: str | Path) -> str:
    _load_model()

    image = Image.open(image_path).convert("RGB")
    image = preprocess_image(image)

    captions = []
    prompts = [
        "a photo of a clothing item, this is a",
        "this is a piece of clothing:",
        "the type of garment in this image is a",
    ]

    for prompt in prompts:
        inputs = processor(image, text=prompt, return_tensors="pt")
        output = model.generate(**inputs, max_new_tokens=60)
        caption = processor.decode(output[0], skip_special_tokens=True)
        captions.append(caption)

    # Берём самое длинное описание
    best = max(captions, key=len)
    # Очищаем от фона
    best = clean_caption(best)

    logger.info(f"{Path(image_path).name} → {best}")
    return best


from PIL import Image, ImageEnhance, ExifTags

def preprocess_image(image: Image.Image) -> Image.Image:
    # Авто-поворот по EXIF
    try:
        exif = image._getexif()
        if exif:
            for tag, value in exif.items():
                if ExifTags.TAGS.get(tag) == "Orientation":
                    if value == 3:
                        image = image.rotate(180, expand=True)
                    elif value == 6:
                        image = image.rotate(270, expand=True)
                    elif value == 8:
                        image = image.rotate(90, expand=True)
                    break
    except Exception:
        pass

    image = image.resize((512, 512), Image.LANCZOS)
    image = ImageEnhance.Contrast(image).enhance(1.2)
    image = ImageEnhance.Sharpness(image).enhance(1.3)
    image = ImageEnhance.Brightness(image).enhance(1.1)
    return image


if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO)
    path = sys.argv[1] if len(sys.argv) > 1 else "data/raw_images"
    folder = Path(path)
    if folder.is_dir():
        for img in folder.iterdir():
            if img.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}:
                print(generate_caption(img))
    else:
        print(generate_caption(folder))

