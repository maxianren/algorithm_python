'''
Given a binary tree, please give its mirror flip.
For the sake of convenience, this question only gives the level traversal of the complete binary tree,
please give the corresponding middle-order traversal of the flipped binary tree.

Remarks:
This question comes from the experience of open source software developer Max Howell who was rejected in an interview at Google:
Google: 90% of our engineers use the software you wrote (Homebrew),
but you can’t write the question of flipping a binary tree on the whiteboard during the interview. This is too bad

Input format:
A sequence of integers separated by spaces, representing a complete binary tree traversal

Output format:
A space-separated sequence of integers, representing the mid-order traversal of the flipped binary tree

Input sample:
4 2 7 1 3 6 9

Sample output:
9 7 6 4 3 2 1

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

    def insertRight(self,newNode):
        self.rigthChild=binaryTree(newNode)

    def getRightChild(self):
        return self.rigthChild

# map the input serials into a binary heap dictionary
def inHeap(string):
    string=list(map(int,string.split()))
    dic_heap={}

    # scan all the elements in order
    for i,s in enumerate(string):

        # the first element in the dictionary
       if i+1==1:
           dic_heap[i+1]=binaryTree(s)

       # the rests
       else:
           parent_key = (i + 1) // 2
           # create left child tree to proper parent tree
           if (i+1)%2==0:
               dic_heap[parent_key].insertLeft(s)
               dic_heap[i+1]=dic_heap[parent_key].getLeftChild()
           # create right child tree to proper parent tree
           else:
               dic_heap[parent_key].insertRight(s)
               dic_heap[i + 1] = dic_heap[parent_key].getRightChild()

    # return the first object in the dictionary
    return dic_heap[1]


def flipTree(tree):
    # the list for final result
    lst_Oput=[]
    # the main function
    flipTree_main(tree,lst_Oput)
    # print the list in the required format
    print(' '.join(str(l) for l in lst_Oput))

# the main recursion to achieve in order traversals
def flipTree_main(tree,lst):
    # output the right tree first
    if tree.getRightChild():
        flipTree_main(tree.getRightChild(),lst)
    # the root second
    lst.append(tree.key)
    # the left tree at last
    if tree.getLeftChild():
        flipTree_main(tree.getLeftChild(),lst)

if __name__ == "__main__":
    string = '4 2 7 1 3 6 9'  # eval(input())
    tree=inHeap(string)
    flipTree(tree)