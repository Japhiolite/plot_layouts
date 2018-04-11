### Libraries
import os, sys
import fileinput
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import color_palette_jn
import seaborn as sns
import dir_manage

### Overall Plot style
def set_style(style):
    """
    Function which sets the overall visual style of the plot it is used
    :param style: -string- 'paper', 'poster', 'notebook' defining different layouts
    :return:
    """
    if style == 'paper':
        plt.style.use(['seaborn-ticks', 'seaborn-paper'])
        matplotlib.rc("font", family="Times New Roman")
        matplotlib.rc("xtick", labelsize=13.)
        matplotlib.rc("ytick", labelsize=13.)
    elif style == 'poster':
        plt.style.use(['seaborn-ticks', 'seaborn-poster'])
    elif style == 'notebook':
        plt.style.use(['seaborn-ticks', 'seaborn-notebook'])


### Monitor files
def read_monitor_as_dataframe(filename):
    """
    Routine to read the monitoring points of a transient SHEMAT-Suite simulation, returning an array of recorded
    values
    param filename: string: name of monitoring file
           varname: string or list of strings: name of variables to be loaded
    return: monitoring file: dataframe containing all information of the monitoring file
    """
    # replace any % comments with
    if sys.version_info.major == 2:
        print("Seems you still work with Python 2.7.")
        print("You should consider moving to Version 3.x")
        fid = fileinput.FileInput(filename, inplace=True, backup='.bak')
        for line in fid:
            print(line.replace('%', ''))
    elif sys.version_info.major == 3:
        with fileinput.FileInput(filename, inplace=True, backup='.bak') as fid:
            for line in fid:
                print(line.replace('%', ''))

    # load dataframe
    datframe = pd.read_csv(filename, delim_whitespace=True)
    return datframe

def plot_monitor(var, dat, time_series=True):
    """
    Plotting function for monitoring points as time series
    :param var: string
                variable name of parameter from dat to be plotted
    :param dat: dataframe
                pandas dataframe containing all information
    :param time_series: boolean
                        definex x axis as time
    :return: ax: axis object of plot
    """
    # check if variable in dataframe
    if var not in dat:
        print("Dataframe does not contain this variable.")
        print("Check for Typos or if the Dataframe is correct.")

    dat.plot(x='time', y=var, style='<-', legend=True, markevery=5)

    return plt.gcf()

