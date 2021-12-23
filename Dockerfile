FROM python:3.8.11-alpine3.14

COPY . /app
WORKDIR app

RUN apk update --no-cache && \
    pip install  --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
