from app.db.base import Base
from app.db.session import engine

import app.models.event  # noqa: F401
import app.models.transfer  # noqa: F401


def init_db():
    Base.metadata.create_all(bind=engine)