FROM python:3.7-slim-buster

RUN pip install mlflow==1.24.0

EXPOSE 5000

CMD mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./models \
    --host 0.0.0.0 \
    --port 5000