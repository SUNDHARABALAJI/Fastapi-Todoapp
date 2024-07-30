from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://todoapp_database_lea0_user:okhWmqSmtg5S9yOd6SEedxfGzj0zX1bD@dpg-cqk7fkrqf0us73c3v7n0-a.oregon-postgres.render.com/todoapp_database_lea0"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
