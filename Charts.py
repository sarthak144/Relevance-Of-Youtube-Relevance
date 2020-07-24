import numpy as np
import matplotlib.pyplot as plt

def BarChannelAge(data):
    xtags = list(data.keys()) 
    yvalues = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(xtags, yvalues, color ='red',  width = 0.4)
    plt.xlabel("Age of Channels")
    plt.ylabel("Number of channels")
    plt.title("Age of channels of top search results")
    plt.show()
