from Graph import Draw_HTML





class point:
    
    def __init__(self, activity, predecessor, duration, id):
        self.ES = None
        self.LS = None
        self.EF = None
        self.LF = None
        self.activity = activity
        self.predecessor = predecessor
        self.duration = duration
        self.id = id
        self.branch = []

    def show(self):
        print(f"Point: {self.id}, activity: {self.activity}, predecessor: {self.predecessor}, duration: {self.duration}")
    
    

class tree:

    def __init__(self):
        self.lista_pkt = []

    def add_point(self, point):
        self.lista_pkt.append(point)

    def get_list(self):
        return self.lista_pkt
    
    def show_tree(self):
        for i in self.lista_pkt:
            i.show()

    # funkcja rozwiacujaca problem brancha w prawa strone
    def Branch_Solver_Right(self):

        # przechodze po punktach z listy
        # selekcjonuje unikalne punkty tzn [A,B,B,C] = [A,B,C]
        # zapisuje w slowniku? {A:CD, B:AD}
        #  [core: rozwidlenia]
        #  [0: 1,2]

        # dodanie waertosci unikalnych i stworznie wstepnej struktury 
        # { Key: [List]}
        unique_value_back = {}
        for i in self.lista_pkt:
            if i.activity not in unique_value_back:
                unique_value_back[i.activity] = []
        
        for j in self.lista_pkt:
            unique_value_back[j.activity].append(j.predecessor)




        print("Out of loop")
        print(unique_value_back)     
    


def cpm(data_list):

    # tree create
    test = tree()


    # add points 

    p1 = point("A", "-", 3, 0)
    p2 = point("B", "A", 4, 1)
    p3 = point("C", "A", 2, 2)
    p4 = point("D", "C", 2, 2)

    test.add_point(p1)
    test.add_point(p2)
    test.add_point(p3)
    test.add_point(p4)

    test.show_tree()
    test.Branch_Solver_Right()

    print("Draw HTML")
    Draw_HTML(test.get_list())









