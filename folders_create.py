# create folders from csv
# folder names must be listed horizontally on csv
import os, csv
with open('folder_names.csv', newline='') as f:
    reader = csv.reader(f)
    for directories in reader:
        for i in range(len(directories)):
            os.makedirs(directories[i])
