import math
import mlflow
import os
import logging
import xgboost
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def train_model():
    logging.info('Início leitura dos dados')
    path_dados = os.getcwd() + '/data/'
    df = pd.read_csv(path_dados + 'processed/casas.csv')
    X = df.drop('preco', axis=1)
    y = df['preco'].copy()

    logging.info('Holdout')
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.3,
                                                        random_state=42)
    dtrain = xgboost.DMatrix(X_train, label=y_train)
    dtest = xgboost.DMatrix(X_test, label=y_test)

    xgb_params = {
        'learning_rate': 0.3,
        'max_depth': 6,
        'seed': 42
    }

    logging.info('Init mlflow connection')
    mlflow.set_tracking_uri('http://mlflow:5000')

    logging.info('Init mlflow set experiment')
    mlflow.set_experiment('house-prices-script')
    with mlflow.start_run():
        logging.info('Init mlflow run')
        # mlflow.xgboost.autolog()
        xgb = xgboost.train(xgb_params, dtrain, evals=[(dtrain, 'train')])

        mlflow.xgboost.log_model(xgb, 'xgboost_auuur')

        xgb_predicted = xgb.predict(dtest)
        mse = mean_squared_error(y_test, xgb_predicted)
        rmse = math.sqrt(mse)
        r2 = r2_score(y_test, xgb_predicted)
        mlflow.log_metric('mse', mse)
        mlflow.log_metric('rmse', rmse)
        mlflow.log_metric('r2', r2)
