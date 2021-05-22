'''
Given a series of integers, please construct the corresponding binary tree so that it is both a binary search tree and a complete binary tree;
please output the traversal of the binary tree hierarchically that meets the conditions.

Input format:
A sequence of integers, separated by spaces

Output format:
the binary search tree is traversed hierarchically, and the integer sequence is output in order,
that is, starting from the root node of the first level, and descending level by level, from left to right when at the same level,
separated by spaces, with no extra spaces at the end of the line

Input sample:
1 2 3 4 5 6 7 8 9 0

Sample output:
6 3 8 1 5 7 9 0 2 4
'''

class treeNode:
    def __init__(self,key,value,left=None,right=None,parent=None):
        self.key=key
        self.value=value
        self.leftChild=left
        self.rightChild=right
        self.parent=parent

def completeTree(lst_input):
    n=len(lst_input)
    treeLst=[treeNode(i,'') for i in range(n)]

    for j,t in enumerate(treeLst):
        if (j+1)*2<=n:
            t.leftChild=treeLst[(j+1)*2-1]
        if (j + 1) * 2+1 <= n:
            t.rightChild = treeLst[(j + 1) * 2+1-1]
    return treeLst[0]

def value2Tree(root,lst_input):
    if root:
        value2Tree(root.leftChild,lst_input)
        root.key=lst_input.pop(0)
        value2Tree(root.rightChild, lst_input)

    return root


def traversal(root_key):
    queTrvsl=[]
    queTrvsl.append(root_key)
    res_lst=[]

    while queTrvsl:
        parent=queTrvsl.pop(0)
        res_lst.append(parent.key)
        if parent.leftChild:
            queTrvsl.append(parent.leftChild)
        if parent.rightChild:
            queTrvsl.append(parent.rightChild)

    print(' '.join(str(l) for l in res_lst))

if __name__ == "__main__":
    lst_input='1 2 3 4 5 6 7 8 9 0'#input()
    lst_input=sorted(list(map(int,lst_input.split())))

    root=completeTree(lst_input)
    root_key=value2Tree(root,lst_input)
    traversal(root_key)