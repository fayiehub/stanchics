from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.config import get_settings

settings = get_settings()

# SQLAlchemy engine — Azure SQL requires pool_pre_ping to handle dropped connections
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,        # test connections before using from pool
    pool_size=5,               # suitable for F1 free tier
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,         # recycle connections every 30 min
    echo=not settings.is_production,  # log SQL in dev, silent in prod
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    """FastAPI dependency — yields a DB session and ensures it closes after each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """Create all tables if they don't exist. Called on app startup."""
    from app.models import member, contact, newsletter, feedback  # noqa: F401 — import to register models
    Base.metadata.create_all(bind=engine)
