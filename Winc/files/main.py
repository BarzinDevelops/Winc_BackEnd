__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#--------------------------------------------
import os, shutil
from zipfile import ZipFile as zf

# Part1: creat function clean_cache which creates a directory 'cache'
# if it doesn't exist, but removes all files and subfolders within 
# 'cash'-directory if it does exist.

def clean_cache():
    cache_dir = "files\cache"
    if os.path.exists(cache_dir):
        for filename in os.listdir(cache_dir):
            file_path = os.path.join(cache_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                if os.path.islink(file_path):
                    os.unlink(file_path)
                else:
                    shutil.rmtree(file_path, ignore_errors=True)
    else:
        os.makedirs(cache_dir)

# Part2: cache_zip: takes a zip file path (str) and a cache dir 
# path (str) as arguments, in that order. The function then 
# unpacks the indicated zip file into a clean cache folder.
# You can test this with provided: "data.zip file".

def cache_zip(zip_path, cache_path):
    with zf(zip_path, 'r') as datazip:
        datazip.extractall(os.path.join(cache_path))

 
if __name__ == "__main__":
    clean_cache()
    zip_path = "files\data.zip"
    cache_path = "files\cache"
    cache_zip(zip_path, cache_path)
    