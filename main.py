from itertools import product

def combProd(L):
    comb = product(["A","T","C", "G"], repeat = L)
    return comb


def distance(Seq,lmer,L):
    #bestWord = "A"*L
    bestScore = 10000000
    for i in range(0, len(Seq)- L +1):
        mis = 0
        temp =Seq[i:i+L]
        # print(temp, lmre)
        for j in range(L):
            if lmer[j]!=temp[j]:
                mis += 1
        if(bestScore > mis):
            bestScore = mis
            #bestWord = temp
    return bestScore


def totDistance(dna, lmer, L):
    #allComb = []
    totScore = 0 
    for i in dna:
        totScore += distance(i, lmer, L)
        #allComb.append()
        #totScore += tempScore
    return totScore, lmer


def medianString(n,l,t,DNA):
    lmers = combProd(l)
    lmerList = []
    for lm in lmers:
        lmerList.append([totDistance(DNA,lm,l)])
    finalScore = min(lmerList)
    print(finalScore)

m=[
   ['A','T','C','C','A','G','C','T'],
   ['G','G','G','C','A','A','C','T'],
   ['A','T','G','G','A','T','C','T'],
   ['A','A','G','C','A','A','C','C'],
   ['T','T','G','G','A','A','C','T'],
   ['A','T','G','C','C','A','T','T'],
   ['A','T','G','G','C','A','C','T']
   ]

medianString(len(m[0]),4,len(m),m)

