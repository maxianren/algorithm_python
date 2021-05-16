'''
Given a polyTree given in the form of a nested list, find its post-order traversal
Note: Each list representing a non-empty multi-branch tree contains at least one item;
the first item in the list represents the node value, and each subsequent item is a subtree;
when traversing the subtree, the list subscripts are in descending order.

Input format:
A line of legal Python expression can be parsed into a multi-tree structure in the form of a nested list

Output format:
One line of integers, separated by spaces

Input sample:
[1,[2,[3,[4],[5]],[6]],[7],[8,[9],[10]]]

Sample output:
4 5 3 6 2 7 9 10 8 1
'''


def polyTree(I_lst):
    # the list for final result
    res_lst=[]
    # the main function
    polyTree_main(I_lst,res_lst)
    # print the list in the required format
    print(' '.join(str(r) for r in res_lst))

def polyTree_main(I_lst,res_lst):
    # output the left tree first
    left=I_lst.pop(1)
    if len(left)==1:
        res_lst.append(left[0])
    else:
        polyTree_main(left,res_lst)

    # the right ones second
    while len(I_lst)!=1:
        rights=I_lst.pop(1)
        if len(rights)==1:
            res_lst.append(rights[0])
        else:
            polyTree_main(rights, res_lst)

    # the root at last
    root = I_lst.pop(0)
    res_lst.append(root)
    pass


if __name__ == "__main__":
    I_lst=[1,[2,[3,[4],[5]],[6]],[7],[8,[9],[10]]]#eval(input())
    polyTree(I_lst)