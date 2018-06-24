import pandas as pd;
import numpy as np;
import plotly.plotly as py;
import plotly.graph_objs as go;
import os;
import sys;


from modules import readfile as rf;
from modules import compoundData as comp;


def main():
    parentDirectory = os.path.dirname(os.getcwd());
    print(parentDirectory);
    file = parentDirectory+"/data/2015-16-crdc-data/CRDC-2015-16-school-data.csv";
    #9 back in index is asian male and female
    resultTable = rf.read_entire_file(file);

    nationWide_results, largest_race = comp.create_data_dictionary(resultTable);

    print("Creating Map");
    trc= dict(
        type ='choropleth',
        locations = [state for state in nationWide_results],
        locationmode='USA-states',
        colorscale=['Viridis'],
        z = [np.max(nationWide_results[i]) for i in nationWide_results],
        text=[largest_race[i] for i in largest_race],
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Millions USD")

        )


    lyt= dict(geo=dict(scope='usa'))
    map=go.Figure(data=[trc],layout=lyt)
    py.plot(map);
    py.image.save_as(map, filename='usa_data_map.png')











if __name__ == "__main__": main()
