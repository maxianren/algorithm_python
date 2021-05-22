'''
Given a binary tree structure and a list of integers,
please fill the integers into the corresponding nodes of the binary tree to make it a binary search tree;
please output the value2tree of the binary search tree hierarchically.

Input format:
The first line of each test sample contains an integer, which is the total number of nodes in the binary tree N.
The next N lines respectively give the left and right subtree numbers of the nodes with numbers from 0 to (N-1), separated by spaces;
the number-1 means that the corresponding subtree is empty. The last line gives N integers separated by spaces

Output format:
the binary search tree is traversed hierarchically, and the integer sequence is output in order,
that is, starting from the root node of the first level, and descending level by level, from left to right when at the same level,
separated by spaces, with no extra spaces at the end of the line

Input sample:
9
1 6
twenty three
-1 -1
-1 4
5-1
-1 -1
7-1
-1 8
-1 -1
73 45 11 58 82 25 67 38 42

Output sample:
58 25 82 11 38 67 45 73 42
'''
'''
class BST:
    def __init__(self):
        self.root=None
        self.size=0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=treeNode(key,val)
        self.size+=1

    def _put(self,key,val,currentNode):
        if key<currentNode:
            if currentNode.hasLeftchild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=key
        else:
            if currentNode.hasRightchild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftRight=key

    def __setitem__(self, key, value):
        return self.put(key, value)
'''


class treeNode:
    def __init__(self,key,value,left=None,right=None,parent=None):
        self.key=key
        self.value=value
        self.leftChild=left
        self.rightChild=right
        self.parent=parent
'''
    def isLeftChild(self):
        return self.parent and self.parent.leftChild==self

    def isRightChild(self):
        return self.parent and self.parent.RightChild==self

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild
'''

def buildTree(lst_key):
    tree_lst=[treeNode(i,'') for i in range(len(lst_key))]
    for i,l_k in enumerate(lst_key):

        if l_k[1] != -1:
            tree_lst[i].rightChild = tree_lst[l_k[1]]

        if l_k[0] != -1:
            tree_lst[i].leftChild = tree_lst[l_k[0]]

    return tree_lst[0]

'''
    tree=treeNode('','')
    stack_parent=[]
    for l_n in lst_key:
        if tree.key=='':
            tree.key=treeNode(0,'')
            parent=tree.key
        else:
            parent = stack_parent.pop()

        if l_n[1] != -1:
            parent.rightChild = treeNode(l_n[1],'')
            parent.rightChild.parent = parent
            stack_parent.append(parent.rightChild)

        if l_n[0] !=-1:
            parent.leftChild=treeNode(l_n[0],'')
            parent.leftChild.parent=parent
            stack_parent.append(parent.leftChild)
'''



def value2tree(treeRoot_key,lst):
    if treeRoot_key.leftChild:
        value2tree(treeRoot_key.leftChild,lst)
    treeRoot_key.value=lst.pop(0)
    if treeRoot_key.rightChild:
        value2tree(treeRoot_key.rightChild,lst)

    return treeRoot_key

def traversal(treeRoot_val):
    queTrvsl=[]
    queTrvsl.append(treeRoot_val)
    res_lst=[]

    while queTrvsl:
        parent=queTrvsl.pop(0)
        res_lst.append(parent.value)
        if parent.leftChild:
            queTrvsl.append(parent.leftChild)
        if parent.rightChild:
            queTrvsl.append(parent.rightChild)

    print(' '.join(str(l) for l in res_lst))





if __name__ == "__main__":
    num=9#int(input())

    lst_test=['1 6','2 3','-1 -1','-1 4','5 -1','-1 -1','7 -1','-1 8','-1 -1']
    lst_key = []
    for i in range(num):
        n=lst_test[i]#input()
        lst_key.append(tuple(map(int,n.split())))

    lst_val='73 45 11 58 82 25 67 38 42'#input()
    lst_val=sorted(list(map(int,lst_val.split())))

    treeRoot_key=buildTree(lst_key)
    treeRoot_val=value2tree(treeRoot_key,lst_val)
    traversal(treeRoot_val)

