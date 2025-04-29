import os
from pathlib import Path


while True:
    project_name = input("Enter the project name: ").strip()
    if project_name:
        break


list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_preprocessing.py",
    f"{project_name}/components/model_loading.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/pipeline/inference.py",
    f"{project_name}/pipeline/training.py",
    f"{project_name}/exception.py",
    f"{project_name}/logger.py",
    "templates/index.html",
    "statics/style.css",
    "notebook/research.ipynb",
    "init_setup.sh",
    "requirements.txt",
    "Dockerfile",
    "app.py",
    "setup.py",
]


for file_path in list_of_files:
    path = Path(file_path)

 
    if path.parent != Path(""):
        path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
     
        path.touch()
