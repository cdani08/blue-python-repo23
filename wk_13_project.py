import os

current_directory = os.getcwd()
files = os.listdir()
files_dict = {}

for file in files:
    file_path = os.path.join(current_directory, file)
    file_size = os.path.getsize(file_path)
    files_dict[file] = file_size

print(files_dict)
