import shutil
import os

def delete_folder_contents(path):
    if not os.path.exists(path):
        print(f"Folder does not exist: {path}")
        return

    for item_name in os.listdir(path):
        if item_name.startswith('.'):
            continue

        item_path = os.path.join(path, item_name)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
            print(f"Deleted: {item_path}")
        except Exception as e:
            print(f"Failed to delete {item_path}. Reason: {e}")

folders_to_clear = [
    "data/",
    "logs/",
    "import/",
    "plugins/",
    "mysql-data/"
]

for folder in folders_to_clear:
    delete_folder_contents(folder)
