'''
Given a way to serialize a binary tree:
traverse all "possible" node locations in the binary tree from the root node hierarchically:
if there is a node at that location, output the node value, and add two available locations in the next layer accordingly;
Otherwise, it outputs None and does not increase the available position of the next layer.
For example, "[5, 4, 7, 3, None, 2, None, -1, None, 9]" is the result of binary tree serialization as shown in the figure below:
Now give the result of a binary tree serialized in this form, please restore the binary tree and give its middle-order traversal.

Input format:
A line of legal Python expression, which can be parsed as a list containing integers and None

Output format:
Sequence of integers traversed in binary tree, separated by spaces

Input sample:
[5, 4, 7, 3, None, 2, None, -1, None, 9]

Sample output:
-1 3 4 5 9 2 7

Input example 2:
[5,1,4,None,None,3,6]

Output sample 2:
1 5 3 4 6

'''
# create a class binaryTree
class binaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rigthChild = None

    def insertLeft(self,newNode):
        self.leftChild=binaryTree(newNode)

    def getLeftChild(self):
        return self.leftChild

    def setLeftChild(self,obj):
        self.leftChild=obj

    def insertRight(self,newNode):
        self.rigthChild=binaryTree(newNode)

    def getRightChild(self):
        return self.rigthChild

    def setRightChild(self,obj):
        self.rigthChild=obj

# map the input serials into a binary heap dictionary,
# where keys are binary heap indexes and values are the tree objects
def seq2tree(seq):
    dic_tree={}

    # map the input serials into a binary heap dictionary first
    dic_seq={}
    key=1
    # scan all the elements in order
    for s in seq:
        # if the key is already in the dictionary, skip until the one not in and calculate its representative key
        if key in dic_seq:
            while key in dic_seq:
                    key+=1

        # if the key is None value, then make its next generation sons None as well
        if s==None:
            dic_seq[key * 2] = None
            dic_seq[key * 2 + 1] = None

        # map the value in the dictionary
        dic_seq[key] = s
        key += 1

    # filter out None value in the dictionary
    dic_seq={k:v for k,v in dic_seq.items() if v!=None}

    # create representative tree objects in the binary heap dictionary
    for k,v in dic_seq.items():
        # the first element in the dictionary
        if k==1:
            dic_tree[k]=binaryTree(v)

        # the rests
        else:
            parent_key = k // 2
            # create left child tree to proper parent tree
            if k%2==0:
                dic_tree[parent_key].insertLeft(v)
                dic_tree[k]=dic_tree[parent_key].getLeftChild()
            # create right child tree to proper parent tree
            else:
                dic_tree[parent_key].insertRight(v)
                dic_tree[k] = dic_tree[parent_key].getRightChild()

    # return the first object in the dictionary
    return dic_tree[1]


def inorderTree(root):
    # the list for final result
    lst_Oput=[]
    # the main function
    inorderTree_main(root,lst_Oput)
    # print the list in the required format
    print(' '.join(str(i) for i in lst_Oput))

# the main recursion to achieve in order traversals
def inorderTree_main(root,lst):
    # output the left tree first
    if root.getLeftChild():
        inorderTree_main(root.getLeftChild(),lst)
    # the root second
    lst.append(root.key)
    # the right tree at last
    if root.getRightChild():
        inorderTree_main(root.getRightChild(),lst)

if __name__ == "__main__":
    lst = [5,1,4,None,None,3,6]#eval(input())
    tree = seq2tree(lst)
    inorderTree(tree)