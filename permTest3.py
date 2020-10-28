from sys import *
from itertools import permutations

allNumbers = '123456789T'
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
    for rule in Rules.keys():
        tmp = sum([gp(x[pos[c]]) for c in rule])
        if(tmp != Rules[rule]): return 0
    return 1

def pList(sum, myList):
    tmpList = []
    for i in range(0, len(myList)-2):
        for j in range(i+1, len(myList)-1):
            for k in range(j+1, len(myList)):
                if gp(myList[i])+gp(myList[j])+gp(myList[k]) == sum:
                    for lst in list(permutations(myList[i]+myList[j]+myList[k])):
                        tmpList.append(lst)
    return tmpList

# A+D+E=18
listADE = pList(18, allNumbers)
for ADE in listADE:
    remainNumbers = allNumbers
    A = ADE[0]
    D = ADE[1]
    E = ADE[2]
    for n in ADE:
        remainNumbers = remainNumbers.replace(n, '')
    pn = [z for z in list(permutations(remainNumbers)) if chk(z, A, D, E)] # 全排列
    if pn != []:
        pn = list(pn[0])
        pn.insert(0, A)
        pn.insert(3, D)
        pn.insert(4, E)
        print(pn)