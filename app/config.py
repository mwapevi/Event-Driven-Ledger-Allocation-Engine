import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    DATABASE_URL: str | None = os.getenv("DATABASE_URL")

    COLUMN_API_KEY: str | None = os.getenv("COLUMN_API_KEY")
    COLUMN_BASE_URL: str | None = os.getenv("COLUMN_BASE_URL")

    CLEARING_ACCOUNT_ID: str | None = os.getenv("CLEARING_ACCOUNT_ID")

    ALLOCATIONS: dict = {
        "ACCOUNT A": float(os.getenv("ACCOUNT A", 0.2)),
        "ACCOUNT B": float(os.getenv("ACCOUNT B", 0.2)),
        "ACCOUNT C": float(os.getenv("ACCOUNT C", 0.2)),
        "ACCOUNT D": float(os.getenv("ACCOUNT D", 0.2)),
        "ACCOUNT E": float(os.getenv("ACCOUNT E", 0.2)),
    }


settings = Settings()