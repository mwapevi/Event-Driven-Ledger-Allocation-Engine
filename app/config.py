import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    #DATABASE_URL: str | None = os.getenv("DATABASE_URL")
    DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "sqlite:///allocation.db"
)

    COLUMN_API_KEY: str | None = os.getenv("COLUMN_API_KEY")
    COLUMN_BASE_URL: str | None = os.getenv("COLUMN_BASE_URL")

    CLEARING_ACCOUNT_ID: str | None = os.getenv("CLEARING_ACCOUNT_ID")

    ALLOCATIONS: dict[str, float] = {
        "ACCOUNT_A": float(os.getenv("ACCOUNT_A", "0.2")),
        "ACCOUNT_B": float(os.getenv("ACCOUNT_B", "0.2")),
        "ACCOUNT_C": float(os.getenv("ACCOUNT_C", "0.2")),
        "ACCOUNT_D": float(os.getenv("ACCOUNT_D", "0.2")),
        "ACCOUNT_E": float(os.getenv("ACCOUNT_E", "0.2")),
    }


settings = Settings()