'''
In a small town, N people are marked from 1 to N. There is a rumor that one of these people is a secret judge in the town.

If the judge of the town really exists, then:
 - The judge in the town doesn't believe anyone.
 - Everyone (except the town judge) trusts the town judge.
 - Only one person satisfies Attribute 1 and Attribute 2 at the same time.

Given a list of trust, the list consists of trust pairs trust[i] = [a, b], which means that the person labeled a trusts the person labeled b.
If there is a secret judge in the town and his identity can be determined, please return the judge's mark. Otherwise return -1.

Input format:
The input consists of two lines:
the first line is a positive integer N, the second line is the trust pairs' list, given as a legal Python expression

Output format:
An integer representing the judge’s number

Input sample:
4
[[1,3],[1,4],[2,3],[2,4],[4,3]]

Sample output:
3
'''

class graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0

    def addVert(self,key):
        self.numVertices+=1
        newVertex=vertex(key)
        self.vertList[key]=newVertex
        return newVertex

    def getVert(self,key):
        return self.vertList[key]

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self,frm,to,cost=0):
        if frm not in self.vertList:
            self.addVert(frm)
        if to not in self.vertList:
            self.addVert(to)
        self.vertList[frm].addNrb(self.vertList[to],cost)

    def __iter__(self):
        return iter(self.vertList.values())



class vertex:
    def __init__(self,key):
        self.id=key
        self.connTo={}
        self.connFrom={}

    def addNrb(self,nbr,weight=0):
        self.connTo[nbr.id]=weight
        nbr.connFrom[self.id]=weight



def findJudge(N,trust):
    g=graph()
    for n in range(1,N+1):
        g.addVert(n)

    for t in trust:
        frm=g.vertList[t[0]]
        to=g.vertList[t[1]]
        g.addEdge(frm.id,to.id)

    ifJudge=-1
    for x in g:
        if len(x.connTo)==0 and len(x.connFrom)==N-1:
            ifJudge=x.id

    return ifJudge



if __name__ == "__main__":
    N = 4 #int(input())
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]] #eval(input())
    print(findJudge(N, trust))