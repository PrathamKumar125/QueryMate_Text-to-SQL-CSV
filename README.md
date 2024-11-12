# QueryMate_Text-to-SQL-CSV

### Deployed Link
QueryMate on Hugging Face Spaces: https://huggingface.co/spaces/pratham0011/QueryMate_Text-to-SQL-CSV

### Overview

QueryMate is an application that converts natural language queries into SQL statements and CSV outputs. It uses FastAPI for the backend and Streamlit for the frontend, allowing users to interact with a SQLite database and CSV files in a seamless and user-friendly way.

### Implementation Steps

1. **Setup**
   - **Database**: Use a SQL database with mock tables (e.g., users, employees).
   - **CSV Data**: Include CSVs with mock data (e.g., sales data, inventory).

2. **Business Logic**
   - Create agents to interpret DDL from different sources.
   - Implement text-to-query conversion logic.
   - Verify the query results against expected outcomes.
   - Use an orchestrator agent to select the correct agent based on the query type.
   - Ensure each agent maintains persistent memory to retain interaction history across app restarts.

3. **REST API**
   - Expose a REST API endpoint for queries: `POST /query`

### Project Structure

```bash
.
├── Dockerfile  
├── employee.csv         # Sample CSV data  
├── main.py              # FastAPI backend 
├── requirements.txt     # Python dependencies
├── streamlit_app.py     # Streamlit frontend 
└── student.db           # Sample SQL data
```

### Approach

1. **Backend with FastAPI**: The FastAPI backend (`main.py`) processes incoming queries, using Google Generative AI for conversions, and returns results in SQL or pandas format. It integrates with SQLite for SQL commands and pandas for CSV processing.

2. **Frontend with Streamlit**: The Streamlit frontend (`streamlit_app.py`) provides an interactive interface for user queries, communicates with the FastAPI backend, and maintains chat history.

3. **Data Storage**: Data is stored in `student.db` for SQL queries and `employee.csv` for CSV-based queries.

4. **Deployment**: The application is deployed on Hugging Face Spaces, accessible via the provided link.

### Challenges Faced

1. **FastAPI and Streamlit Integration**: Ensuring smooth asynchronous communication between FastAPI and Streamlit was challenging but crucial for reliability.
2. **Error Handling**: Robust error handling for SQL and pandas-related errors was necessary to deliver clear feedback to users.
3. **Chat History**: Implementing persistent chat history in Streamlit enhanced user experience.

### Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Streamlit
- Pandas
- SQLite3
- Requests
- python-dotenv
- google-generativeai

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Procureyard/ai-engineer-explorer-PrathamKumar125.git
   cd ai-engineer-explorer-PrathamKumar125
   ```

2. Set up a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the applications in separate terminals:

   - **FastAPI backend**: Run in one terminal:

     ```bash
     uvicorn main:app --reload
     ```

   - **Streamlit app**: Run in another terminal:

     ```bash
     streamlit run streamlit_app.py
     ```

### Running with Docker

To use Docker, follow these steps:

1. **Build the Docker image**:

   ```bash
   docker build -t querymate .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 8501:8501 -p 8000:8000 querymate
   ```

3. **Pull the Docker image** from Docker Hub:

   ```bash
   docker pull prathamkumars125/querymate-text-to-sql-csv
   ```

4. **Docker Hub Repository**: https://hub.docker.com/r/prathamkumars125/querymate-text-to-sql-csv
