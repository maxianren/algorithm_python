'''
There are n courses to choose, and their numbers are from 0 to n-1
Each course has some prerequisite courses that need to be completed in advance:
For example, if you need to study course 1 before studying course 0, we use a prerequisite relationship pair [0, 1] to represent this relationship
"post-learning course, prerequisite courses"
Given a series of courses and a number of prerequisites, please determine whether there is a plan to complete all courses

Input format:
The input is divided into two lines, the first line is an integer, indicating the total number of courses
The second line is a Python expression of a nested list, containing several prerequisite relation pairs

Output format:
True or False, indicating whether there is an order in which all courses are completed according to the prerequisite relationship

Input sample:
2
[[1,0],[0,1]]

Sample output:
False
'''

#from pythonds.graphs import Graph

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


def canFinish( n, pre):
    g=graph()
    for p in pre:
        frm,to=p[1],p[0]
        g.addEdge(frm,to)

    dicInDegree={vert:0 for vert in g}
    for v in g:
        for toVert in v.connectedTo:
            dicInDegree[toVert]+=1

    Q=[vert for vert in dicInDegree if dicInDegree[vert]==0]
    seq=[]

    while Q:
        outQ=Q.pop()
        seq.append(outQ.id)

        for vert in outQ.connectedTo:
            dicInDegree[vert]-=1
            if dicInDegree[vert]==0:
                Q.append(vert)
    print(seq)
    if len(seq)==n:
        return True
    else:
        return False


    #print([len(node.connectedTo) for node in g])
    # code here




if __name__ == "__main__":
    n = 4#int(input())

    pre = [[2, 0], [2, 1],[3,2],[5,6]] #eval(input())
    print(canFinish(n, pre))

