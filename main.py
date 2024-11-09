from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai

app = FastAPI()

# Load environment variables and configure Genai
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

class Query(BaseModel):
    question: str
    data_source: str

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

def get_csv_columns():
    df = pd.read_csv('employee.csv')
    return df.columns.tolist()

csv_columns = get_csv_columns()

sql_prompt = """
You are an expert in converting English questions to SQL code!
The SQL database has the name STUDENT and has the following Columns - NAME, CLASS, SECTION

For example:
- How many entries of records are present? SQL command: SELECT COUNT(*) FROM STUDENT;
- Tell me all the students studying in Data Science class? SQL command: SELECT * FROM STUDENT where CLASS="Data Science";

Also, the SQL code should not have ''' in the beginning or at the end, and SQL word in output.
Ensure that you only generate valid SQL queries, not pandas or Python code.
"""

csv_prompt = f"""
You are an expert in analyzing CSV data and converting English questions to pandas query syntax.
The CSV file is named 'employee.csv' and contains employee information.
The available columns in the CSV file are: {', '.join(csv_columns)}

For example:
- How many employees are there? Pandas query: len(df)
- List all employees in the Sales department. Pandas query: df[df['Department'] == 'Sales']
- Show employees with a specific ID. Pandas query: df[df['ID'] == specific_id]

Provide only the pandas query syntax without any additional explanation or markdown formatting.
Do not include 'df = ' or any variable assignment in your response.
Make sure to use only the columns that are available in the CSV file.
Ensure that you only generate valid pandas queries, not SQL or other types of code.
"""

def execute_sql_query(query):
    conn = sqlite3.connect('student.db')
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        raise HTTPException(status_code=400, detail=f"SQL Error: {str(e)}")
    finally:
        conn.close()

def execute_pandas_query(query):
    df = pd.read_csv('employee.csv')
    try:
        result = eval(query, {'df': df, 'pd': pd})
        if isinstance(result, pd.DataFrame):
            return result.to_dict(orient='records')
        elif isinstance(result, pd.Series):
            return result.to_dict()
        else:
            return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Pandas Error: {str(e)}")

@app.post("/query")
async def process_query(query: Query):
    if query.data_source == "SQL Database":
        ai_response = get_gemini_response(query.question, sql_prompt)
        try:
            result = execute_sql_query(ai_response)
            return {"query": ai_response, "result": result}
        except HTTPException as e:
            raise HTTPException(status_code=400, detail=f"Error in SQL query: {e.detail}")
    else:  # CSV Data
        ai_response = get_gemini_response(query.question, csv_prompt)
        try:
            result = execute_pandas_query(ai_response)
            return {"query": ai_response, "result": result, "columns": csv_columns}
        except HTTPException as e:
            raise HTTPException(status_code=400, detail=f"Error in pandas query: {e.detail}")