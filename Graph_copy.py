from multiprocessing import Value
import webbrowser
from pyvis.network import Network
import pandas as pd
import codecs
from pyvis.network import Network
import networkx as nx
import urllib
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
import random
import cpm

def fil(points_list, CPM_TEST, lista_testowa):

    lista_nowe = []
    for i in points_list:
        if i in CPM_TEST:
            continue
        else:
            lista_nowe.append(i)
    return lista_nowe

def duplikat(points_list):

    lista_dup = []
    lista_dup_2 = []
    for num,i in enumerate(points_list):

        if i.activity not in lista_dup:
            lista_dup.append(i.activity)
        else:
            continue
    
    for n in points_list:
        if n.activity in lista_dup:
            lista_dup_2.append(n)
            lista_dup.remove(n.activity)
        else:
            continue

    for x in lista_dup_2:

        print("Ciekawe czy beda powtorki: ", x.activity)

    return lista_dup_2


def Search(list, name):

    for i in list:
        if i.activity == name:
            return i

def Draw_HTML(points_list, CPM_TEST, test):
   
    CPMTEST_tag = []
    CPMTEST_tag_single = []
    for z in CPM_TEST:
        if z.predecessor == "-":
            continue
        else:
            CPMTEST_tag.append([z.activity, z.predecessor])
            CPMTEST_tag_single.append(z.activity)
   
    print("zxczxc", CPMTEST_tag)
    hmm = points_list
    # usuwanie duplikatow
    points_list = duplikat(points_list)

    lista_testowa = [test.get_start_point(), test.get_end_point()]
    lista_testowa_tagi = [test.get_start_point().activity, test.get_end_point().activity]
    net = Network(notebook=True)
    nowe = fil(points_list, CPM_TEST, lista_testowa)

    for i in nowe:
        print(i.activity)
    print("No se robie graf ta ta tf tf ")
    print(test.get_start_point().activity)
    print(test.get_end_point().activity)

    # poczatek i koniec
    net.add_nodes(
    [test.get_start_point().activity, test.get_end_point().activity],
    label=[test.get_start_point().activity + " start", test.get_end_point().activity+ " end"],
    color=["#3da831", "#3da831",],
    x=[-250, 250],
    y=[1000, 1000]
    )

    for i in CPM_TEST:
        if i.activity in lista_testowa_tagi:
            print("Co tu sie dzieje: ", i.activity)

            continue
        else:
            print("Co tu sie dzieje---: ", i.activity)
            net.add_node(i.activity, label=i.activity, color="#3da831")

    for i in nowe:
        net.add_node(i.activity, label=i.activity, color="#3155a8")







    for i in hmm:
        print(i.activity)
        if i.predecessor == "-":
            continue
        else:
            net.add_edge(i.activity, i.predecessor)



    

    # zx, zy = random.randint(-50,50), random.randint(-50,50)

    # net = Network(notebook=True)

    # net.add_nodes(
    # [0, 1, 2],
    # label=[test.get_start_point().activity, test.get_end_point().activity, "C"],
    # color=["#3da831", "#9a31a8", "#9a31a8"],
    # x=[-50, 50, zx],
    # y=[100, 100, zy]
    # )

    # net.add_edge(0, 1, value=2)
    # net.add_edge(0, 2, value=2)
    # net.add_edge(1, 2, value=2)

    net.save_graph('./HTML/nx.html')
