"""
folder.py - Class for folder.
"""
from __future__ import annotations
import os
import shutil
from src.File import File
from src.CompressedFile import CompressedFile, is_compressed_file
from typing import Union

class Folder:
    def __init__(self, source_path: str = ""):
        """
        Instance initialization settings.

        :param source_path: The path of the folder. This is a string representing the path to the folder.

        :var self.name: The name of the folder. This is a string representing the name of the folder.
        :var self.path: The path in a standard format. This is a string representing the standardized path to the folder.
        """
        self.name = os.path.basename(source_path)
        self.path = os.path.abspath(source_path)

        # create the folder if it does not exist
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def __getitem__(self, key: str) -> Union[File, Folder]:
        """
        Get the child of the folder.

        :param key: The name of the child. This is a string representing the name of the child.
        :return: An object representing the child of the folder.
        """

        child_path = os.path.join(self.path, key)
        if os.path.isfile(child_path):
            return File(child_path)
        elif os.path.isdir(child_path):
            return Folder(child_path)
        else:
            # create the folder if it does not exist
            os.makedirs(child_path)
            return Folder(child_path)


    def unpack(self, target_path: str = "") -> list[str]:
        """
        Unpack the folder.

        :deprecated: This method is deprecated. Please use the unpack_to_folder method instead.
        :param target_path: The path where the files in the folder will be unpacked. This is a string representing the path to the target directory.
        :return: A list of strings representing the paths to the unpacked files.
        """

        if not os.path.exists(target_path):
            raise Exception("The target directory does not exist.")

        file_list = []
        for file in os.listdir(self.path):
            file_path = os.path.join(self.path, file)
            if os.path.isfile(file_path):
                shutil.move(file_path, target_path)
                file_list.append(os.path.join(target_path, file))

        return file_list

    def unpack_to_folder(self, target: Folder) -> list[File]:
        """
        Unpack the folder to a folder.

        :param target: The folder where the files in the folder will be unpacked. This is an object representing the target folder.
        :return: A list of objects representing the unpacked files.
        """
        file_list = []
        for file in os.listdir(self.path):
            file_path = os.path.join(self.path, file)
            if os.path.isfile(file_path):
                File(file_path).move(target.path)
                file_list.append(File(os.path.join(target.path, file)))

        return file_list

    def children(self) -> list[Union[File, Folder]]:
        """
        Get the children of the folder.

        :return: A list of objects representing the children of the folder.
        """

        children_list = []
        for child in os.listdir(self.path):
            child_path = os.path.join(self.path, child)
            if os.path.isfile(child_path):
                children_list.append(File(child_path))
            elif os.path.isdir(child_path):
                children_list.append(Folder(child_path))

        return children_list

    def file_children(self) -> list[File]:
        """
        Get the file children of the folder.
        """
        file_children_list = []
        for child in os.listdir(self.path):
            child_path = os.path.join(self.path, child)
            if os.path.isfile(child_path):
                if is_compressed_file(child_path):
                    file_children_list.append(CompressedFile(child_path))
                else:
                    file_children_list.append(File(child_path))
        return file_children_list

    def folder_children(self) -> list[Folder]:
        """
        Get the folder children of the folder.
        """
        folder_children_list = []
        for child in os.listdir(self.path):
            child_path = os.path.join(self.path, child)
            if os.path.isdir(child_path):
                folder_children_list.append(Folder(child_path))
        return folder_children_list

    def delete(self) -> None:
        """
        Delete the folder.
        """
        shutil.rmtree(self.path)

    def __str__(self) -> str:
        """
        Rewrite the print function.

        :return: A string representing the name and path of the folder.
        """
        return f"<Folder: name = {self.name}, path = {self.path}>"

def current_folder() -> Folder:
    """
    Get the current folder.

    :return: An object representing the current folder.
    """
    return Folder(os.getcwd())