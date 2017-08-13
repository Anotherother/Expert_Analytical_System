import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
from mpl_toolkits.mplot3d import Axes3D

# make plot matplotlib

def makePlots(original_feature_1, original_feature_2,
              spoof_feature_1, spoof_feature_2,
              label_feature_1, label_feature_2):
    """
    EXAMPLE. IT MAY BE
    :param original_feature_1: variance
    :param original_feature_2: mean
    :param spoof_feature_1: 
    :param spoof_feature_2: 

    """
    plt.figure(figsize=(20, 7))
    plt.plot(spoof_feature_1, color='blue', label="spoof")
    plt.title(label_feature_1)
    plt.plot(original_feature_1, color='red', label="original")
    plt.legend()
    plt.show()

    plt.figure(figsize=(20, 10))
    plt.title('Plot data on 2D space ' + label_feature_1 + ' + ' + label_feature_2, size=30)
    plt.scatter(spoof_feature_1, spoof_feature_2, label="spoof")
    plt.scatter(original_feature_1, original_feature_2, color='yellow', edgecolors='red', label="original")
    plt.legend()
    plt.show()


# In Ipython add option: init_notebook_mode(connected=True)

def makePlotsPlotly(original_feature_1, spoof_feature_1,
                    label_feature_1, label_feature_2):

    trace1 = go.Scatter(x=range(len(original_feature_1)), y = original_feature_1, name=label_feature_1)
    trace2 = go.Scatter(x=range(len(spoof_feature_1)), y = spoof_feature_1, name = label_feature_2)
    iplot([trace1, trace2])


# 3D representation

def plot_figs(fig_num, elev, azim,
              original_feature_1,original_feature_2,original_feature_3,
              spoof_feature_1, spoof_feature_2,spoof_feature_3 ):

    """
    How it works:        
        elev = 43.5
        azim = -110
        plot_figs(1, elev, azim, 
                     original_feature_1,original_feature_2,original_feature_3,
                     spoof_feature_1, spoof_feature_2,spoof_feature_3 )
        
        elev = 20
        azim = -100
        
        plot_figs(2, elev, azim, 
                     original_feature_1,original_feature_2,original_feature_3,
                     spoof_feature_1, spoof_feature_2,spoof_feature_3 )
        
        elev = -.5
        azim = 180
        plot_figs(3, elev, azim)
        
        plt.show()

    """
    fig = plt.figure(fig_num, figsize=(10, 10))
    plt.clf()
    ax = Axes3D(fig, elev=elev, azim=azim)

    ax.scatter(original_feature_1, original_feature_2, original_feature_3, color='red', edgecolor='yellow', marker='^', label='original')
    ax.scatter(spoof_feature_1, spoof_feature_2, spoof_feature_3, marker='o', label='spoof')

    ax.set_xlabel('X')
    ax.set_ylabel('y')
    ax.set_zlabel('Z')
    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    plt.legend()




