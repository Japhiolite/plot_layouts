### Libraries
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

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
