import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="QueryMate: Text to SQL & CSV")

st.markdown("# QueryMate: Text to SQL & CSV 💬🗄️")
st.markdown('''Welcome to QueryMate, your friendly assistant for converting natural language queries into SQL statements and CSV outputs!
               Let's get started with your data queries!''')

# Initialize chat history in session state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Data source selection
data_source = st.radio("Select Data Source:", ('SQL Database', 'Employee CSV'))

# Predefined queries
predefined_queries = {
    'SQL Database': [
        'Print all students',
        'Count total number of students',
        'List students in Data Science class'
    ],
    'Employee CSV': [
        'Print employees having the department id equal to 100',
        'Count total number of employees',
        'List Top 5 employees according to salary in descending order'
    ]
}

st.markdown(f"### Predefined Queries for {data_source}")

# Create buttons for predefined queries
for query in predefined_queries[data_source]:
    if st.button(query):
        st.session_state.predefined_query = query

st.markdown("### Enter Your Question")
question = st.text_input("Input: ", key="input", value=st.session_state.get('predefined_query', ''))

# Submit button
submit = st.button("Submit")

if submit:
    # Send request to FastAPI backend
    response = requests.post("http://localhost:8000/query", 
                             json={"question": question, "data_source": data_source})
    if response.status_code == 200:
        data = response.json()
        st.markdown(f"## Generated {'SQL' if data_source == 'SQL Database' else 'Pandas'} Query")
        st.code(data['query'])
        
        st.markdown("## Query Results")
        result = data['result']
        
        if isinstance(result, list) and len(result) > 0:
            if isinstance(result[0], dict):
                # For CSV queries that return a list of dictionaries
                df = pd.DataFrame(result)
                st.dataframe(df)
            elif isinstance(result[0], list):
                # For SQL queries that return a list of lists
                df = pd.DataFrame(result)
                st.dataframe(df)
            else:
                # For single column results
                st.dataframe(pd.DataFrame(result, columns=['Result']))
        elif isinstance(result, dict):
            # For single row results
            st.table(result)
        else:
            # For scalar results or empty results
            st.write(result)

        if data_source == 'Employee CSV':
            st.markdown("## Available CSV Columns")
            st.write(data['columns'])

        # Update chat history in session state
        st.session_state.chat_history.append(f"👨‍💻({data_source}): {question}")
        st.session_state.chat_history.append(f"🤖: {data['query']}")
    else:
        st.error(f"Error processing your request: {response.text}")

    # Clear the predefined query from session state
    st.session_state.pop('predefined_query', None)

# Display chat history
st.markdown("## Chat History")
for message in st.session_state.chat_history:
    st.text(message)

# Option to clear chat history
if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.success("Chat history cleared!")