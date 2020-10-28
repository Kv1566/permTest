from sys import *
from itertools import permutations

gp = lambda c : 10 if c == 'T' else int(c)
pos = {chr(k): k-65 for k in range(65, 75)}

Rules = ({'ACD': 19,
          'DEG': 16,
          'BCF': 11,
          'HGJ': 22,
          'FHI': 17})
          
def chk(x, A, D, E):
    x = list(x)
    x.insert(0, A)
    x.insert(3, D)
    x.insert(4, E)
    #print(x)
    for rule in Rules.keys():
        tmp = sum([gp(x[pos[c]]) for c in rule])
        if(tmp != Rules[rule]): return 0
    return 1

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

def pList(sum, myList):
    tmpList = []
    for i in range(0, len(myList)-2):
        for j in range(i+1, len(myList)-1):
            for k in range(j+1, len(myList)):
                if myList[i]+myList[j]+myList[k] == sum:
                    for list in perm([myList[i], myList[j], myList[k]]):
                        tmpList.append(list)
    return tmpList

gp2 = lambda c : 'T' if c == 10 else str(c)

# A+D+E=18
listADE = pList(18, allNumbers)
for ADE in listADE:
    remainNumbers = allNumbers.copy()
    A = ADE[0]
    sA = gp2(A)
    D = ADE[1]
    sD = gp2(D)
    E = ADE[2]
    sE = gp2(E)
    for n in ADE:
        remainNumbers.remove(n)
    remainNumberString = ''.join(map(str, remainNumbers)).replace('10','T')
    
    pn = [z for z in list(permutations(remainNumberString)) if chk(z, sA, sD, sE)] # 全排列
    if pn != []:
        pn = list(pn[0])
        pn.insert(0, sA)
        pn.insert(3, sD)
        pn.insert(4, sE)
        print(pn)
