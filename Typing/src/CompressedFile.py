"""
compressed_file.py - Class for compressed file.
"""
from __future__ import annotations
import os
import shutil
import zipfile
from src.File import File
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.Folder import Folder
from typing import Optional

def is_compressed_file(file_path: str) -> bool:
    """
    Determine if the file is a compressed file.

    :param file_path: The path to the file. This is a string representing the path to the file.
    :return: A boolean value representing whether the file is a compressed file.
    """
    return os.path.splitext(file_path)[1] in [".zip", ".rar", ".7z"]

class CompressedFile(File):
    def __init__(self, source_path: str = ""):
        """
        Instance initialization settings.

        :param source_path: The path where the compressed file is stored. This is a string representing the path to the compressed file.

        :var self.name: The name of the compressed file. This is a string representing the name of the compressed file.
        :var self.path: The path in a standard format. This is a string representing the standardized path to the compressed file.
        """
        self.name = os.path.basename(source_path)
        self.path = os.path.abspath(source_path)

    def compress(self, source_path: str = ""):
        """
        Create a compressed file from the folder.

        :deprecated: This method is deprecated. Please use the compress_folder method instead.
        :param source_path: The path of the folder. This is a string representing the path to the folder.
        """
        if not os.path.exists(source_path):
            raise Exception("The source directory does not exist.")

        with zipfile.ZipFile(self.path, "w") as zip_file:
            for file in os.listdir(source_path):
                file_path = os.path.join(source_path, file)
                if os.path.isfile(file_path):
                    zip_file.write(file_path, file)

    def compress_folder(self, source: Folder):
        """
        Create a compressed file from the folder.

        :param source: The folder. This is an object representing the folder.
        """
        with zipfile.ZipFile(self.path, "w") as zip_file:
            for file in os.listdir(source.path):
                file_path = os.path.join(source.path, file)
                if os.path.isfile(file_path):
                    zip_file.write(file_path, file)

    def decompress(self, target_path: str = ""):
        """
        Decompress the compressed file.

        :deprecated: This method is deprecated. Please use the decompress_to_folder method instead.
        :param target_path: The path where the compressed file will be decompressed. This is a string representing the path to the target directory.
        """
        if not os.path.exists(target_path):
            raise Exception("The target directory does not exist.")

        with zipfile.ZipFile(self.path, "r") as zip_file:
            zip_file.extractall(target_path)

    def decompress_to_folder(self, target: Optional[Folder] = None) -> Folder:
        from src.Folder import Folder # Avoid circular import
        """
        Decompress the compressed file.

        :param target: The folder where the compressed file will be decompressed. If this parameter is None, the compressed file will be decompressed to the {compress file upper folder}/{compressed file name}.
        """

        if target is None:
            path = os.path.join(os.path.dirname(self.path), os.path.splitext(self.name)[0])
        else:
            path = target.path

        with zipfile.ZipFile(self.path, "r") as zip_file:
            zip_file.extractall(path)

        return Folder(path)

    def __str__(self) -> str:
        """
        Rewrite the print function.

        :return: A string representing the CompressedFile instance. This string should include the name and path of the compressed file.
        """

        return f"<CompressedFile: name = {self.name}, path = {self.path}>"
