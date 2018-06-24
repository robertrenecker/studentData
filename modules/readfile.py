import pandas as pd;
import numpy as np;
import csv;

def read_entire_file(filename):
    #temp = pd.read_csv(filename,sep=",", quotechar='"', names=['LEA_STATE', 'TOT_LEPENR_F', 'TOT_LEPENR_M'],encoding = 'unicode_escape', dtype = {'LEA_STATE': str, 'TOT_LEPENR_F': int, 'TOT_LEPENR_M': int});
    #return temp.query('TOT_LEPENR_M > 0 and TOT_LEPENR_F' > 0);
    tempArr = [];
    with open(filename, newline='', encoding='unicode_escape') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            try:
                tempArr.append([row[0], row[91], row[92]])
            except:
                print("Last row");

    temp = pd.DataFrame(tempArr[1:], columns=['stateNames','impairedAmales', 'impairedAfemales']);
    temp["impairedAmales"] = pd.to_numeric(temp["impairedAmales"]);
    temp["impairedAfemales"] = pd.to_numeric(temp["impairedAfemales"]);


    return temp;




#Generator method
"""
def read_entire_file(filename, header=False, chunkSize = 10 ** 5):
    for chunk in pd.read_csv(filename, delimiter=',', iterator = True, chunksize = chunkSize):
        yield (chunk)

def _generator(filename, header=False, chunk_size = 10 ** 5):
    chunk = read_entire_file(filename, header=False, chunkSize=10**5)
    for row in chunk:
        yield row
"""

