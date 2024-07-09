import os
from pathlib import Path

# Define the project name
project_name = "us_visa"

# List of files to be created for the project
list_of_files = [
    f"{project_name}/__init__.py",

    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/components/__init__.py",

    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",

    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"
]


# Loop through each file path in the list
for file_path in list_of_files:

    # Convert the file path string to a Path object
    file_path = Path(file_path)

    # Split the file path into directory and file name
    file_dir, file_name = os.path.split(file_path)

    # Create the directory if it does not exist
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)

    # Create an empty file if it does not exist or if it is empty
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
    else:
        # Print a message if the file already exists
        print(f"file already exists: {file_path}")
    
