import os

file_name = 'file_to_delete.txt'

os.remove(file_name)

if os.path.exists(file_name):
    os.remove(file_name)
