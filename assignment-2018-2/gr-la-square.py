import pprint
import copy
import argparse

# This method takes the txt file and convert it to list
def filetolist(file):
    input_filename = file
    #to latin-square
    global latin_square
    latin_square = []

    with open(input_filename) as input:
        for line in input:
            lista = [int(x) for x in line.split(", ")]
            latin_square.append(lista)

# This method finds all transversals of a latin square
def find_tranversals ():
    #transversals ena dictionary me key to proto psifio ton diasxiseon kai value mia lista me tis diasxiseis os lista
    global transversals
    transversals = {}
    #h stoiva pou mpenoun oi airithmoi gia na ginei h diasxisi
    Stack = []
    #d h diasstasi ton pinakon pou diaxirizomaste
    global d
    d = len(latin_square)
    #oi grammes pou exoume perasei
    energesgrammes = []
    for i in range(len(latin_square)):
        tf = [[False for i in range(d)] for y in range(d)]  # a true - false array
        Stack.append(latin_square[i][0])
        key = latin_square[i][0]
        transversals [key]= []
        energesgrammes.append(i)
        for j in range(d):
            tf[i][j] = True
            tf[j][0] = True
        flag_1 = False
        stili = 1
        while(flag_1 == False):
            # dhmiourgei seires (stacks) pou perilamvanei mia diasxisi
            for y in range(stili,d):
                # elegxos na min einai idia ta stoixeia
                for m in range (d):
                    for k in range(len(Stack)):
                        if (Stack[k] == latin_square[m][y] and tf[m][y] == False):
                            tf[m][y] = True
                # psaxnei kai vazei to epomeno stoixeio
                for x in range (d):
                    if (tf[x][y] == False):
                        Stack.append(latin_square[x][y])
                        energesgrammes.append(x)
                        # ta stoixeia tis idia grammis ta kanei true
                        for u in range (y, d):
                            tf[x][u] = True
                        break
            #vazei mia diasxisi pou vrike sti lista me tis diasxiseis
            if (len(Stack) == d):
                transversals[key].append(list(Stack))
            # elegxos mipos teliosame apo ena iposinolo diasxiseon
            flag_1 = True
            for x in range(d):
                for y in range(d):
                    if (tf[x][y] == False):
                        flag_1 = False
                        break
            if (flag_1 == True):
                break
            #elegxos an exo ftiaksei diasxisi pou den oloklironete, einai adinati
            if (len(Stack) < d):
                for x in range(d):
                    for y in range(len(Stack), d):
                        if (x != i):
                            tf[x][y] = False
                stili = len(Stack) - 1
                o = len(Stack) - 1
                flag_3 = False
                while (flag_3 == False):
                    trues = 0
                    for p in range(d):
                        if (tf[p][o] == True):
                            trues = trues + 1
                    if (trues == d):
                        for p in range(d):
                            if (p != i):
                                tf[p][o] = False
                        Stack.pop(len(Stack) - 1)
                        energesgrammes.pop(len(energesgrammes) - 1)
                    else:
                        Stack.pop(len(Stack) - 1)
                        energesgrammes.pop(len(energesgrammes) - 1)
                        flag_3 = True
                        break
                    o = o - 1
                    stili = stili - 1
                for h in energesgrammes:
                    for p in range(len(energesgrammes),d):
                        tf[h][p] = True
            #elegxos an iparxei diasxisi pou den exo kanei
            if (len(Stack) == d):
                stili = d - 1
                o = d - 1 #o odigos gia tis stiles ston parakato ipologismo
                flag_2 = False
                while(flag_2 == False):
                    trues = 0
                    # ipologizo se kathe stili posa trues exei
                    for p in range(d):
                        if (tf[p][o] == True):
                            trues = trues + 1
                    if (trues == d):
                        for p in range(d):
                            if (p != i):
                                tf[p][o] = False

                        Stack.pop(len(Stack) - 1)
                        energesgrammes.pop(len(energesgrammes) - 1)
                    else :
                        Stack.pop(len(Stack) - 1)
                        energesgrammes.pop(len(energesgrammes) - 1)
                        flag_2 = True
                        break
                    o = o - 1
                    stili = stili - 1
                for h in energesgrammes:
                    for p in range(len(Stack) + 1,d):
                        tf[h][p] = True

        #edo mpainei otan allazoume proto stoixeio (diasxisi me diaforetiki enarksi adeiazei tin stack)
        if (len(Stack) == d):
            for z in range(d):
                Stack.pop(len(Stack) - 1)
                energesgrammes.pop(len(energesgrammes) - 1)
        else:
            a = len(Stack)
            for x in range(a):
                Stack.pop(len(Stack) - 1)
                energesgrammes.pop(len(energesgrammes) - 1)

# This method finds n-transversals of all transversals
def ntranversals_search():
    #h lista me tis n diasxiseis
    global listan
    listan = []
    kleidia = list(transversals.keys())
    grammi = {x : -1 for x in kleidia}
    flag = False
    thesi = 1
    listan.append(list(transversals.get(kleidia[0])[0]))
    grammi [0] = 0
    star = 0
    while (flag == False):
        #arxiko sindiasmon
        for a in range(thesi, len(kleidia)):
            key = kleidia[a]
            #mesa sto value, lista
            #arxi einai to star
            star = grammi.get(key) + 1
            tran = transversals.get(key)
            for i in range(star, len(tran)):
                grammi[key] = i
                test = list(tran[i])
                #metritis gia ton an oi diasxiseis einai diaforetikes
                plithos_diafor_sind = 0
                for x in listan:
                    plithos_diafor_psif = 0
                    #mesa se diasxisi
                    for j in range(1, d):
                        if (test[j] == x[j]):
                            break
                        else:
                            plithos_diafor_psif = plithos_diafor_psif + 1
                    if (plithos_diafor_psif == (d - 1)):
                        plithos_diafor_sind = plithos_diafor_sind + 1
                    else:
                        break
                #o sindiasmos kaliptei tis ipothesis mas kai mpenei sth listan
                if (plithos_diafor_sind == len(listan)):
                    listan.append(test)
                    break
            if (len(listan) != a + 1):
                break
        #an exo vrei x transversals kai oxi n, tote vgazo orismena transversals gia na valo allo sindiasmo transversals
        if (len(listan) != d):
                grammi[len(listan)] = -1
                thesi = kleidia[len(listan) - 1]
                listan.pop(len(listan) - 1)
        else:
            break

# This method makes an orthogonical square from n - transversals
def final_square():
    tflista = [[False for i in range(d)] for y in range(d)]
    # tetr to orthogonio tetragono
    global tetr
    tetr = copy.deepcopy(latin_square)
    for i in range(d):
        test = list(listan[i])
        psifio = test[0]
        for y in range(d):
            for x in range(d):
                if (tflista[x][y] == False and test[y] == tetr[x][y]):
                    tetr[x][y] = psifio
                    tflista[x][y] = True
                    break

# This method takes the latin - square and its orthogonical square and makes the graeco - latin square
def squares_tograecolatin():
    grecolatin_square = []
    for x in range(d):
        z = list(zip(latin_square[x], tetr[x]))
        grecolatin_square.append(z)
    pprint.pprint(grecolatin_square, width = 100)

# The base of our programm
def main():
    # ta apaitoumena gia thn konsola
    parser = argparse.ArgumentParser()
    parser.add_argument("fn", help = "input_file")

    args = parser.parse_args()
    filename = args.fn

    filetolist(filename)

    lista = []

    if (len(latin_square) == 6 or len(latin_square) == 2):
        pprint.pprint(lista)
    else:
        find_tranversals()
        ntranversals_search()
        final_square()
        squares_tograecolatin()

main()