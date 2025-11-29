import os
from pathlib import Path

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
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
    "research/trials.ipynb" ,
    "test.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    folder, filename = filepath.parent, filepath.name

    # Create folder
    if folder != "":
        os.makedirs(folder, exist_ok=True)

    # Create file
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass

        print(f"Created: {filepath}")
    else:
        print(f"Already exists: {filepath}")

print("\n✅ All files created successfully!")
