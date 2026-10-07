from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
RAW_IMAGES_DIR = DATA_DIR / "raw_images"
PROCESSED_IMAGES_DIR = DATA_DIR / "processed_images"
OUTPUTS_DIR = BASE_DIR / "outputs"
PROMPTS_DIR = BASE_DIR / "prompts"
DB_PATH = DATA_DIR / "wardrobe.db"

LM_STUDIO_BASE_URL = "http://localhost:1234/v1"

from dotenv import load_dotenv
import os

load_dotenv()

BLIP_MAX_TOKENS     = int(os.getenv("BLIP_MAX_TOKENS", 60))
BLIP_MODEL          = os.getenv("BLIP_MODEL", "Salesforce/blip-image-captioning-base")
LM_STUDIO_URL       = os.getenv("LM_STUDIO_URL", "http://localhost:1234/v1")
LM_TEMPERATURE      = float(os.getenv("LM_STUDIO_TEMPERATURE", 0.7))
LM_MAX_TOKENS       = int(os.getenv("LM_STUDIO_MAX_TOKENS", 2048))

