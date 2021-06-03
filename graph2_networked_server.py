'''
Given a map represented by a two-dimensional list, each location has a value of 1 or 0;
1 represents that there is a server at that location, and 0 represents that the location is empty.
For each server, if there are other servers in the same row or column in its location, it is said to be "networked".
find the total number of all networked servers on the map.

Input format:
One line, a two-dimensional nested list given as a valid Python expression

Output format:
One line of integer

Input sample:
[[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

Sample output:
4
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
        self.connectedTo={}

    def addNrb(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

def network(lst):

    g=graph()
    lstRev = list(map(list, zip(*lst)))
    connServer(g,lst,'oScan')
    connServer(g, lstRev,'vScan')


    return g.numVertices

def connServer(graph,lst,scanMode):

    for y,i in enumerate(lst):
        count = 0
        current,pre=None,None
        for x,j in enumerate(i):
            if j==1:
                count+=1
                if count==1:
                    current=(y,x)
                else:
                    pre=current
                    current=(y,x)
                    if scanMode=='oScan':
                        graph.addEdge(pre,current)
                    else:
                        graph.addEdge((pre[1],pre[0]), (x,y))
    return graph



if __name__ == "__main__":
    lst = [[1,0,0,1],[0,0,0,0],[0,0,0,1],[0,0,0,1]]#eval(input())
    print(network(lst))

