from pathlib import Path
from dotenv import load_dotenv
import os
env_path=Path("'.env'")
load_dotenv(dotenv_path="'env_path'")
from decouple import config

class Settings:
    postgresql_user: str = config("postgresql_user")
    postgresql_pwd=config("postgresql_pwd")
    postgresql_port=config("postgresql_port")
    postgresql_db=config("postgresql_db")
    postgresql_server=config("postgresql_server")
    database_url=f"postgresql+psycopg2://{postgresql_user}:{postgresql_pwd}@{postgresql_server}:{postgresql_port}/{postgresql_db}"
settings = Settings()


