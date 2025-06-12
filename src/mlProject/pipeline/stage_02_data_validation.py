from mlProject.config.configuration import ConfigurationManger
from mlProject.components.data_validation import DataValidation
from mlProject import logger

STAGE_NAME = "Data Validation stage"

class DataValidationPipeline:
    def __init_(self):
        pass


    def main(self):
        config = ConfigurationManger()
        data_validation_config =config.get_data_validation_config()  # Make sure this matches your method name
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()  # Make sure this matches your method name
      

if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started  <<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\n============X")
    except Exception as e:
        logger.exception(e)
        raise e