'''
There are now N versions of the same product, numbered as integers from 1 to N; among them, all versions have been damaged since a certain version.
Now given a function isBadVersion, enter the number N to determine whether the version is damaged (if it is damaged, it will output True);
please find the first damaged version.
Note: Sometimes the isBadVersion function runs very slowly, please pay attention to optimize the search method

Input format:
Two lines
The first line is an integer, which is the total number of product numbers N
The second line is the given judgment function, which is given in a valid Python expression and can be read using eval

Output format:
A line of numbers, indicating the first damaged version

Input sample:
50
lambda n:n>=30

Sample output:
30

'''



def firstBadVersion(n):
    # define variables for binary search
    first=1
    last=n
    mid = (first + last) // 2

    # keep reducing the possible range by halfing the range till the length of the range become 1
    while last-first >1:
        # check if the current middle point fit the requirement, if true keep search in the left part
        if isBadVersion(mid):

            # if the middle point is the smallest possible value, stop the loop in advance
            if isBadVersion(mid + 1) and not isBadVersion(mid-1):
                return mid
            else:
                last=mid

        # check if the current middle point fit the requirement, if false keep search in the right part
        else:
            first=mid

        # redefine the middle point and start the next loop
        mid=(first + last) // 2

    # when the loop finishes, there are only 2 value remain, decide which one is the smallest
    if not isBadVersion(mid):
        return last

if __name__ == "__main__":
    N = 50#int(input())
    isBadVersion = lambda n:n>=50#eval(input())
    print(firstBadVersion(N))

