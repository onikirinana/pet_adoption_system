import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
INSTANCE_DIR = BASE_DIR / "instance"
DATABASE_PATH = INSTANCE_DIR / "pet_adoption.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def init_db():
    INSTANCE_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
        connection.executescript(file.read())

    connection.commit()
    connection.close()

    print(f"Database created successfully: {DATABASE_PATH}")


if __name__ == "__main__":
    init_db()
