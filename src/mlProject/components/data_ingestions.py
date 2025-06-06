import os 
import urllib.request as request # to get the data from Url 
import zipfile # to unzip the file
from mlProject.utils.common import get_size
from mlProject import logger
from pathlib import Path
from mlProject.entity.config_entity import (DataIngestionConfig)



# Function to download the file from the URL
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file

            )
            logger.info(f"{filename} downloaded with follwing  info: \n{headers}")
        else:
            logger.info(f"file a;reday exist if size: {get_size(self.config.local_data_file)}")



    # create another funciton to unzip and extract zip file 
    def extract_zip_file(self):
        """
        extract_zip_file: str
        Extract the zip file to the data directory.
        functioin return time """
        unzip_path =self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)