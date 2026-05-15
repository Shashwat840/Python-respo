import os

if os.path.exists("file1.txt"):
    os.remove("file1.txt")
    print("file deleted..")
else:
    print("file not found to delete..")