from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm.declarative import declarative_base
from sqlalchemy.ext.declarative import declarative_base
# /Users/shubhamsinghchouhan/projects/fastapi/TodoApp/database.py:11: MovedIn20Warning: The ``declarative_base()``
# function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

Base = declarative_base()
SQLALCHEMY_DATABASE_URL = "sqlite:///.todos.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

