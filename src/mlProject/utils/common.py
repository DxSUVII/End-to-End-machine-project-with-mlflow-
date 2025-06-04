""" sso we need this file keep most comonly usesd functions """
import os

from box.config_box import ConfigBox    #it used so we can use ex: d3.key
from box.exceptions import BoxValueError
import yaml
from src.mlProject import logger
import json
import joblib
from ensure import ensure_annotations  #
from box import ConfigBox
from pathlib import Path
from typing import Any


""" to read yaml file and load yaml file create a fucntion"""
@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """ read yaml file and return
    Args:
        Path_to_yaml (str): Path like input
    Raises:
        if yaml filers are empty
    Return
         ConfigBox: CongfigboxType"""

 try:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe.load(yaml_file)
        logger.info(f"yaml file:{path_to_yaml}loaded succuesfuly")
        return ConfigBox(content)
 except BoxValueError:
    raise  ValueError("yaml file is empty")
 except Exception as e:
     raise e


 @ensure_annotations
 def create_directories(path_to_directories:list,verbose=True):
    """ create list of direcotories """
    """ARGs:
             path_to_directories (list): lsit of path of directories 
             ingore_log(bool,optinal): ingore if multile dirs is to be crearted .Deafaulters to Faslse"""

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directoety at: {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    """SAve jsom data"""
    """Args:
    path (Path): path to json files
    data(dict):data to be saved in json files"""

    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at :{path}")


@ensure_annotation
def load_json(path: Path) -> ConfigBox:
    """load json files data
    Args:
        path(path)- path to json files
     Return:
            ConfigBox:data as Class attributre instedd   of dict"""

   with open(path) as f:
       content = json.load(f)

   logger.info(f"json file loaded succesfulry form:{path}")
   return ConfigBox(content)



@ensure_annotations
def save_bin(data: Any,path:Path):
    """Save binary file
    Args:
        data(any): data tobe saved as binary
        path(Path): path to binary file """

    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at:{path}")


@ensure_annotations
def load_bin(path:Path) -> Any:
    """load binary data
    Args:
        path((Path):path to binary file
    returns:
    Any: object stored in the files"""
    data =joblib.load(path)
    logger.info(f"binary file  loaded from: {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """load binary data
      Args:
          path((Path):path to binary file
      returns:
      size: size in kb"""
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

