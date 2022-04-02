import os
from tokenize import Name
import numpy as np
import json
from importlib_metadata import files
import pandas as pd

from cpm import cpm

Folder_Path_Json = "./JSON/"
Folder_Path_Html = "./HTML/"

# laduje jsona
def LOADER(name):
    
    # f = open(name)
    # data = json.load(f)
    df = pd.read_json(name)

    return df

# funkcja wczytujaca pliki z folderu
def listdir_nohidden(path):
    
    tmp = []
    for f in os.listdir(path):
        if not f.startswith('.'):
            if f.endswith('.json'):
                tmp.append(f)
    return tmp


# sprawdzanie istnienia folderu Json
def Json_Folder_Exist():

    if os.path.exists("./JSON/"):
        return True
    else:
        return False

# sprawdzanie istnienia folderu Json
# jezeli nie istnieje stworz go
def Html_Folder_Exist():

    if os.path.exists("./HTML/"):
        return True
    else:
        os.mkdir("./HTML/")



# zmienna wysyla dane w liscie
# do skryptu tworzacego klasy 
data_list = []
def main():
    
    # check json existing
    if Json_Folder_Exist():
        print("Folder JSON exist")
    else:
        print("Folder JSON missing")
        quit()

    # tworzenie folderu/sprawdzenie
    Html_Folder_Exist()

    Json_Name = listdir_nohidden(Folder_Path_Json)[0]
    Full_Path_Json = Folder_Path_Json + Json_Name
    JSON_DATA = LOADER(Full_Path_Json)
    JSON_DATA = pd.DataFrame(JSON_DATA)

    # tworzenie listy z danymi d otworzenia klas 
    for i in JSON_DATA['points']:
        data_list.append([i['start'], i['beforek'], i['finish'], i['value']])


    print("DATA: ", data_list)

    # twqorzenie klas + algorytm 
    cpm(data_list)



if __name__ == "__main__":
    main()