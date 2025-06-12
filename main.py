from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationPipeline


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
