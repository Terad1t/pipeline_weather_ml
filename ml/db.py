import os
from pathlib import Path
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from dotenv import load_dotenv

# caminho correto do .env
env_path = Path(__file__).resolve().parent.parent / "config" / ".env"

load_dotenv(env_path)

user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")
host = os.getenv("host", "localhost")

connection_string = f"postgresql+psycopg2://{user}:{quote_plus(password)}@{host}:5432/{database}"


def get_engine():
    

    if not all([user, password, database]):
        raise ValueError("Variáveis do banco não carregadas do .env")

    engine = create_engine(
        f"postgresql+psycopg2://{user}:{quote_plus(password)}@{host}:5432/{database}"
    )

    return engine