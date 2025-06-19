from mlProject.config.configuration import ConfigurationManger
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger

STAGE_NAME = "Modle Trainng stage"

class ModelTrainerPipeline():
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManger()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model_trainer.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<< \n\n X=======")
        
    except Exception as e:
        logger.exceptions(e)
        raise e
