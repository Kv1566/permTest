from functools import reduce

allNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def allRotated(list):
    def rotatedTo(i):
        return [list[i]] + list[0:i] + list[i + 1:]
    return [rotatedTo(i) for i in range(len(list))]
   
def perm(list):
    if list == []:
        return [[]]
    else:
        lts = allRotated(list)
        return reduce(lambda a, b: a + b, 
            [[[lt[0]] + pl for pl in perm(lt[1:])] for lt in lts])

def pList3(sum, myList):
    tmpList3 = []
    for i in range(0, len(myList)-2):
        for j in range(i+1, len(myList)-1):
            for k in range(j+1, len(myList)):
                if myList[i]+myList[j]+myList[k] == sum:
                    for list in perm([myList[i], myList[j], myList[k]]):
                        tmpList3.append(list)
    return tmpList3

def pList2(sum, myList):
    tmpList2 = []
    for i in range(0, len(myList)-1):
        for j in range(i+1, len(myList)):
            if myList[i]+myList[j] == sum:
                for list in perm([myList[i], myList[j]]):
                    tmpList2.append(list)
    return tmpList2

# A+D+E=18
listADE = pList3(18, allNumbers)
#listADE
print('A B C D E F G H I J')
for ADE in listADE:
    remainNumbers = allNumbers.copy()
    A = ADE[0]
    D = ADE[1]
    E = ADE[2]
    for n in ADE:
        remainNumbers.remove(n)
    C = 19 - A - D
    if C in remainNumbers:
        remainNumbers.remove(C)
        G = 16 - D - E
        if G in remainNumbers:
            remainNumbers.remove(G)
            if 11 - C >= 3:
                listBF = pList2(11 - C, remainNumbers)
                #print(listBF)
                for BF in listBF:
                    remainNumbers_2 = remainNumbers.copy()
                    B = BF[0]
                    F = BF[1]
                    for n in BF:
                        remainNumbers_2.remove(n)
                    if 22 - G >= 3:
                        listHJ = pList2(22 - G, remainNumbers_2)
                        #print(listHJ)
                        for HJ in listHJ:
                            remainNumbers_3 = remainNumbers_2.copy()
                            H = HJ[0]
                            J = HJ[1]
                            for n in HJ:
                                remainNumbers_3.remove(n)
                            I = 17 - F - H
                            if I in remainNumbers_3:
                                remainNumbers_3.remove(I)
                                #print(remainNumbers_3)
                                print(A, B, C, D, E, F, G, H, I, J)