import databases
from config import settings
from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


@lru_cache()
def setting():
    return settings


def database_pgsql_url_config():
    return str(setting().DB_CONNECTION + "://" + setting().DB_USERNAME + ":" + setting().DB_PASSWORD +
               "@" + setting().DB_HOST + ":" + setting().DB_PORT + "/" + setting().DB_DATABASE)


database = databases.Database(database_pgsql_url_config())
engine = create_engine(database_pgsql_url_config())
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    return database
