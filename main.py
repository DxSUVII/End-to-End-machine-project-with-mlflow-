## here in main.py we are importing all the necessary modules and classes
# and then we are running all the stages of the pipeline one by one
# we are also logging the start and end of each stage in the logger
## we are also handling exceptions in each stage and logging them in the logger
# and then we are raising the exception again so that the pipeline can be stopped
# if any stage fails
# and finally we are running the main function of each stage
# to run the pipeline
# we start from the data ingestion stage and then we move to the data validation stage
# then we move to the data transformation stage
# then we move to the model training stage
# and finally we move to the model evaluation stage

from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationPipeline
from mlProject.pipeline.stage_03_data_transformations import DataTransformationsTrainingPipeliine
from mlProject.pipeline.stage_04_model_training import ModelTrainerPipeline
from mlProject.pipeline.stage_05_model_evaluations import ModelEvaluationsTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started  <<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\n============x")
except Exception as e:
            logger.exception (e)
            raise e


STAGE_NAME = "Data Validation Stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started  <<<<<")
        data_ingestion=DataValidationPipeline()
        data_ingestion.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\n============X")
except Exception as e:
        logger.exception (e)
        raise e



STAGE_NAME = "Data Transformation Stage"
try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj  = DataTransformationsTrainingPipeliine()
        obj.main()
        logger.info(f">>>>>>>stage{STAGE_NAME}   ccompleted <<<<<<<\n\n XXXXXXXXXXXXXXXX")

except Exception as e:  
        logger.exception(e)
        raise e     



STAGE_NAME = "Model_Training_Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<< \n\n X=======")
        
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Evaluations Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationsTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<< \n\n X=======")
        
except Exception as e:
        logger.exceptions(e)
        raise e      