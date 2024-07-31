import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variable
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///projects.db')

# Create a database engine
engine = create_engine(DATABASE_URL)

@st.cache
def load_data():
    """
    Load data from the SQLite database.
    This function is cached to avoid reloading data on every interaction.
    """
    return pd.read_sql('projects', engine)

# Create a Streamlit app
st.title('Projects Dashboard')

# Load data from the database
data = load_data()

# Display key metrics
st.header('Key Metrics')
st.write(f"Total number of entries: {data.shape[0]}")

# Distribution of entries by User ID
st.header('Number of Projects per User')
user_project_counts = data['userId'].value_counts().sort_index()
st.bar_chart(user_project_counts)

# Display the distribution of project title lengths
st.header('Distribution of Project Title Lengths')
data['title_length'] = data['title'].apply(len)
title_length_counts = data['title_length'].value_counts().sort_index()
st.bar_chart(title_length_counts)

# Display top 10 entries
st.header('Top 10 Entries')
st.write(data.head(10))

# Implement search functionality
st.header('Search Projects')
search_term = st.text_input('Enter Project ID or Title:')
if search_term:
    search_result = data[
        (data['title'].str.contains(search_term, case=False)) | 
        (data['id'].astype(str).str.contains(search_term))
    ]
    st.write(search_result)
