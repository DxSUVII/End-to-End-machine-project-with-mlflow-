import dagshub
dagshub.init(repo_owner='dxsm6996', repo_name='End-to-End-machine-project-with-mlflow-', mlflow=True)

import mlflow
with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name', 1)