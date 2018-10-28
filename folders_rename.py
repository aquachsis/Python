# rename files based off csv
# CSVs should be single column with new name in each row
import os
with open('old_name.csv') as f:
    old_file_names = f.readlines()
with open('new_name.csv') as f:
    new_file_names = f.readlines()
for i in range(len(old_file_names)):
    os.rename(old_file_names[i].strip(),new_file_names[i].strip())
