FROM python:3.9.6

# Set the working directory in the container
WORKDIR /usr/src/app

# Upgrade Pip
RUN python -m pip install --upgrade pip

# Install Poetry
RUN pip install poetry

# set the virtualenvs.create to false 
RUN poetry config virtualenvs.create false

# Copy the dependencies file to the working directory
COPY . .

# Install the dependencies
RUN poetry install

# Run the container
CMD ["poetry", "run", "python", "etl/main.py"]