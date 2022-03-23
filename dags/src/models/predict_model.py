import requests
import logging

url = 'http://mlflow:5001/invocations'

data = {
    "columns": ["tamanho", "ano", "garagem"],
    "data":[[159.0, 2004, 2]]
}

header = { 'Content-Type':'application/json'}

logging.info('Init run')

response = requests.post(url, json = data, headers = header)

logging.info('OK!')
logging.info(response)