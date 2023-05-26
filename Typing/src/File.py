"""
file.py - Class for file.
"""
from __future__ import annotations
import os
import shutil
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.Folder import Folder

class File:
    def __init__(self, source_path: str = ""):
        """
        Instance initialization settings.

        :param source_path: The path where the file is stored. This parameter is a string representing the path to the file.

        :var self.name: The name of the file. This is a string representing the file name.
        :var self.path: The path in a standard format. This is a string representing the standardized path to the file.
        """
        self.name = os.path.basename(source_path)
        self.path = os.path.abspath(source_path)


    def transfer(self, target_path: str = "") -> str:
        """
        Transfer the file.

        :deprecated: This method is deprecated. Please use the move method instead.
        :param target_path: The path where the file is to be transferred. This parameter is a string representing the path to the target directory.
        :return: The new path to the file after transfer.
        """

        if not os.path.exists(target_path):
            raise Exception("The target directory does not exist.")

        shutil.move(self.path, target_path)
        self.path = os.path.join(target_path, self.name)

        return self.path

    def move(self, target: Folder):
        """
        Transfer the file to a folder.

        :param target: The folder where the file is to be transferred. This parameter is an object representing the target folder.
        """
        if os.path.exists(os.path.join(target.path, self.name)):
            # remove
            os.remove(os.path.join(target.path, self.name))
        shutil.move(self.path, target.path)
        self.path = os.path.join(target.path, self.name)

    def delete(self):
        """
        Delete the file.
        """

        os.remove(self.path)

    def __str__(self):
        """
        Rewrite the print function.

        :return: A string representing the name and path of the file
        """

        return f"<File: name = {self.name}, path = {self.path}>"