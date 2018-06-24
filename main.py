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

    nationWide_results = comp.create_data_dictionary(resultTable);
    [print(state, nationWide_results[state]) for state in nationWide_results];
    print("Creating Map");
    trc= dict(
        type ='choropleth',
        locations = [state for state in nationWide_results],
        locationmode='USA-states',
        colorscale=['Viridis'],
        z = [np.sum(nationWide_results[i]) for i in nationWide_results]
        )
    lyt= dict(geo=dict(scope='usa'))
    map=go.Figure(data=[trc],layout=lyt)
    py.plot(map);












if __name__ == "__main__": main()
