import pandas as pd
import matplotlib
import matplotlib.backends.backend_svg as svg
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import dendrogram, linkage 


def plot(dat, fname, title):
    dendrogram(linkage(pdist(dat), method="complete"), labels=dat.columns)
    plt.title("Distance Measure: " + title)
    plt.xticks(size=12)
    plt.savefig(fname + ".svg")
    plt.show()

