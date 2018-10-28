# combine all csv in directory into one csv named combined.csv
# TODO include single line break between files
from glob import glob
with open('combined.csv', 'a') as singleFile:
    for csv in glob('*.csv'):
        if csv == 'main.csv':
            pass
        else:
            for line in open(csv, 'r'):
                singleFile.write(line)
