import yaml
import sys
import os


from us_visa.exception import USVisaException


def read_yaml_file(file_path:str) -> dict:
    """
    Reads a YAML file and returns its content as a dictionary.

    Args:
    file_path (str): The path to the YAML file.

    Returns:
    dict: The content of the YAML file as a dictionary.

    Raises:
    USVisaException: If there is an error reading the YAML file.
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise USVisaException(e,sys) from e
    

def write_yaml_file(file_path,content,replace=False):
    """
    Writes a dictionary to a YAML file.

    Args:
    file_path (str): The path to the YAML file.
    content (dict): The content to write to the YAML file.
    replace (bool): Whether to replace the file if it already exists. Default is False.

    Raises:
    USVisaException: If there is an error writing to the YAML file.
    """
    try:
        # Remove the existing file if replace is True and the file exists
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        # Write the content to the YAML file
        with open(file_path,"w") as file:
            yaml.dump(content,file)
    
    except Exception as e:
        raise USVisaException(e,sys) from e
    
