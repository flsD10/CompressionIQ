import os
import time as t
import pandas as pd
import re
import csv
import zipfile
folder = input('Enter the folder: ')
date = folder.split("\\")[-1].split("_")[0]

results = os.popen("dir " + str(folder) + "\\*.zip").read()
folder = folder.replace("\\", "\\\\")
results = results.split("_")

i = 2
indexes = []
cont = True
while cont == True:
    try: 
        indexes.append(results[i])
    except IndexError:
        cont = False
    i+=2
f = open(folder + "\\\\RowCount.txt", "a")

for index in range(len(indexes)):
    #csvLocation = folder + "\\\\" +  str(date) + "_" + indexes[index] + "_IQ.go-live.zip\\\\tmp\\\\MDX_manual_IQ.pl.split\\\\" + date + "_" + indexes[index] + "_IQ.go-live\\\\" + date + "_" + indexes[index] + "_IQ.csv" 
    zipLocation = folder.replace("\\\\", "/") + "/" +  str(date) + "_" + indexes[index] + "_IQ.go-live.zip"
    zf = zipfile.ZipFile(zipLocation) 
    df = pd.read_csv(zf.open("tmp/MDX_manual_IQ.pl.split/" + date + "_" + indexes[index] + "_IQ.go-live/" + date + "_" + indexes[index] + "_IQ.csv"), header=None)
    rowCount = df.shape[0] 
    f.write(indexes[index] + ", " + str(rowCount) + "\n")