import os

# Get current working directory
path = os.getcwd()

# Delete the directory
def delete_dir(directory):
  os.rmdir(directory)

delete_dir(path + "/test")