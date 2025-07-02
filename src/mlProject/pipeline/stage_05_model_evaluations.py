
from mlProject.components.model_evaluations import ModelEvaluation
from mlProject import logger
from mlProject.config.configuration import ConfigurationManger

STAGE_NAME = "Model evaluations stage"

class ModelEvaluationsTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config =ConfigurationManger()
        model_evaluation_config = config.get_model_evalution_config()
        model_evaluation = ModelEvaluation(config =model_evaluation_config)
        model_evaluation.log_into_mlflow()  



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationsTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<< \n\n X=======")
        
    except Exception as e:
        logger.exception(e)
        raise e      
