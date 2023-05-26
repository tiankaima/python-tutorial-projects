# !!! deprecated !!!
#%%
from src.File import File
from src.Folder import Folder
from src.CompressedFile import CompressedFile
import os
import shutil
import time
import random

def get_timestamp() -> str:
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return timestamp

#%%
# ------------------------ File ------------------------

# generate test file
def generate_test_file() -> str:
    # at dir Tests/, create example{timestamp}.txt
    file_name = "example" + str(get_timestamp()) + ".txt"
    file_path = os.path.join(os.getcwd(), "Tests", file_name)
    with open(file_path, "w") as f:
        f.write("This is a test file.")

    return file_path

# open test file with File class
def open_test_file(file_path: str) -> File:
    file = File(file_path)
    return file

file_path = generate_test_file()
file = open_test_file(file_path)
print(file)
# try move that to Tests/{timestamp}/example{timestamp}.txt
target_path = os.path.join(os.getcwd(), "Tests", get_timestamp())
if not os.path.exists(target_path):
    os.mkdir(target_path)
file.transfer(target_path)

# wait for user to check
input("Check the file and press Enter to continue...")


# %%
# ------------------------ Folder ------------------------

# generate test folder
def generate_test_folder() -> str:
    # at dir Tests/, create example{timestamp}/
    folder_name = "example" + str(get_timestamp())
    folder_path = os.path.join(os.getcwd(), "Tests", folder_name)
    os.mkdir(folder_path)

    # at dir Tests/example{timestamp}/, create example{timestamp}.txt
    file_name = "example" + str(get_timestamp()) + ".txt"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as f:
        f.write("This is a test file.")

    return folder_path

# open test folder with Folder class
def open_test_folder(folder_path: str) -> Folder:
    folder = Folder(folder_path)
    return folder

# test Folder class

folder_path = generate_test_folder()
folder = open_test_folder(folder_path)
print(folder)
# try move that to Tests/{timestamp}/example{timestamp}/
target_path = os.path.join(os.getcwd(), "Tests", get_timestamp())
if not os.path.exists(target_path):
    os.mkdir(target_path)
folder.unpack(target_path)

# wait for user to check
input("Check the folder and press Enter to continue...")



# %%
# ------------------------ CompressedFile ------------------------

# create an example folder for later to compress
def create_example_folder() -> str:
    # at dir Tests/, create example{timestamp}/
    folder_name = "example" + str(get_timestamp())
    folder_path = os.path.join(os.getcwd(), "Tests", folder_name)
    os.mkdir(folder_path)

    # at dir Tests/example{timestamp}/, create example{timestamp}.txt
    file_name = "example" + str(get_timestamp()) + ".txt"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as f:
        f.write("This is a test file.")

    return folder_path

# make example compress file
compress_file_path = os.path.join(os.getcwd(), "Tests", "example" + str(get_timestamp()) + ".zip")
compress_file = CompressedFile(compress_file_path)
print(compress_file)

# compress example folder
example_folder_path = create_example_folder()
compress_file.compress(example_folder_path)

# wait for user to check
input("Check the compressed file and press Enter to continue...")

# decompress example file
target_path = os.path.join(os.getcwd(), "Tests", get_timestamp())
if not os.path.exists(target_path):
    os.mkdir(target_path)

compress_file.decompress(target_path)

# wait for user to check
input("Check the decompressed folder and press Enter to continue...")
# %%
