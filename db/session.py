
from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine

DATABASE_URL= "sqlite:///./campus_companion.db"

# create the database engine
engine= create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False,
)



#create a session factory

SessionLocal= sessionmaker (autocommit=False, autoflush=False, bind=engine)


def init_db():
    from . import models


    SQLModel.metadata.create_all(bind=engine)

    print("Database initialised successfully!")
    print("Database location: {DATABASE_URL}")
    print("All tables created from db/models.py")