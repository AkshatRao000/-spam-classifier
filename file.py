import os

folder_path = 'C:/your/folder/path'

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), 'r') as file:
            content = file.read()
            print(f"--- {filename} ---")
            print(content)
