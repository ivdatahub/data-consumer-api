FROM python:3.10-slim

WORKDIR /app

# Install build-essential
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

# Update pip and install poetry
RUN pip install --upgrade pip \
    && pip install poetry

# Copy application for container
COPY . .

# Instale as dependências usando Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --only main

# Run the command to start the application \
CMD ["poetry", "run", "python", "etl/run.py"]