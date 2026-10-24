import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+mysqldb://username:password@localhost:3306/database_name",
)
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()

if __name__ == "__main__":
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1")).scalar()
        print("DB 연결 성공:", result)
