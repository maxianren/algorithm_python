'''
Given a binary search tree, please modify the tree nodes so that the value of each node in the new tree is equal to the sum that are​greater than or equal to the node in the original tree;
please output the modified tree hierarchy traversal sequence.

Input format:
A non-repetitive sequence of integers, separated by spaces, is the insertion order of the nodes in the original binary search tree
Note: The title guarantees that the input sequence is not repeated

Output format:
the binary search tree is traversed hierarchically, and the integer sequence is output in order,
that is, starting from the root node of the first level, and descending level by level, from left to right when at the same level,
separated by spaces, with no extra spaces at the end of the line

Input sample:
6 1 8 3 4 9 2 7 5 0

Sample output:
30 45 17 45 42 24 9 44 39 35
'''


class BST:
    def __init__(self):
        self.root=None
        self.size=0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self,key,val=None):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=treeNode(key,val)
        self.size+=1

    def _put(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=treeNode(key,val)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=treeNode(key,val)

    def __setitem__(self, key, value):
        return self.put(key, value)



class treeNode:
    def __init__(self,key,value,left=None,right=None,parent=None):
        self.key=key
        self.value=value
        self.leftChild=left
        self.rightChild=right
        self.parent=parent

    def isLeftChild(self):
        return self.parent and self.parent.leftChild==self

    def isRightChild(self):
        return self.parent and self.parent.RightChild==self

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild


def str2tree(lst_str):
    tree=BST()
    for l_s in lst_str:
        tree.put(l_s)

    return tree.root

    pass
def value2Tree(root,sum,lst):
    if root:
        value2Tree(root.rightChild,sum,lst)

        if lst:
            sum=root.key+lst[-1]
        else:
            sum=root.key
        lst.append(sum)
        root.val=sum

        value2Tree(root.leftChild,sum,lst)

    return root

def traversal(root):
    queTrvsl=[]
    queTrvsl.append(root)
    res_lst=[]

    while queTrvsl:
        parent=queTrvsl.pop(0)
        res_lst.append(parent.val)
        if parent.leftChild:
            queTrvsl.append(parent.leftChild)
        if parent.rightChild:
            queTrvsl.append(parent.rightChild)

    print(' '.join(str(l) for l in res_lst))

if __name__ == "__main__":
    input_str='6 1 8 3 4 9 2 7 5 0'#input()
    lst_str=(list(map(int,input_str.split())))
    sum=0
    med_lst=[]

    tree=str2tree(lst_str)
    root_val=value2Tree(tree,sum,med_lst)
    traversal(root_val)
