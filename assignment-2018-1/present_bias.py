import argparse
import copy

# This method takes a .txt file and makes a graph
def filetograph (file):
    input_filename = file

    #graph : the graph with KEY a node and as VALUE the neighbors of KEY node
    global graph
    graph = {}

    #distance : a dictionary with KEY 2 nodes and as VALUE the distance between them
    global distance
    distance = {}

    #destination : a dictionary with KEY a node and as VALUE the nodes that we can go from KEY node
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

# This method takes the graph and finds all the available paths
def searchpath(start, end):
    global paths
    paths = [] #Saving all available paths
    SVis = [] #The Stack as list which include the nodes that we have visited
    visited = {}
    keysli = {} #we use this dictionary for saving keys
    pathsvisited = {}
    keysli = list(graph.keys())

    # Create a dictionary to mark which route we have done
    # for example x node and y node
    # if we have done xy path then ('x y' : True)
    for i in range (len(list(distance.keys()))):
        pathsvisited[list(distance.keys())[i]] = False
    
    # Create a dictionary to mark which node we have visited 
    for i in range(len(graph)):
        visited [keysli[i]] = False
    
    # Start wandering to the graph
    visited[start] = True
    SVis.append(start)
    telos = False
    supvisited = visited

    while (telos == False):
        if (len(SVis) == 0):
            break
        a = SVis.pop(len(SVis) - 1)
        geitones = 0

        for y in list(destination.get(a)):
            if (pathsvisited.get(a + " " + y) == True): #counts the neighbors
                geitones = geitones + 1

            if (geitones == len(destination.get(a))): #makes all neighbors True if we have visited them
                for w in list(destination.get(a)):
                    supvisited[w] = False
                    pathsvisited[a + " " + w] = False
                    visited[w] = False
                break

            if (pathsvisited.get(a + " " + y) == False):
                visited[y] = True
                supvisited[y] = True
                SVis.append(a)
                SVis.append(y)
                pathsvisited[a + " "+ y] = True
                break
                
        # Search and save the path
        if (visited[start] == True and visited[end] == True): #prosthetoyme sth lista mia diadromi
            paths.append(list(SVis))
            supvisited[end] = False
            b = SVis.pop(len(SVis) - 1)
            if (len(SVis) == 0):
                telos = True

        # Search if we have go from start to end with all available options
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

    for i in range(len(paths)):
        lista = list(paths[i])
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
    diadromesvoith = copy.deepcopy(paths)

    for i in range(len(paths)):
        efikta [i] = True
        monopatia.append(int(0))

    telos = False
    komvos = start
    Stackdiadromi.append(komvos)

    # Searching paths with unfairness
    while (Stackdiadromi[len(Stackdiadromi) - 1] != end):
        
        # Paths calculation with unfairness
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

        #Smallest path
        m = min(monopatia)
        thesi = -1
        for i in range(len(monopatia)):
            if (monopatia[i] == m):
                thesi = i

        #go to another node
        for i in range(len(diadromesvoith)):
            if (len(diadromesvoith[i]) > 0 and efikta.get(i) == True):
                diadromesvoith[i].pop(0)
        epomeno = diadromesvoith[thesi][0]

        for i in range(len(diadromesvoith)):
            lista = list(diadromesvoith[i])
            if (lista[0] != epomeno):
                efikta[i] = False

        #Case if we have left one path
        count = 0
        thesief = - 1
        for i in range(len(efikta)):
            if (efikta.get(i) == True):
                count = count + 1
                thesief = i
        if (count == 1):
            break

        Stackdiadromi.append(epomeno)

    #diad : the best path
    diad = list(paths[thesief])

    #thesief : the position of the best path, in lists
    return thesief

#The base of my program
def main():

    #requirements for console
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
    path_1 = list(paths[thesim])
    kostos_1 = int(m)

    thesi_2 = calculate_bdist(start, end, bias)
    path_2 = list(paths[thesi_2])
    kostos_2 = Mikos[thesi_2]

    msg_1 = str(path_1) + " " + str(kostos_1)
    msg_2 = str(path_2) + " " + str(kostos_2)
    print(msg_1)
    print(msg_2)

main()