from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:simple123@localhost:5432/ledger_allocation_engine"

#DATABASE_URL = os.getenv(
    #"DATABASE_URL",
   # "sqlite:///allocation.db"
#)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
