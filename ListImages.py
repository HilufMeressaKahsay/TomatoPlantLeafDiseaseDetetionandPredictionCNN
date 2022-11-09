import os
def List():
    path = 'uploads/'
    for file in os.scandir(path):
            if file.is_file():
                return file.name
name = List()
