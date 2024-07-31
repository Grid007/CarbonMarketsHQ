```markdown
# Project Dashboard

This project provides a simple dashboard to visualize data from a REST API using Streamlit and SQLAlchemy. The project fetches data from an API, stores it in an SQLite database, and displays key metrics and visualizations in a Streamlit application.

## Project Structure

```
project_dashboard/
│
├── app.py              # Streamlit dashboard application
├── fetch_data.py       # Python script to fetch and store data
├── models.py           # SQLAlchemy models
├── requirements.txt    # List of dependencies
├── .env                # Environment variables configuration
└── projects.db         # SQLite database file (created after running fetch_data.py)
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   cd project_dashboard
   ```

2. **Create and Activate a Virtual Environment**

   Create a virtual environment for your project:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - **On Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS and Linux:**

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**

   Create a `.env` file in the root directory of your project and add the following line:

   ```
   DATABASE_URL=sqlite:///projects.db
   ```

   This line sets the database URL to use SQLite and stores the database file in the project directory.

5. **Fetch and Store Data**

   Run the `fetch_data.py` script to fetch data from the API and store it in the SQLite database:

   ```bash
   python fetch_data.py
   ```

   This will create a `projects.db` file in your project directory.

6. **Run the Streamlit Dashboard**

   Start the Streamlit application to view the dashboard:

   ```bash
   streamlit run app.py
   ```

   This will open a new browser window with the dashboard.

## Viewing the SQLite Database

To view and interact with the `projects.db` SQLite database, you have several options but I prefer this:

 **Using SQLite Command Line Interface**

   - Open Terminal (or Command Prompt on Windows)
   - Navigate to your project directory:

     ```bash
     cd path/to/your/project_dashboard
     ```

   - Open the SQLite CLI:

     ```bash
     sqlite3 projects.db
     ```

   - View the tables in the database:

     ```sql
     .tables
     ```

   - View the schema of the `projects` table:

     ```sql
     .schema projects
     ```

   - Query the `projects` table:

     ```sql
     SELECT * FROM projects LIMIT 10;
     ```

   - Exit the SQLite CLI:

     ```sql
     .exit
     ```



## Usage

- **Key Metrics**: View the total number of entries in the database.
- **Number of Projects per User**: Visualize how many projects each user has created.
- **Distribution of Project Title Lengths**: See the distribution of lengths of project titles.
- **Top 10 Entries**: Display the top 10 entries in the database.
- **Search Projects**: Search for projects by ID or title.

## Project Dependencies

The project relies on the following Python packages:

- `requests`: For making HTTP requests to the API.
- `pandas`: For data manipulation and analysis.
- `sqlalchemy`: For SQL database operations.
- `streamlit`: For creating the web dashboard.
- `python-dotenv`: For managing environment variables.


