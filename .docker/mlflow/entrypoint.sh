#!/bin/bash

mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./models \
    --host 0.0.0.0 \
    --port 5000