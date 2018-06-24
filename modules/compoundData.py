import numpy as np;


def create_data_dictionary(pandasTable):
    temp_dic = {};

    """

    """

    for i in range(len(pandasTable.index)):
        try:

            temp_dic[pandasTable.iloc[i,0]] = [int(a)+int(b) for a, b in zip(temp_dic[pandasTable.iloc[i,0]],[pandasTable.iloc[i,1], pandasTable.iloc[i,2], pandasTable.iloc[i,3],pandasTable.iloc[i,4],pandasTable.iloc[i,5],pandasTable.iloc[i,6],pandasTable.iloc[i,7],pandasTable.iloc[i,8],pandasTable.iloc[i,9],pandasTable.iloc[i,10], pandasTable.iloc[i,11],pandasTable.iloc[i,12],pandasTable.iloc[i,13],pandasTable.iloc[i,14]])]
        except KeyError:

            temp_dic[pandasTable.iloc[i,0]] = list([pandasTable.iloc[i,1],pandasTable.iloc[i,2], pandasTable.iloc[i,3],pandasTable.iloc[i,4],pandasTable.iloc[i,5],pandasTable.iloc[i,6],pandasTable.iloc[i,7],pandasTable.iloc[i,8],pandasTable.iloc[i,9],pandasTable.iloc[i,10], pandasTable.iloc[i,11],pandasTable.iloc[i,12],pandasTable.iloc[i,13],pandasTable.iloc[i,14]])
        except:
            print("Unhashable key type")

        largest_race = {};
        #allocate index, or since we know the index associated race, allocate it as a symbol.

    for key in temp_dic:

        race_val = np.argmax(temp_dic[key][:-2]);
        print(key, temp_dic[key][:-2], race_val);
        if race_val >= 0:

            if race_val == 0:
                #Hawaiin Male
                largest_race[key] = "Hispanic Male"
            if race_val == 1:
                largest_race[key] = "Hispanic Female"
            if race_val == 2:
                largest_race[key] = "Indian American/ Alaska Native Male"
            if race_val == 3:
                largest_race[key] = "Indian American/ Alaska Native Female"
            if race_val == 4:
                largest_race[key] = "Asian Male"
            if race_val == 5:
                largest_race[key] = "Asian Female"
            if race_val == 6:
                largest_race[key] = "Pacific Islander Male"
            if race_val == 7:
                largest_race[key] = "Pacific Islander Female"
            if race_val == 8:
                largest_race[key] = "African American Male"
            if race_val == 9:
                largest_race[key] = "African American Female"
            if race_val == 10:
                largest_race[key] = "White Male"
            if race_val == 11:
                largest_race[key] = "White Female"
            if race_val == 12:
                largest_race[key] = "Hawaiin Male"
            if race_val == 13:
                largest_race[key] = "Hawaiin Male"




    return temp_dic, largest_race;
