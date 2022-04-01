from multiprocessing import Value
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

def Time_duration(G, points_list):

    for i,v in enumerate(G.nodes()):
        G.nodes[v]['state'] = points_list[i].duration
    
    pos = nx.spring_layout(G)
    nx.draw(G,pos)
    node_labels = nx.get_node_attributes(G,'state')
    nx.draw_networkx_labels(G, pos, labels = node_labels)
    return G


def Draw_HTML(points_list):
    
    G = nx.Graph()



    for i in points_list:

        if i.activity == "-" or i.predecessor == "-":
            G.add_node(i.activity)
        else:
            G.add_node(i.activity)
            G.add_node(i.predecessor)
            G.add_edge(i.activity, i.predecessor)


    # time label
    G = Time_duration(G, points_list)


    nt = Network('1000', '1000px')
    nt.from_nx(G)
    nt.show('./HTML/nx.html')