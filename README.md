# QueryMate_Text-to-SQL-CSV

## Deployed Link: https://huggingface.co/spaces/pratham0011/QueryMate_Text-to-SQL-CSV

![image](https://github.com/user-attachments/assets/59bf8b5f-a447-4f30-8f4b-21f34927b457)

### Implementation Steps:

1.	Setup
  - DB: Choose a SQL database with some mock tables (e.g., users, employees etc) 
  - CSV data:Use CSVs containing mock data (e.g. sales data, inventory, etc.)

2. Business logic:
- Setup agents to understand DDL from different sources
- Setup text to query conversion logic
- Run the query and verify the expected results
- Setup orchestrator agent to trigger the right agent based on the query passed
- Each agent should maintain a memory of all past interactions (such as tasks given to the Task Manager Agent). Also ensure that memory is persistent, so restarting the app doesn’t lose the history.

3.	Rest API:
- Expose the Rest API for asking query i.e. POST /query


### Submission Guidelines:
1.	Git Repository:
- Use Git for version control and commit your progress regularly.
- Ensure the repository is well-organized with clear documentation.
	
2.	Code Quality:
- Follow good coding practices, including semantic variable naming and code comments.
- Write clean, readable, and well-structured code.

3.	Documentation:
- Provide a README file explaining your approach, challenges faced, and how to run the project.
- Include any additional notes or comments for the evaluators.

4.	Video Demonstration:
- Record a video (max 120 seconds) showing the tool in action.
- Explain your biggest blocker and how you overcame it during the development process.

5. Time:
- The time to submission is 3 days from the day of accepting the assignment. For any queries, reach out to anshu@procureyard.com

<br>

# Submission

# QueryMate: Text to SQL & CSV

QueryMate is a powerful application that converts natural language queries into SQL statements and CSV outputs using FastAPI for the backend and Streamlit for the frontend. It allows users to interact with a SQLite database and CSV files seamlessly.

## Project Structure
``` bash
.
├── Dockerfile  
├── employee.csv         # Sample CSV data  
├── main.py              # FastAPI backend 
├── requirements.txt      # Python dependencies
├── streamlit_app.py      # Streamlit frontend 
└── student.db           # Sample SQL data
```

## Approach

1. **Backend with FastAPI**: The FastAPI application (`main.py`) handles incoming queries, processes them using Google Generative AI, and returns the results in either SQL or pandas query format. It integrates with SQLite to execute SQL commands and uses pandas to process CSV data.

2. **Frontend with Streamlit**: The Streamlit application (`streamlit_app.py`) provides an interactive UI for users to input queries. It communicates with the FastAPI backend, displaying results and maintaining chat history.

3. **Data Storage**: Sample data is stored in `student.db` for SQL queries and `employee.csv` for CSV-based queries.

4. **Deployment**: The application is deployed on Hugging Face Spaces, allowing users to access it easily.

## Challenges Faced

1. **Integration of FastAPI with Streamlit**: Ensuring smooth communication between the FastAPI backend and the Streamlit frontend was a key challenge. This involved handling asynchronous requests and ensuring the backend was running when the frontend made requests.

2. **Error Handling**: Managing different types of errors, such as SQL errors and pandas execution errors, required robust error handling mechanisms to provide clear feedback to users.

3. **Chat History Management**: Implementing chat history in Streamlit to persist through user interactions added complexity but improved user experience.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Streamlit
- Pandas
- SQLite3
- Requests
- python-dotenv
- google-generativeai

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Procureyard/ai-engineer-explorer-PrathamKumar125.git
   cd ai-engineer-explorer-PrathamKumar125
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the applications in separate terminals:

   - In the first terminal, start the FastAPI backend:

     ```bash
     streamlit run streamlit_app.py
     ```

   - In the second terminal, start the Streamlit app:

     ```bash
     uvicorn main:app --reload
     ```

## Running with Docker

To run the application using Docker, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t querymate .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8501:8501 -p 8000:8000 querymate
   ```

## Deployment

You can access the deployed application here: [QueryMate on Hugging Face Spaces](https://huggingface.co/spaces/pratham0011/QueryMate_Text-to-SQL-CSV)
