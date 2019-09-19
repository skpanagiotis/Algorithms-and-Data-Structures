import copy
import sys

#The base of my program
def main():
    #ta apaitoumena gia tin konsola
    data = ""
    for i in range(1, len(sys.argv)):
        data = data + sys.argv[i] + " "
    #oi arithmoi pou vazei o xristis
    decimal = list(data.split())
    #oi diadikoi arithmoi pou vgenoun apo tous arithmous tou xristi
    global bstack
    bstack = []
    for i in range(len(decimal)):
        bstack.append(str("{0:04b}".format(int(decimal[i]))))

    norm_maker()
    search()
    if (apotelesma == "1"):
        print(apotelesma)
    else:
        print(calculation())

#This method constructs the norm
def norm_maker():
    global norma
    norma = [[0 for i in range(4)] for j in range(4)]
    x = ["00", "01", "11", "10"]
    y = x
    for k in range(len(bstack)):
        a = bstack[k][:2]
        b = bstack[k][2:]
        for i in range(len(x)):
            if (a == x[i]):
                for j in range(len(y)):
                    if (b == y[j]):
                        norma[j][i] = 1

#This methos search for eights, fours, twos ,ones
def search():
    global apotelesma
    apotelesma = ""
    #oi oktades
    global eights
    eights = []
    #oi tetrades
    global fours
    fours = []
    #oi diades
    global twos
    twos = []
    #o pinakas pou perilamvanei tis theseis ton monadon
    global ones
    ones = []
    for i in range(4):
        for j in range(4):
            if (norma[i][j] == 1):
                ones.append(str(i)+" "+str(j))
    #elegxos an olos o pinakas perilamvanetai apo monades
    if (len(ones) == 16):
        apotelesma = "1"
        return

    #PSAKSIMO GIA 8 kai xorismo apo to an iparxoun 4 katheta h' orizontia
    orizontia = []
    katheta = []
    for i in range(4):
        oplithos = 0
        kplithos = 0
        for x in ones:
            if (x[0] == str(i)):
                oplithos = oplithos + 1
            if (x[2] == str(i)):
                kplithos = kplithos + 1
        if (oplithos == 4):
            orizontia.append(i)
        if (kplithos == 4):
            katheta.append(i)

    #orizontia
    if (len(orizontia) > 1):
        for x in orizontia:
            flag = False
            for y in orizontia:
                if(abs(x - y) == 1 or abs(x - y) == 3):
                    flag = True
                    alista = []
                    blista = []
                    for a in range(4):
                        alista.append(str(x)+" "+str(a))
                        blista.append(str(y)+" "+str(a))

                    eights.append(alista + blista)
                    break

            if (flag == True):
                orizontia.remove(x)
                orizontia.remove(y)
                break
            else:
                lista = []
                for a in range(4):
                    lista.append(str(x) + " " + str(a))
                fours.append(lista)
                orizontia.remove(x)
    if (len(orizontia) == 1):
        lista = []
        for a in range(4):
            lista.append(str(orizontia[0]) + " " + str(a))
        fours.append(lista)

    #kahteta
    if (len(katheta) > 1):
        for x in katheta:
            flag = False
            for y in katheta:
                if (abs(x - y) == 1 or abs(x - y) == 3):
                    flag = True
                    alista = []
                    blista = []
                    for a in range(4):
                        alista.append(str(a) + " " + str(x))
                        blista.append(str(a) + " " + str(y))

                    eights.append(alista+blista)
                    break
            if (flag == True):
                katheta.remove(x)
                katheta.remove(y)
                break
            else:
                lista = []
                for a in range(4):
                    lista.append(str(a) + " " + str(x))
                    fours.append(lista)
                katheta.remove(x)
    if (len(katheta) == 1):
        lista = []
        for a in range(4):
            lista.append(str(a) + " " + str(katheta[0]))
        fours.append(lista)

    #PSAKSIMO GIA 4 (gia stiles kai grammes me 4 exei ginei apo to psaksimo gia 8)

    #kratao ksexorista tis tetrades pou einai grammes h' stiles
    foursfrom8 = copy.deepcopy(fours)

    fours = []

    # kratao ta kelia pou einai h oktada gia na min ta kalipso
    testeights = []
    for i in range(len(eights)):
        for j in range(len(eights[i])):
            # o pinakas pou exei kalipsei tin oktada
            testeights.append(eights[i][j])

    # eksafanizei ta diplotipa
    testeights = list(set(testeights))

    #PSASKIMO GIA STIS 4 GONIES
    plithos = 0
    plithos8 = 0
    for x in ones:
        if (x == "0 0" or x == "0 3" or x == "3 0" or x == "3 3"):
            plithos = plithos + 1
    if (plithos == 4):
        for a in testeights:
            if (a == "0 0" or a == "0 3" or a == "3 0" or a == "3 3"):
                plithos8 = plithos8 + 1
        if (plithos8 < 4):
            fours.append(["0 0", "0 3", "3 0", "3 3"])

    #PSAKSIMO GIA TA APENANTI
    #psaksimo gia apenanti katheta
    for i in range(3):
        plithos = 0
        akeli = str(i)+" "+"0"
        bkeli = str(i + 1)+" "+"0"
        ckeli = str(i) + " " + "3"
        dkeli = str(i + 1) + " " + "3"
        for x in ones:
            if (x == akeli or x == bkeli or x == ckeli or x == dkeli):
                plithos = plithos + 1
        if (plithos == 4):
            plithos8 = 0
            for a in testeights:
                    if (a == akeli or a == bkeli or a == ckeli or a == dkeli):
                        plithos8 = plithos8 + 1
            if (plithos8 < 4):
                fours.append([akeli, bkeli, ckeli, dkeli])

    #psaksimo gia apenanti orizontia
    for i in range(3):
        plithos = 0
        akeli = "0"+" "+str(i)
        bkeli = "0"+" "+str(i + 1)
        ckeli = "3"+" "+str(i)
        dkeli = "3"+" "+str(i + 1)
        for x in ones:
            if (x == akeli or x == bkeli or x == ckeli or x == dkeli):
                plithos = plithos + 1
        if (plithos == 4):
            plithos8 = 0
            for a in testeights:
                if (a == akeli or a == bkeli or a == ckeli or a == dkeli):
                    plithos8 = plithos8 + 1
            if (plithos8 < 4):
                fours.append([akeli, bkeli, ckeli, dkeli])

    #PSAKSIMO GIA TETRAGONA
    for i in range(3):
        for j in range(3):
            testkeli = [str(i)+" "+str(j), str(i + 1)+" "+str(j), str(i)+" "+str(j + 1), str(i + 1)+" "+str(j + 1)]
            plithos = 0
            for keli in testkeli:
                for a in ones:
                    if (keli == a):
                        plithos = plithos + 1
            if (plithos == 4):
                plithos8 = 0
                for keli in testkeli:
                    for a in testeights:
                        if (keli == a):
                            plithos8 = plithos8 + 1
                if (plithos8 < 4):
                    fours.append(testkeli)

    #afairesi ton kelion pou exo kalipsei apo tetrades kai oktades
    #otan teleioso me tin anazitisi oktadon tetradon kai diadon STO TESTONES THA PERIEXEI TA MONA KELIA
    global testones
    testones = copy.deepcopy(ones)

    #kratao ta kelia pou einai oi tetrades gia na ta diagrapso
    testfours = []
    for i in range(len(fours)):
        for j in range(len(fours[i])):
            testfours.append(fours[i][j])

    #eksafanizei ta diplotipa
    testfours = list(set(testfours))

    # *elegxo gia na do an tha valo tis tetrades pou einai se grammi h' stili
    for i in range(len(foursfrom8)):
        plithos = 0
        for j in range(len(foursfrom8[i])):
            for x in testfours:
                if (x == foursfrom8[i][j]):
                    plithos = plithos + 1
        if (plithos < 4):
            fours.append(foursfrom8[i])
            testfours.append(foursfrom8[i][0])
            testfours.append(foursfrom8[i][1])
            testfours.append(foursfrom8[i][2])
            testfours.append(foursfrom8[i][3])

    #monadikotita kai meta ton elegxo
    #eksafanizei ta diplotipa
    testfours = list(set(testfours))

    #AFAIRO ta kelia pou einai oktades kai tetrades
    for i in testeights:
        if i in testones:
            testones.remove(i)
    for i in testfours:
        if i in testones:
            testones.remove(i)

    #PSAKSIMO GIA DIADES

    #psaksimo orizontia
    for i in range(4):
        for j in range(3):
            akeli = str(i)+" "+str(j)
            bkeli = str(i)+" "+str(j+1)
            plithos2 = 0
            for x in testones:
                if (x == akeli or x == bkeli):
                    plithos2 = plithos2 + 1

            if (plithos2 == 2):
                twos.append([akeli, bkeli])

    # psaksimo katheta
    for j in range(4):
        for i in range(3):
            akeli = str(i) + " " + str(j)
            bkeli = str(i + 1) + " " + str(j)
            plithos2 = 0
            for x in testones:
                if (x == akeli or x == bkeli):
                    plithos2 = plithos2 + 1

            if (plithos2 == 2):
                twos.append([akeli, bkeli])

    #afairesi ton diadon
    testtwos = []
    for i in range(len(twos)):
        for j in range(len(twos[i])):
            testtwos.append(twos[i][j])
    for x in testtwos:
        if x in testones:
            testones.remove(x)

#This method finds the result
def calculation():
    b = ["00", "01", "11", "10"]
    G = "ABCD"
    #to teliko apotelesma
    telikoapotelesma = ""
    #plithos elaxistooron
    plelax = 0
    apotelesma = ""
    grammata = {}
    sindiasmos = []
    #GIA TIS OKTADES
    for i in range(len(eights)):
        pinakas = []
        for j in range(len(eights[i])):
            a = eights[i][j]
            pinakas.append(b[int(a[2])] + b[int(a[0])])
        for k in range(4):
            temp = pinakas[0][k]
            plithos = 1
            for l in range(1, len(pinakas)):
                if (temp == pinakas[l][k]):
                    plithos = plithos + 1
            if (plithos == len(pinakas)):
                if (temp == "0"):
                    grammata[G[k]] = "~"
                else:
                    grammata[G[k]] = ""
                break
    keys = sorted(list(grammata.keys()))
    for x in keys:
        plelax = plelax + 1
        if (grammata.get(x) == "~"):
            apotelesma ="~"+x
        else:
            apotelesma = x
        sindiasmos.append(apotelesma)
    sindiasmos = sorted(sindiasmos)

    for x in sindiasmos:
        telikoapotelesma = telikoapotelesma + x + " " + "\u2228" + " "

    #GIA TIS TETRADES
    grammata = {}
    sindiasmos = []
    for i in range(len(fours)):
        pinakas = []
        for j in range(len(fours[i])):
            a = fours[i][j]
            pinakas.append(b[int(a[2])] + b[int(a[0])])
        for k in range(4):
            temp = pinakas[0][k]
            plithos = 1
            for l in range(1, len(pinakas)):
                if (temp == pinakas[l][k]):
                    plithos = plithos + 1
            if (plithos == len(pinakas)):
                if (temp == "0"):
                    grammata[G[k]] = "~"
                else:
                    grammata[G[k]] = ""
        keys = sorted(list(grammata.keys()))
        apotelesma = ""
        for x in keys:
            plelax = plelax + 1
            if (grammata.get(x) == "~"):
                apotelesma = apotelesma + "~" + x
            else:
                apotelesma = apotelesma + x
        sindiasmos.append(apotelesma)
        grammata = {}
    sindiasmos = sorted(sindiasmos)

    for x in sindiasmos:
        telikoapotelesma = telikoapotelesma + x + " " + "\u2228" + " "

    #GIA TIS DIADES
    grammata = {}
    sindiasmos = []
    for i in range(len(twos)):
        pinakas = []
        for j in range(len(twos[i])):
            a = twos[i][j]
            pinakas.append(b[int(a[2])] + b[int(a[0])])
        for k in range(4):
            temp = pinakas[0][k]
            plithos = 1
            for l in range(1, len(pinakas)):
                if (temp == pinakas[l][k]):
                    plithos = plithos + 1
            if (plithos == len(pinakas)):
                if (temp == "0"):
                    grammata[G[k]] = "~"
                else:
                    grammata[G[k]] = ""
        keys = sorted(list(grammata.keys()))
        apotelesma = ""
        for x in keys:
            plelax = plelax + 1
            if (grammata.get(x) == "~"):
                apotelesma = apotelesma + "~" + x
            else:
                apotelesma = apotelesma + x
        sindiasmos.append(apotelesma)
        grammata = {}
    sindiasmos = sorted(sindiasmos)

    for x in sindiasmos:
        telikoapotelesma = telikoapotelesma + x + " " + "\u2228" + " "

    #GIA TA MONADIKA KELIA
    grammata = {}
    sindiasmos = []
    for i in range(len(testones)):
        a = testones[i]
        stoixeio = b[int(a[2])] + b[int(a[0])]
        for k in range(4):
            if (stoixeio[k] == "0"):
                grammata[G[k]] = "~"
            else:
                grammata[G[k]] = ""
        keys = sorted(list(grammata.keys()))
        apotelesma = ""
        for x in keys:
            plelax = plelax + 1
            if (grammata.get(x) == "~"):
                apotelesma = apotelesma + "~" + x
            else:
                apotelesma = apotelesma + x
        sindiasmos.append(apotelesma)
        grammata = {}
    sindiasmos = sorted(sindiasmos)

    for x in sindiasmos:
        telikoapotelesma = telikoapotelesma + x + " " + "\u2228" + " "

    telikoapotelesma = telikoapotelesma[:-2] + str(plelax)

    return(telikoapotelesma)

main()