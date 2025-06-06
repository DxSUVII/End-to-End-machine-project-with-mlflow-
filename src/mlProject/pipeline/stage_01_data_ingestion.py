from mlProject.config.configuration import ConfigurationManger
from mlProject.components.data_ingestions import DataIngestion
from mlProject import logger

STAGE_NAME="Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


# now we utilise the main 

if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started  <<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\n============x")
    except Exception as e:
        logger.exceptioin(e)
        raise e