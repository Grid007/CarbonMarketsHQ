import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variable
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///projects.db')

# Define SQLAlchemy Base
Base = declarative_base()

# Define Project model
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer)
    title = Column(String)
    body = Column(Text)

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create all tables
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()
