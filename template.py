# Project template

import os
from pathlib import Path

project_name = input("Enter Project Name without any space...  ")
list_of_dir_and_files = [
    f"{project_name}_project/{project_name}_model/__init__.py",
    f"{project_name}_project/{project_name}_model/VERSION.txt",
    f"{project_name}_project/{project_name}_model/config.yml",
    f"{project_name}_project/{project_name}_model/pipeline.py",
    f"{project_name}_project/{project_name}_model/predict_pipeline.py",
    f"{project_name}_project/{project_name}_model/train_pipline.py",
    f"{project_name}_project/{project_name}_model/config/core.py",
    f"{project_name}_project/{project_name}_model/config/__init__.py",
    f"{project_name}_project/{project_name}_model/datasets/__init__.py",
    f"{project_name}_project/{project_name}_model/processing/__init__.py",
    f"{project_name}_project/{project_name}_model/processing/data_manager.py",
    f"{project_name}_project/{project_name}_model/processing/features.py",
    f"{project_name}_project/{project_name}_model/processing/validation.py",
    f"{project_name}_project/{project_name}_model/trained_models/__init__.py",
    f"{project_name}_project/requirements/requirements.txt"
]

for filepath in list_of_dir_and_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    print(filedir, filename)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # create an empty file