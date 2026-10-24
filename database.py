from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:test@127.0.0.1:3307/fastapi-ca"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()

if __name__ == "__main__":
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1")).scalar()
        print("DB 연결 성공:", result)