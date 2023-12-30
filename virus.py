# import os
# import shutil

# def delete_dir(directory):
#   # Delete directory and all its contents
#   shutil.rmtree(directory)

# root_dir = os.path.expanduser('~')

# file_path = os.path.join(root_dir, "test")

# delete_dir(file_path)

import os
import shutil
import pyAesCrypt
from getpass import getpass

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024

def lock_dir(directory):
    # compress the directory
    shutil.make_archive(directory, 'zip', directory)
    password = "123"
    
    # encrypt the zip file
    pyAesCrypt.encryptFile(f"{directory}.zip", f"{directory}.zip.aes", password, bufferSize)
    
    # delete the original directory
    shutil.rmtree(directory)
    os.remove(f"{directory}.zip")

# lock the directory
lock_dir("test")