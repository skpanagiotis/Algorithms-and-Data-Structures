import pprint
import copy
import argparse

# This method takes the txt file and convert it to a list
def filetolist(file):
    input_filename = file
    # the latin-square
    global latin_square
    latin_square = []

    with open(input_filename) as input:
        for line in input:
            lista = [int(x) for x in line.split(", ")]
            latin_square.append(lista)

# This method finds all transversals of a latin square
def find_tranversals ():
    # transversals : a dictionary with KEY the first digit and as VALUES a list with transversals as list
    global transversals
    transversals = {}

    # the stack where we save the numbers to make the transversals
    Stack = []

    # d the dimension of arrays that we control
    global d
    d = len(latin_square)

    # the lines that we have parse
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
            
            # We create series (stacks) which contains a transversal
            for y in range(stili,d):
                # Check for not having the same elements
                for m in range (d):
                    for k in range(len(Stack)):
                        if (Stack[k] == latin_square[m][y] and tf[m][y] == False):
                            tf[m][y] = True

                # search and add the next element
                for x in range (d):
                    if (tf[x][y] == False):
                        Stack.append(latin_square[x][y])
                        energesgrammes.append(x)

                        # We make true the elements in the same serie
                        for u in range (y, d):
                            tf[x][u] = True
                        break
            # Insert a transversal in the list wiht transversals
            if (len(Stack) == d):
                transversals[key].append(list(Stack))

            # Check if we have complete a subset of transversals
            flag_1 = True
            for x in range(d):
                for y in range(d):
                    if (tf[x][y] == False):
                        flag_1 = False
                        break

            if (flag_1 == True):
                break

            # Check if I have made an impossible transversal
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

            # Check the existance of transversals that I have not make
            if (len(Stack) == d):
                stili = d - 1
                o = d - 1 #o : support for columns, I need this for the next calculation
                flag_2 = False

                while(flag_2 == False):
                    trues = 0
                    # Calculate how many TRUEs I have in every column
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

        # We enter here when we change the first element
        # We make transversal with alternative start
        # We clear the stack
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
    # The list with n transversals
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
        for a in range(thesi, len(kleidia)):
            key = kleidia[a]
            star = grammi.get(key) + 1
            tran = transversals.get(key)

            for i in range(star, len(tran)):
                grammi[key] = i
                test = list(tran[i])

                # counter for unique transversals
                plithos_diafor_sind = 0

                for x in listan:
                    plithos_diafor_psif = 0
                    for j in range(1, d):
                        if (test[j] == x[j]):
                            break
                        else:
                            plithos_diafor_psif = plithos_diafor_psif + 1
                    if (plithos_diafor_psif == (d - 1)):
                        plithos_diafor_sind = plithos_diafor_sind + 1
                    else:
                        break

                # The combination satisfies the cases
                # We add the combination on the list
                if (plithos_diafor_sind == len(listan)):
                    listan.append(test)
                    break
            if (len(listan) != a + 1):
                break

        # If I have find x transversals and not n, the I delete some transversals to add another transversals
        if (len(listan) != d):
                grammi[len(listan)] = -1
                thesi = kleidia[len(listan) - 1]
                listan.pop(len(listan) - 1)
        else:
            break

# This method makes an orthogonical square from n - transversals
def final_square():
    tflista = [[False for i in range(d)] for y in range(d)]
    # tetr : the square
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
    # The requirements for the cosnole
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