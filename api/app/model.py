import mlflow
from mlflow.tracking.client import MlflowClient
import xgboost as xgb

class Model:
    def __init__(self, model_name, stage):

        client = MlflowClient('sqlite:///models/mlflow.db')
        latest_version_info = client.get_latest_versions(model_name, stages=[stage])
        latest_production_version = latest_version_info[0].version

        print("Model latest version path is '%s'" % latest_version_info[0].source)

        self.loaded_model = mlflow.xgboost.load_model(
            latest_version_info[0].source
        )

        print("The latest production version of the model '%s' is '%s'." % (model_name, latest_production_version))
        print('Model is loaded!')

    def make_predictions(self, data):
        y_pred = xgb.DMatrix(data = data)
        predictions = self.loaded_model.predict(y_pred)

        print(predictions[0])
        print(predictions.shape[0])

        return 'success!'
