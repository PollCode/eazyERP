from sqlmodel import create_engine, Session
from core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    pool_recycle=300,
    # Clave para pgbouncer en transaction mode:
    connect_args=(
        {"prepare_threshold": None} if "+psycopg://" in settings.DATABASE_URL else {},
        {"prepare_threshold": None} if "pgbouncer=true" in settings.DATABASE_URL else {}
    ),
)

def get_db():
    with Session(engine) as session:
        yield session