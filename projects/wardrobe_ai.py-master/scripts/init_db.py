import sys
from pathlib import Path

# Чтобы скрипт видел папку src
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.db.schema import create_tables

if __name__ == "__main__":
    create_tables()
