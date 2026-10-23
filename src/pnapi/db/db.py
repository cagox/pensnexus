# src/pnapi/db/db.py
from sqlalchemy import URL, create_engine

from ..config import settings

db = settings.database

database_url = URL.create(
    "postgresql+psycopg2",
    username=db.user,
    password=db.password,
    host=db.host,
    port=db.port,
    database=db.name,
)

engine = create_engine(database_url)