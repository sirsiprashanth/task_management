from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

password = 'Gurups4202'
#SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{password}@localhost/local_tm"
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{password}@localhost:5555/task_mgmt"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# Dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

print('connected to db')