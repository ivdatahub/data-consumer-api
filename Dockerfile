FROM python:3.9.6

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Gerar o arquivo .env
RUN echo "SERVER_URL=https://economia.awesomeapi.com.br" > .env

COPY . .

CMD [ "python", "./etl/main.py" ]