'''
You now have a "map" grid of size M x N in your hand. Each "area" (cell) on it is marked with 0 and 1.
Where 0 represents the ocean and 1 represents the land
For each ocean grid, there is a land grid closest to it, and correspondingly there is a minimum distance to land
Please output the maximum of all the above minimum distances.

The distance we are talking about here is the "Manhattan Distance": the distance between (x0, y0) and (x1, y1) is |x0-x1| + |y0-y1|.
If there is only land or sea on the map, please return -1.

Input format:
Input a total of 1 line, which is a nested list containing only 0 and 1, given by a legal Python expression

Output format:
An integer representing the shortest distance

Input sample:
[[1,0,1],[0,0,0],[1,0,1]]

Sample output:
2
Note: The coordinates of the farthest ocean area are (1,1)
'''

'''
def maxDistance(grid):

    res_dic={}
    # create a map
    width=len(grid[0])
    depth=len(grid)
    for x,i in enumerate(grid):
        for y,j in enumerate(i):
            if j ==0:
                iterLimit = max(x, depth - x-1, y, width - y-1)
                #print((x,y),iterLimit,res_dic)

                count=1
                found=False
                while count<=iterLimit and not found:

                    searchLst=searchRange(x,y,depth,width,count)

                    for s in searchLst:
                        _x,_y=s[0],s[1]
                        if grid[_x][_y] == 1:
                            dist = abs(_x - x) + abs(y - _y)
                            if (x, y) not in res_dic or dist < res_dic[(x, y)]:
                                res_dic[(x, y)] = dist
                            found = True
                            # print((x,y),(_x,_y),grid[_x][_y], found,'x,y:',top,bottom,left,right,res_dic)

                    count+=1
                if (x,y) not in res_dic:
                    res_dic[(x, y)]=-1

    if res_dic:
        return max(res_dic.values())
    else:
        return -1

def searchRange(x,y,depth,width,count):
    top, bottom = x - count, x+count+1
    left, right = y - count, y+count+1
    searchLst=[]
    for i in range(top,bottom):
        for j in range(left , right ):
            if i >=0 and i<depth and j >= 0 and j < width:
                if i==top or i==depth-1:
                    searchLst.append((i,j))
                else:
                    if j==left or j==right-1:
                        if i == top or i == bottom - 1:
                            searchLst.append((i, j))
                        else:
                            if j == left or j == right - 1:
                                searchLst.append((i, j))

    #print((x,y),'count: ',count,searchLst)
    return searchLst
'''

'''
class graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0

    def addVert(self,key,value=0):
        self.numVertices+=1
        newVertex=vertex(key,value)
        self.vertList[key]=newVertex
        return newVertex

    def getVert(self,key):
        return self.vertList[key]

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self,frm,f_value,to,t_value,cost=0):
        if frm not in self.vertList:
            self.addVert(frm,f_value)
        if to not in self.vertList:
            self.addVert(to,t_value)
        self.vertList[frm].addNrb(self.vertList[to],cost)

    def __iter__(self):
        return iter(self.vertList.values())



class vertex:
    def __init__(self,key,value,status=None,dist=0):
        self.id=key
        self.val=value
        self.connTo={}
        self.distance=dist
        self.status=status
        #self.connFrom={}

    def addNrb(self,nbr,weight=0):
        self.connTo[nbr.id]=weight
        #nbr.connFrom[self.id]=weight


def maxDistance(grid):
    distGraph=createGraph(grid)
    resList=[]
    for vert in distGraph:
        if vert.val==0:
            distGraph=clearMark(distGraph)
            vert.distance = 0
            vertQueue = []
            vertQueue.append(vert)
            found = False

            while len(vertQueue) > 0 and not found:
                currentVert = vertQueue.pop(0)
                for Nbr in currentVert.connTo:

                    Nbr = distGraph.getVert(Nbr)
                    if Nbr.status==None:
                        Nbr.status = 'mark'
                        Nbr.distance = currentVert.distance + 1
                        vertQueue.append(Nbr)
                        if Nbr.val == 1:
                            found = True
                            resList.append(Nbr.distance)
                            break


    if resList:
        return max(resList)
    else:
        return -1

def clearMark(graph):
    for vert in graph:
        vert.status=None
    return graph







def createGraph(grid):
    g=graph()

    width = len(grid[0])
    depth = len(grid)
    for x, i in enumerate(grid):
        for y, j in enumerate(i):
            curentID,currentVal=(x,y),j
            newPos=genNewPos(x,y,depth,width)

            for p in newPos:
                newID,newVal=(p[0],p[1]),grid[p[0]][p[1]]
                dist=1
                g.addEdge(curentID,currentVal,newID,newVal,dist)

    return g


def genNewPos(x,y,d,w):
    newPos=[]

    coorNbr = [ (-1, 0),  (0, -1), (0, 1), (1, 0)]
    for c in coorNbr:
        newX,newY=x+c[0],y+c[1]
        if newX>=0 and newX<d and newY>=0 and newY<w:
            newPos.append((newX,newY))
    return newPos
'''


def maxDistance(grid):
    width=len(grid[0])
    depth=len(grid)
    distMap=[[None for n in range(width)] for d in range(depth)]
    queue=[]

    for x,row in enumerate(grid):
        for y,r in enumerate(row):
            if r==1:
                queue.append((x,y))
                distMap[x][y]=0

    if not queue or len(queue)==width*depth:
        return -1
    else:
        move=[(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            x,y=queue.pop(0)
            for m in move:
                newX=x+m[0]
                newY=y+m[1]

                if newX>=0 and newX<depth and newY>=0 and newY<width and distMap[newX][newY]==None:
                    distMap[newX][newY]=distMap[x][y]+1
                    queue.append((newX, newY))

    return max([max(row) for row in distMap])


if __name__ == "__main__":
    grid = [[1,0,1],[0,0,0],[0,0,0],[0,0,0],[1,0,1]]#eval(input())
    print(maxDistance(grid))