import shutil
import os

if os.path.exists("Files/file2.txt"):
	shutil.move("Files/file2.txt", "filedemo2.txt")
	print("Copy of file executed")
else:
	print("File not found")