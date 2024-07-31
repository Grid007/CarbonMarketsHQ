import os
import requests
import pandas as pd
from models import Project, Session
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define constants
API_URL = "https://jsonplaceholder.typicode.com/posts"

# Get the database URL from environment variable
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///projects.db')

# Fetch data from the API
response = requests.get(API_URL)
data = response.json()

# Convert data to DataFrame
df = pd.DataFrame(data)

# Store data in SQLite database
session = Session()
for index, row in df.iterrows():
    project = Project(
        id=row['id'], 
        userId=row['userId'], 
        title=row['title'], 
        body=row['body']
    )
    session.add(project)
session.commit()

print("Data has been successfully fetched and stored in the database.")
