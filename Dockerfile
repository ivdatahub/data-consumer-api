FROM python:3.9.6

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

## The entrypoint of pipeline
CMD [ "python", "./etl/main.py" ]