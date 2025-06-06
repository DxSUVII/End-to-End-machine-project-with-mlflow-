import os
import json
import joblib
import yaml

from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any
from src.mlProject import logger  # Ensure `mlProject/logger.py` has `logger` defined

# ✅ Function to read YAML file
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read YAML file and return its content as ConfigBox."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


# ✅ Function to create directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories.

    Args:
        path_to_directories (list): List of directory paths.
        verbose (bool, optional): Log creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


# ✅ Function to save JSON
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save JSON data to file.

    Args:
        path (Path): Path to JSON file.
        data (dict): Data to save.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


# ✅ Function to load JSON
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load JSON data and return as ConfigBox.

    Args:
        path (Path): Path to JSON file.

    Returns:
        ConfigBox: Loaded JSON content.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from {path}")
    return ConfigBox(content)


# ✅ Function to save binary file
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save data as binary file.

    Args:
        data (Any): Data to save.
        path (Path): Path to save binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


# ✅ Function to load binary file
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file.

    Args:
        path (Path): Path to binary file.

    Returns:
        Any: Loaded data.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


# ✅ Function to get file size in KB
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get file size in KB.

    Args:
        path (Path): Path to file.

    Returns:
        str: Size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
