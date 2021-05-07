'''
There is a classic division process in the well-known quick sort algorithm:
we usually adopt a certain method to take an element as the pivot (median value),
and through exchange, put the elements smaller than the pivot to its left and the ones larger than the pivot to its right.
Given the arrangement of N non-negative integers that are different from each other after the division,
how many elements may be the pivot selected before the division?

For example, the given arrangement is [1, 3, 2, 4, 5]. then:
- There is no element on the left side of 1, and the elements on the right side are larger than it, so it may be a pivot;
- Although the left element of 3 is smaller than it, the 2 on its right is smaller than it, so it cannot be a pivot;
- Although the elements on the right of 2 are larger than it, the 3 on the left is larger than it, so it cannot be a pivot;

For similar reasons, both 4 and 5 may be pivotal.
Therefore, 3 elements may be pivots.

Input format:
Arrangement of several integers in a row, separated by spaces

Output format:
In the first line, output the number of elements that may be pivotal elements;
in the second line, output these elements in increasing order, separated by 1 space,
and there must be no extra spaces at the beginning and end of the line (if the number of elements is 0, the first The second line is a blank line).

Input sample:
1 3 2 4 5

Sample output:
3
1 4 5
'''

def func(S):
    S=list(map(int,S.split()))
    count=0
    res_lst=[]

    #check each number in the list, if it fit the requirement: largest from its left and smallest from its right
    for s in range(len(S)):
        if max(S[:s+1])<=S[s] and min(S[s:])>=S[s]:
            res_lst.append(S[s])
            count+=1
    print(count)
    print(' '.join(str(r) for r in res_lst))


if __name__ == "__main__":
    S = '1 3 2 4 5'#eval(input())
    func(S)

