import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"

]


for filepath in list_of_files:
    filepath = Path(filepath) # CHECKING THE OS 
    filedir, filename = os.path.split(filepath) #SPLIT RETURNS THE FOLDER AND THE FILE SEPARATELY 
    

    #FOLDER CREATION IS DONE IN THE BELOW IF STATEMENT 
    if filedir != "":  #CHECKS FILEDIR IS EMPTY OR NOT 
        os.makedirs(filedir, exist_ok=True)  #MAKING DIRECTORY
        logging.info(f"Creating directory:{filedir} for the file {filename}")


    # FILE CREATION IS DONE IN THE BELOW IF STATEMENT     
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  #CHECKS THE FILES EXISTS OR NOT AND ITS SIZE AND IT IS 0 BEACUSE IF ONLY THE SIZE IS 0 WE WILL CREATE THE FILE 
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")