#!/bin/bash

export MLFLOW_TRACKING_URI=sqlite:///models/mlflow.db

mlflow models serve \
    --model-uri "models:/xgboost/production" \
    --host 0.0.0.0 \
    --port 5001 \
    --no-conda