import numpy as np;


def create_data_dictionary(pandasTable):
    temp_dic = {};
    print(pandasTable);
    for i in range(len(pandasTable.index)):
        try:
            print("Curr vals: ", temp_dic[pandasTable.iloc[i,0]], "vals to be added: ", [pandasTable.iloc[i,1], pandasTable.iloc[i,2]]);
            temp_dic[pandasTable.iloc[i,0]] = [int(a)+int(b) for a, b in zip(temp_dic[pandasTable.iloc[i,0]],[pandasTable.iloc[i,1], pandasTable.iloc[i,2]])]
        except KeyError:

            temp_dic[pandasTable.iloc[i,0]] = [pandasTable.iloc[i,1],pandasTable.iloc[i,2]]
        except:
            print("Unhashable key type")
    return temp_dic;
