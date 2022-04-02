from multiprocessing import Value
import webbrowser
from pyvis.network import Network
import pandas as pd
import codecs
from pyvis.network import Network
import networkx as nx
import urllib
import matplotlib.pyplot as plt

def Draw_HTML(points_list, CPM_TEST):
    
    G = nx.Graph()


    for i in points_list:

        if i.activity == "-" or i.predecessor == "-" or i.next == "-":
            G.add_node(i.activity)
        else:
            G.add_node(i.activity)
            G.add_node(i.predecessor)
            G.add_node(i.next)

            G.add_edge(i.activity, i.predecessor)
            G.add_edge(i.activity, i.next)



    color_map = []
    temporary = []
    for z in CPM_TEST:
        temporary.append(str(z.activity))

    for node in G:
        if node in temporary:
            color_map.append('#ff0000')
        else:
            color_map.append('#6699ff')





    nt = Network('500', '500px')
    nx.draw(G, node_color=color_map, with_labels=True)
    plt.show()
    nt.from_nx(G)
    nt.save_graph('./HTML/nx.html')