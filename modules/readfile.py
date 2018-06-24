import pandas as pd;
import numpy as np;
import csv;

def read_entire_file(filename):
    #temp = pd.read_csv(filename,sep=",", quotechar='"', names=['LEA_STATE', 'TOT_LEPENR_F', 'TOT_LEPENR_M'],encoding = 'unicode_escape', dtype = {'LEA_STATE': str, 'TOT_LEPENR_F': int, 'TOT_LEPENR_M': int});
    #return temp.query('TOT_LEPENR_M > 0 and TOT_LEPENR_F' > 0);

    """
    learning impaired individuals
    80 --> Hawaiin Male
    81 --> Hawaii Female
    82 --> Native American / Alaskan Male
    83 --> Native American / Alaskan Female
    84 --> Asian Male
    85 --> Asian Female
    86 --> Hispanic Male
    87 --> Hispanic Female
    88 --> Black Male
    89 --> Black Female
    90 --> White Male
    91 --> White Female
    91 --> total Male
    92 --> total female
    """

    tempArr = [];
    with open(filename, newline='', encoding='unicode_escape') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            try:
                
                tempArr.append([row[0],row[77],row[78],row[79],row[80],row[81],row[82],row[83],row[84],row[85],row[86],row[87],row[88], row[91], row[92]])
            except:
                print("Last row");

    temp = pd.DataFrame(tempArr[1:], columns=['stateNames', 'hiM', 'hiF','na_aM', 'na_aF', 'aM','aF', 'haM', 'haF', 'blM', 'blF', 'whM', 'whF', 'impairedAmales', 'impairedAfemales']);
    for i in range(1,len(temp.columns)):
        temp.iloc[:,i] = pd.to_numeric(temp.iloc[:,i]);
    #temp["impairedTotalmales"] = pd.to_numeric(temp.iloc[:,1:]);
    #temp["impairedTotalfemales"] = pd.to_numeric(temp["impairedAfemales"]);



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
