FROM python:3.10.0-alpine

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 5000
CMD ["uvicorn", "app:app", "--port", "5000", "--host", "0.0.0.0"]
