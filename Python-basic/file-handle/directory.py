import os

folder_path='C:\Practice\python'
entries=os.scandir(folder_path)

for entry in entries:
    if os.path.isfile(entry):
        print("file:",entry.name)
    elif os.path.isdir(entry):
        print("directory",entry.name)