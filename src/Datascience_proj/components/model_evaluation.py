## importing the needed libraries
from src.Datascience_proj.entity.config_entity import ModelEvaluationConfig
from src.Datascience_proj.utils.common import save_json

from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, mae, r2

    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_X = test_data.drop([self.config.TARGET_COLUMN], axis =1)
        test_y = test_data[self.config.TARGET_COLUMN]

        #mlflow.set_registry_uri(self.config.mlflow_uri)
        #tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_X)

            (rmse,mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            ## save the metrics as local
            scores ={'rmse': rmse, 'mae': mae, 'r2': r2}
            save_json(path=Path(self.config.metric_filename), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric('mae', mae)

            # Model Registry does not work with file store
            #if tracking_uri_type_store != 'file':

                # Register te model
                # Ther are other ways to use the Model Registry, wich depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
               # mlflow.sklearn.log_model(model, 'model', registered_model_name = "ElasticNetModel")
            
            #else:
            mlflow.sklearn.log_model(model, 'model')