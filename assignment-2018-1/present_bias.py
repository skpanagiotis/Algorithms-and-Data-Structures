import argparse
import copy

# This method takes a file and makes a graph and save the distances and destination
def filetograph (file):
    input_filename = file
    #graph o grafos mas me key ton enan komvo kai values tous geitones komvous
    global graph
    graph = {}
    #distance ena dictionary me key 2 komvous kai value h apostasi metaksi tous
    global distance
    distance = {}
    #destination ena dictionary me key enan komvo kai value tous komvous pou mporoume na pame apo to kombo key
    global destination
    destination = {}
    with open(input_filename) as graph_input:
        for line in graph_input:
            nodes = [str(x) for x in line.split()]
            nodesdist = [str(x) for x in line.split()]
            c = nodesdist.pop(2)
            b = nodesdist.pop(1)
            a = nodesdist.pop(0)
            if (str(destination.get(a)) == 'None'):
                destination.setdefault(str(a), []).append(str(b))
            else :
                destination.setdefault(str(a), []).append(str(b))
            distance[str(a) + " " + str(b)] = int(c)
            nodes.pop(2)

            if len(nodes) != 2:
                continue
            if nodes[0] not in graph:
                graph[nodes[0]] = []
            if nodes[1] not in graph:
                graph[nodes[1]] = []
            graph[nodes[0]].append(nodes[1])
            graph[nodes[1]].append(nodes[0])

# This method takes the graph and find all the available paths
def searchpath(start, end):
    global diadromes
    diadromes = [] #apothikevonte oi efiktes diadromes
    SVis = [] #The Stack as list which include the nodes that we have visited
    visited = {}
    keysli = {} #xrisimopoiete gia tin apothikefsi ton klidion
    diadromesvisited = {}
    keysli = list(graph.keys())
    #dimiourgia dictionary gia to pies diadromes exoume kanei px ('s t' : False)
    for i in range (len(list(distance.keys()))):
        diadromesvisited[list(distance.keys())[i]] = False
    #dhmiourgia dicitonary gia to pious komvous episkeptomaste
    for i in range(len(graph)):
        visited [keysli[i]] = False
    # enarksi periplanisis stous komvous
    visited[start] = True
    SVis.append(start)
    telos = False
    boithvisited = visited
    while (telos == False):
        if (len(SVis) == 0):
            break
        a = SVis.pop(len(SVis) - 1)
        geitones = 0
        for y in list(destination.get(a)):
            if (diadromesvisited.get(a + " " + y) == True): #metraei gitones
                geitones = geitones + 1
            if (geitones == len(destination.get(a))): #kanei olous tou geitones tou false an tous exoume episkefti
                for w in list(destination.get(a)):
                    boithvisited[w] = False
                    diadromesvisited[a + " " + w] = False
                    visited[w] = False
                break
            if (diadromesvisited.get(a + " " + y) == False):
                visited[y] = True
                boithvisited[y] = True
                SVis.append(a)
                SVis.append(y)
                diadromesvisited[a + " "+ y] = True
                break
        #ebresi kai kataxorisi monopatiou
        if (visited[start] == True and visited[end] == True): #prosthetoyme sth lista mia diadromi
            diadromes.append(list(SVis))
            boithvisited[end] = False
            b = SVis.pop(len(SVis) - 1)
            if (len(SVis) == 0):
                telos = True

        #ekserevnisi an exoume paei apo to start sto end me olous tous efiktous tropous
        listakleidiavis = list(visited.keys())
        episkepsi = 0
        for x in range(len(listakleidiavis)):
            klidi = listakleidiavis[x]
            if (visited.get(klidi) == True):
                episkepsi = episkepsi + 1
        if (episkepsi == len(visited)):
            telos = True

#This method calculates the distance for every path
def calculate_dist():
    global Mikos
    Mikos = []

    for i in range(len(diadromes)):
        lista = list(diadromes[i])
        sum = 0
        for j in range(len(lista) - 1):
            a = lista[j]
            b = lista[j + 1]
            sum = sum + int(distance.get(a + " " + b))
        Mikos.append(sum)

#This method calculates the distance with parameter b
def calculate_bdist(start, end, bias):
    Stackdiadromi = []
    monopatia = []
    diadromesvoith = []
    efikta = {}
    diadromesvoith = copy.deepcopy(diadromes)
    for i in range(len(diadromes)):
        efikta [i] = True
        monopatia.append(int(0))
    telos = False
    komvos = start
    Stackdiadromi.append(komvos)
    #anazitisi monopation me merolipsia
    while (Stackdiadromi[len(Stackdiadromi) - 1] != end):
        #ipologismos monopation me meropsia
        for k in range(len(diadromesvoith)):
            if (efikta[k] == True):
                lista = list(diadromesvoith[k])
                sum = 0
                for j in range(len(lista) - 1):
                    a = lista[j]
                    b = lista[j + 1]
                    if (j == 0):
                        prosthesi = int(distance.get(a + " " + b))
                    else:
                        prosthesi = bias * int(distance.get(a + " " + b))
                    sum = sum + prosthesi
                monopatia[k] = sum
        #mikrotero monopati
        m = min(monopatia)
        thesi = -1
        for i in range(len(monopatia)):
            if (monopatia[i] == m):
                thesi = i
        #metafora se epomeno komvo
        for i in range(len(diadromesvoith)):
            if (len(diadromesvoith[i]) > 0 and efikta.get(i) == True):
                diadromesvoith[i].pop(0)
        epomeno = diadromesvoith[thesi][0]
        for i in range(len(diadromesvoith)):
            lista = list(diadromesvoith[i])
            if (lista[0] != epomeno):
                efikta[i] = False
        #periptosi an exei minei ena monopati
        count = 0
        thesief = - 1
        for i in range(len(efikta)):
            if (efikta.get(i) == True):
                count = count + 1
                thesief = i
        if (count == 1):
            break

        Stackdiadromi.append(epomeno)
    #diad to kalitero monopati
    diad = list(diadromes[thesief])
    #thesief h thesi stis listes, tou monopatiou
    return thesief

#The base of my program
def main():
    #apaitoumena gia konsola
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", help = "input_file")
    parser.add_argument("b", type = float, help = "bias_parameter")
    parser.add_argument("s", type = str, help = "start_node")
    parser.add_argument("e", type = str, help = "end_node")

    args = parser.parse_args()
    filename = args.fn
    bias = args.b
    start = args.s
    end = args.e

    filetograph(filename)
    searchpath(start,end)

    calculate_dist()
    m = Mikos[0]
    thesim = 0
    for i in range(1, len(Mikos)):
        if (Mikos[i] < m):
            m = Mikos[i]
            thesim = i
    path_1 = list(diadromes[thesim])
    kostos_1 = int(m)

    thesi_2 = calculate_bdist(start, end, bias)
    path_2 = list(diadromes[thesi_2])
    kostos_2 = Mikos[thesi_2]

    msg_1 = str(path_1) + " " + str(kostos_1)
    msg_2 = str(path_2) + " " + str(kostos_2)
    print(msg_1)
    print(msg_2)

main()