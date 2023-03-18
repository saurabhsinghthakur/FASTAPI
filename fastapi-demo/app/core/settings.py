from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHMENY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHMENY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bing=False)

Base = declarative_base()
