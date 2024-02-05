import os
import time as t
import pandas as pd
import re
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
def getTime(filetype, array):
    indexOfFileType = array.index(filetype)
    time = array[indexOfFileType -1][0:5]
    return time

f = open(date + "_MDX_UFM_Transactions.txt", "a")
f.write(",get batch,copy image to local,run 12 instances,review,review,review,prepare set sql 0th,prepare set sql 1st,compressed images list,review	list of src images,create BAT from for instances,split TXT; run BAT; and log,set sql log,compressed images list,prepare set sql 2nd,db sql out\n")
f.write("index,IQ.csv,IQ.bat,IQ.bat.xxx.bat,IQ.jpg.uniq.diff,IQ.csv.uniq,IQ.jpg.uniq,IQ.jpg.bat,IQ.jpg.bat.transid,IQ.jpg.txt,IQ.jpg.uniq.diff.2,IQ.jpg.copy.txt,IQ.jpg.bat.3.bat,IQ.jpg.bat.3.bat.xxx.bat,IQ.jpg.bat.transid.sql,IQ.jpg.txt.2,IQ.jpg.bat.transid.sql.1,IQ.jpg.bat.transid.sql.out\n")

for index in range(len(indexes)):
    results = os.popen("\"c:\\Program Files\\7-Zip\\7z.exe\" l " + folder + "\\" +  str(date) + "_" + indexes[index] + "_IQ.go-live.zip").read()
    results = re.sub("\s\s+" , " ", str(results.split("-------------------")[2].split("-------------------")[0].split("-----")[1]))
    df = pd.DataFrame([x.split(' ') for x in results.split('\n')])
    df = df.drop(df.columns[[0, 2, 3,4]], axis=1).dropna()
    string = df.to_string(header=None,index=False)
    string= string.replace("tmp\\MDX_manual_IQ.pl.split\\" + str(date) + "_" + str(indexes[index]) + "_IQ.go-live\\"+str(date) + "_" + str(indexes[index]) + "_IQ.", "")
    string = re.sub("\s\s+" , " ", string)
    string = string.replace(" ", "\n")
    timeNFile = string.split("\n")
    #           index,                  IQ.csv,                         IQ.bat,                             IQ.bat.xxx.bat,                         IQ.jpg.uniq.diff,                       IQ.csv.uniq,                            IQ.jpg.uniq,                                    IQ.jpg.bat,                     IQ.jpg.bat.transid,                         IQ.jpg.txt,                             IQ.jpg.uniq.diff.2,                             IQ.jpg.copy.txt,                            IQ.jpg.bat.3.bat,                           IQ.jpg.bat.3.bat.xxx.bat,                       IQ.jpg.bat.transid.sql                              ,IQ.jpg.txt.2,                          IQ.jpg.bat.transid.sql.1,                       IQ.jpg.bat.transid.sql.out
    f.write(indexes[index] + "," + getTime("csv", timeNFile) + "," + getTime("bat", timeNFile) + "," + getTime("bat.xxx.bat", timeNFile) + "," + getTime("jpg.uniq.diff", timeNFile) + "," + getTime("csv.uniq", timeNFile) + "," + getTime("jpg.uniq", timeNFile) + "," + getTime("jpg.bat", timeNFile) + "," + getTime("jpg.bat.transid", timeNFile) + "," + getTime("jpg.txt", timeNFile) + "," + getTime("jpg.uniq.diff.2", timeNFile) + "," + getTime("jpg.copy.txt", timeNFile) + "," + getTime("jpg.bat.3.bat", timeNFile) + "," + getTime("jpg.bat.3.bat.xxx.bat", timeNFile) + "," + getTime("jpg.bat.transid.sql", timeNFile) + "," + getTime("jpg.txt.2", timeNFile) + "," + getTime("jpg.bat.transid.sql.1", timeNFile) + "," + getTime("jpg.bat.transid.sql.out", timeNFile) + "\n")

f.close()