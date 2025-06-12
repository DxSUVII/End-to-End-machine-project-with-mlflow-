# create componets 
# it willl create a list of all coumn then check each column shecma 
# # and then check if the column is in the schema or not
# if not it will raise an error 
# if yes it will return the schema of the column as status text 
import os 
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd



class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config


    def validate_all_columns(self) -> bool:
        try:
            validation_status= None
            data= pd.read_csv(self.config.unzip_data_dir)
            all_cols =  list(data.columns)
            all_datatype = list(data.dtypes)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema and  all_datatype:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation Status :{validation_status}")
                    raise ValueError(f"Column {col} is not in the schema or datatype mismatch")
                else:
                    validation_status =True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation stats: {validation_status} for column {col} with datatype {data[col].dtype} and schema {self.config.all_schema[col]}")
            logger.info("All columns validated successfully")
            return validation_status

        except Exception as e:
            raise e
