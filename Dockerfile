# This is a sample image 
FROM python:3.9-slim-buster

RUN mkdir /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "/app/main.py"]