import os
datasets = 'uploads'
files = []
folder = []
for r, d, f in os.walk(datasets):
    for file in f:
        if '.JPG' in file:
            files.append(os.path.join(r, file))
for f in files:
    path = f
    print(path)
