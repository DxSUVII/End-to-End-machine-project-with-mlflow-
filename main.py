from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationPipeline
from mlProject.pipeline.stage_03_data_transformations import DataTransformationsTrainingPipeliine


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
        logger.exceptions (e)
        raise e     