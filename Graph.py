import webbrowser
from pyvis.network import Network
import pandas as pd
import codecs
from pyvis.network import Network
import networkx as nx
import urllib

# nx_graph = nx.cycle_graph(10)
# nx_graph.nodes[1]['title'] = 'Number 1'
# nx_graph.nodes[1]['group'] = 1
# nx_graph.nodes[3]['title'] = 'I belong to a different group!'
# nx_graph.nodes[3]['group'] = 10
# nx_graph.add_node(20, size=20, title='couple', group=2)
# nx_graph.add_node(21, size=15, title='couple', group=2)
# nx_graph.add_edge(20, 21, weight=5)
# nt = Network('1000', '1000px')
# nt.from_nx(nx_graph)
# nt.show('nx.html')

def Draw_HTML(points_list):
    
    G = nx.Graph()



    for i in points_list:

        if i.activity == "-" or i.predecessor == "-":
            G.add_node(i.activity)
        else:
            G.add_node(i.activity)
            G.add_node(i.predecessor)
            G.add_edge(i.activity, i.predecessor)





    #nx_graph = nx.Graph()
    # nx_graph = nx.path_graph()
    # nx_graph.add_node("Sample")
    # nx_graph.add_node("Hello")


    nt = Network('1000', '1000px')
    nt.from_nx(G)
    nt.show('nx.html')