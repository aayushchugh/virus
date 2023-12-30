import os

# Get current working directory
path = os.getcwd()

# Delete the directory
def delete_dir(directory):
  # Delete files in directory
  files = os.listdir(directory)
  for file in files:
    os.remove(os.path.join(directory, file))
  
  os.rmdir(directory)

delete_dir(os.path.join(path, 'test'))
