import os
import pandas as pd
import numpy as np
import joblib
import mlflow
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from pathlib import Path

from mlProject.entity.config_entity import ModelEvaluationsConfig
from mlProject.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationsConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mse = mean_squared_error(actual, pred)
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mse, r2, mae

    def log_into_mlflow(self):
        #  Set DagsHub credentials securely
        os.environ["MLFLOW_TRACKING_USERNAME"] = "dxsm6996"
        os.environ["MLFLOW_TRACKING_PASSWORD"] = "f90be35b72976c9fa0212395125c3e069ad1701d"

        #  Load test data and model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        #  Set DagsHub MLflow URI
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        mlflow.set_experiment("wine-quality-evaluation")

        with mlflow.start_run():
            # Predict and evaluate
            y_pred = model.predict(test_x)
            rmse, mse, r2, mae = self.eval_metrics(test_y, y_pred)

            #  Save metrics locally
            Path(self.config.metric_file_name).parent.mkdir(parents=True, exist_ok=True)
            scores = {"rmse": rmse, "mae": mae, "r2": r2, "mse": mse}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Log to MLflow
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mse", mse)
            mlflow.log_metric("mae", mae)

            #  Skip model logging due to WebGL or DAGSHub storage limitations
            # mlflow.sklearn.log_model(model, "model")
