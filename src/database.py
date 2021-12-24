from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:120320@127.0.0.1:5434/vr_dart"

#create engine connect to db
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#create db session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#create db instant
Base = declarative_base()
