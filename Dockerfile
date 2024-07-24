FROM python:3.9-slim

WORKDIR /app

# Instale as dependências do sistema e as ferramentas necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

# Instale pip, poetry e dependências
RUN pip install --upgrade pip \
    && pip install poetry

# Copie apenas os arquivos necessários para instalar as dependências
COPY pyproject.toml poetry.lock ./

# Instale as dependências usando Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --only main

# Copie o restante dos arquivos para o diretório de trabalho
COPY . .

# Run the command to start the application \
CMD ["python", "run.py"]