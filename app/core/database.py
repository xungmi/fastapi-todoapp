import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Đường dẫn SQLite
# SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
#                                    username:password@localhost/database_name
# SQLALCHEMY_DATABASE_URL = "postgresql://xungdb:123@localhost:5432/fastapi_db"

# Tạo kết nối với database
# engine = create_engine(SQLALCHEMY_DATABASE_URL,
#           connect_args={"check_same_thread": False}) # Dùng cho SQLite
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# Tạo Session
"""
Dùng sessionmaker để tạo session tương tác với database.
Tắt autocommit và autoflush để bạn kiểm soát transaction 1 cách rõ ràng.
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base class để các model ORM kế thừa
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
