FROM python:3.7-slim-buster

RUN pip install mlflow==1.24.0

COPY requirements.txt .
RUN pip install --user -r requirements.txt

COPY entrypoint.sh ./
RUN ["chmod", "+x", "entrypoint.sh"]

ENTRYPOINT [ "./entrypoint.sh" ]

EXPOSE 5001