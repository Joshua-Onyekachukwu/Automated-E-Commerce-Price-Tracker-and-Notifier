import os


def create_folder_structure(base_path):
    structure = {
        "data": ["products.json"],
        "drivers": ["msedgedriver.exe"],
        "logs": ["tracker.log"],
        "src": [
            "__init__.py",
            "scraper.py",
            "notifications.py",
            "scheduler.py",
            "utils.py",
            "main.py",
        ],
        "tests": ["test_scraper.py"],
    }

    # Create base directory
    os.makedirs(base_path, exist_ok=True)

    # Create folders and files
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "w") as file:
                if file_name == "__init__.py":
                    file.write("")  # Empty file for initialization

    # Create standalone files in the base directory
    standalone_files = ["requirements.txt", "README.md", ".gitignore"]
    for file_name in standalone_files:
        file_path = os.path.join(base_path, file_name)
        with open(file_path, "w") as file:
            if file_name == "README.md":
                file.write("# Automated Price Tracker\n\nProject documentation.")
            elif file_name == ".gitignore":
                file.write("*.log\n*.pyc\n__pycache__/\ndriver/msedgedriver.exe\n")
            else:
                file.write("")  # Empty file for requirements.txt


if __name__ == "__main__":
    base_path = "Automated_Price_Tracker"
    create_folder_structure(base_path)
    print(f"Folder structure created under {base_path}")
