from multiprocessing import Value
import webbrowser
from pyvis.network import Network
import pandas as pd
import codecs
from pyvis.network import Network
import networkx as nx
import urllib


def Draw_HTML(points_list):
    
    G = nx.Graph()



    for i in points_list:

        if i.activity == "-" or i.predecessor == "-":
            G.add_node(i.activity)
        else:
            G.add_node(i.activity)
            G.add_node(i.predecessor)
            G.add_edge(i.activity, i.predecessor)




    nt = Network('500', '500px')
    nt.from_nx(G)
    nt.save_graph('./HTML/nx.html')