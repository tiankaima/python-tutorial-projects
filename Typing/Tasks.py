"""
Tasks.py

This file contains the tasks for the project.
Which shall be the ideal main entry point for the project.
"""
import json
from src import Folder, File, CompressedFile, current_folder

history = {}

def run(folder: Folder, target: Folder) -> None:
    global history
    """
    Run the task.

    :param folder: The folder to run the task.
    :param target: The target folder.
    """
    for file in folder.file_children():
        if isinstance(file, CompressedFile):
            decompressed = file.decompress_to_folder()
            run(decompressed, target)
            decompressed.delete()
        else:
            file.move(target[folder.name])
            # history[target[folder.name].path] = folder.path
            if target[folder.name].path not in history:
                history[target[folder.name].path] = {
                    "source": folder.path,
                    "count": 1
                }
            else:
                history[target[folder.name].path]["count"] += 1
    for folder in folder.folder_children():
        run(folder, target)

def run_task(id: int) -> None:
    global history
    """
    Run the task with given id.

    :param id: The id of the task [1,7]
    """

    source_folder = current_folder()["Tasks"][f"task{id}"]
    result_folder = current_folder()["Task_Results"][f"task{id}"]
    history = {}
    run(source_folder, result_folder)
    print(history)
    with open(f"./Task_Results/task{id}/data.json", "w") as f:
        json.dump(history, f, indent=4)

if __name__ == "__main__":
    for i in range(1, 8):
        run_task(i)

