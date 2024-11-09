# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 7860 available to the world outside this container
EXPOSE 7860

# Create a script to run both FastAPI and Streamlit
RUN echo '#!/bin/bash\n\
uvicorn main:app --host 0.0.0.0 --port 8000 &\n\
streamlit run streamlit_app.py --server.port 7860 --server.address 0.0.0.0\n\
' > /app/run.sh

RUN chmod +x /app/run.sh

# Run the script when the container launches
CMD ["/app/run.sh"]