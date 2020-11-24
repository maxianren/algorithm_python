'''
At the beginning, a string S consisting of lowercase letters is given.
In each move, select the leftmost letter, remove it from its original position, and add it to the end of the string.
Such movement can be performed as many times as you want

Return the smallest string that we can have after moving
(note: in Python3, the size of the string can be compared with the inequality sign).

Input format:
S. S is a string containing only lowercase letters and the length does not exceed 100000.

Output format:
A string of the same length as S.

Input sample:
"cba"

Sample output:
acb
'''



def func(S):

    min_S=min(S)

    while S[0]!=min_S:
        S=S[1:]+S[0]

    return S

if __name__ == "__main__":
    S = 'fttzr'
    #S = eval(input())
    print(func(S))

