from mlProject.config.configuration import ConfigurationManger
#from mlProject.components.data_transformation import DataTransformation
# If the above import fails, check if the file is named 'data_transformation.py' in 'mlProject/components/'
# If the file is actually named 'data_transformations.py', use the following import instead:
from mlProject.components.data_transformations import DataTransformation
from mlProject import logger
from pathlib import Path



STAGE_NAME  = "Data Transformation Stage"

class DataTransformationsTrainingPipeliine:
 def main(self):
    try:
        with open(Path("artifacts/data_validation/status.txt"), "r") as f:
            status_text = f.read()
            # Extract the word after 'validation stats: '
            status_word = status_text.split("validation stats: ")[-1].split()[0]

        if status_word == "True":
            config = ConfigurationManger()
            data_transformations_config = config.get_data_transformation_config()
            data_transformations = DataTransformation(config=data_transformations_config)
            data_transformations.train_test_spliting()
        else:
            raise Exception("Your data schema is not valid")

    except Exception as e:
        print(e)


if __name__ =='__main__':
 try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj  = DataTransformationsTrainingPipeliine()
    obj.main()
    logger.info(f">>>>>>>stage{STAGE_NAME}   ccompleted <<<<<<<\n\n XXXXXXXXXXXXXXXX")

 except Exception as e:  
        logger.exceptions (e)
        raise e     
           



