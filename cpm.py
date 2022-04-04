from Graph_copy import Draw_HTML

from collections import OrderedDict



class point:
    
    def __init__(self, activity, predecessor, next, duration, id):
        self.ES = 0
        self.LS = 1000
        self.EF = 0
        self.LF = 10000
        self.activity = activity
        self.predecessor = predecessor
        self.next = next
        self.duration = int(duration)
        self.id = id
        self.branch = []

    def show(self):
        print(f"Point: {self.id}, activity: {self.activity}, predecessor: {self.predecessor}, next: {self.next} ,duration: {self.duration}")
    
    def show_2(self):
        print(f"Point: {self.activity}, ES: {self.ES}, EF: {self.EF}, LS: {self.LS}, LF: {self.LF},  duration: {self.duration}")

    def set_ES(self, value):
        self.ES = value

    def set_EF(self, value):
        self.EF = value

    def set_LS(self, value):
        self.LS = value

    def set_LF(self, value):
        self.LF = value
    
    def get_ES(self):
        return self.ES

    def get_EF(self):
        return self.EF

    def get_LS(self):
        return self.LS

    def get_LF(self):
        return self.LF

class tree:

    def __init__(self):
        self.lista_pkt = []
        self.start_point = None
        self.end_point = None

        self.max_points = None


    def get_start_point(self):
        return self.start_point
    
    def get_end_point(self):
        return self.end_point

    def add_point(self, point):
        self.lista_pkt.append(point)

    def get_list(self):
        return self.lista_pkt
    
    def show_tree(self):
        for i in self.lista_pkt:
            i.show()

    def show_tree_2(self):
        for i in self.lista_pkt:
            i.show_2()

    def search_list(self, activity):
        for i in self.lista_pkt:
            if i.activity == activity:
                return i



    # funkcja rozwiacujaca problem brancha w prawa strone
    def Branch_Solver_Right(self):
        
        self.max_points = len(self.lista_pkt)

        unique_value_back = {}
        for i in self.lista_pkt:
            if i.activity not in unique_value_back:
                unique_value_back[i.activity] = []


        for j in self.lista_pkt:

            if j.predecessor == "-":
                self.start_point = j
                j.set_EF( j.get_ES() + j.duration )


            else:
                unique_value_back[j.predecessor].append(j.activity)


        print(unique_value_back)
            
        for i in unique_value_back:

            # A
            obiekty = unique_value_back[str(i)]
            main_obj = self.search_list(str(i))
            for z in obiekty:
                tmp = self.search_list(str(z))

                #tmp.ES = main_obj.EF
                #tmp.EF = tmp.ES + tmp.duration

                # tmp.set_ES( main_obj.get_EF())
                # tmp.set_EF( tmp.get_ES() + tmp.duration )

                if tmp.get_ES() < main_obj.get_EF():
                    tmp.set_ES( main_obj.get_EF())
                    tmp.set_EF( tmp.get_ES() + tmp.duration )
                else:
                    continue

        # szukanie najwiekszego czyli ostatniego wyniku
        # maximum = 0
        # for m in self.lista_pkt:
        #     if m.get_EF() > maximum:
        #         maximum = m.get_EF()
        #         self.end_point = m
        #     else:
        #         continue

        # self.end_point.set_LF(maximum)
        # self.end_point.set_LS(maximum - self.end_point.duration)
        # print("hhh", self.end_point.show_2())
        low = 0
        obiekt = None
        for zxc in self.lista_pkt:
            if low < zxc.get_EF():
                low = zxc.get_EF()
                obiekt = zxc
        self.end_point = obiekt

        self.end_point.set_LF(low)
        self.end_point.set_LS(low - self.end_point.duration)

        return self.end_point


                
    def Branch_Solver_Left(self, end_point):

        unique_value_back = {}
        for i in self.lista_pkt:
            if i.activity not in unique_value_back:
                unique_value_back[i.activity] = []
        
        for j in self.lista_pkt:
            unique_value_back[j.activity].append(j.predecessor)



        unique_value_back = OrderedDict(reversed(list(unique_value_back.items())))


        # for i in unique_value_back:

        #     print(i)
        #     obiekty = unique_value_back[str(i)]
        #     main_obj = self.search_list(str(i))


        #     for z in obiekty:
        #         if z == "-":
        #             continue

        #         tmp = self.search_list(str(z))
        #         print(tmp.activity)

        #         tmp.set_LF(main_obj.get_LS())
        #         tmp.set_LS(tmp.get_LF() - tmp.duration)

                    




        print("--- sprawdzam ---")
        minim = 0
        for i in unique_value_back:

            obiekty = unique_value_back[str(i)]
            main_obj = self.search_list(str(i))
            #print("To jest i: ", i)
            #print(main_obj.show_2())

            for z in obiekty:
                print("----")

                if z == '-':
                    continue
                print(z)
                print(main_obj.activity)
                tmp = self.search_list(str(z))
                print("----")

                print("Wartosci maina: ", main_obj.get_LS())
                print("Wartosci tmp: ", tmp.get_LF())

                if main_obj.get_LS() < tmp.get_LF():
                    tmp.set_LF(main_obj.get_LS())
                    tmp.set_LS( tmp.get_LF() - tmp.duration)

        
        print("co tu sie")
        self.start_point.show_2()
        print("minim", minim)
        #self.start_point.set_LF(minim)
        self.start_point.set_LS(self.start_point.get_LF() - self.start_point.duration)






def cpm(data_list):

    # tree create
    test = tree()

    #print(data_list)
    # add points 
    for j,i in enumerate(data_list):
        p = point(i[0], i[1], i[2],i[3], j)
        test.add_point(p)

    # p1 = point("A", "-", 3, 0)
    # p2 = point("B", "A", 4, 1)
    # p3 = point("C", "A", 2, 2)
    # p4 = point("D", "C", 2, 2)

    # test.add_point(p1)
    # test.add_point(p2)
    # test.add_point(p3)
    # test.add_point(p4)

    test.show_tree()
    end = test.Branch_Solver_Right()
    test.show_tree_2()
    test.Branch_Solver_Left(end)
    test.show_tree_2()

    for z in test.lista_pkt:
        if z.ES == 0 and z.EF == 0 and z.LS == 0 and z.LF == 0:
            test.lista_pkt.remove(z)

    CPM_TEST = []
    for z in test.lista_pkt:
        if z.EF == z.LF:
            CPM_TEST.append(z)

    print("new")
    for m in CPM_TEST:
        print(m.activity)

    
    test.show_tree_2()







    print("Draw HTML")
    Draw_HTML(test.get_list(), CPM_TEST, test)









