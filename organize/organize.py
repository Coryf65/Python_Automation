# Organzing Files
import os
from pathlib import Path

# Dictionary
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

# Finds which Directory to put the File into
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    # could not find the category
    return 'MISC'

# testing the function
# print(pickDirectory('.mp3'))

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        # if the directory does not exist create one
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
