'''
Given an area of length N, and 4 different lengths of tiles:
gray tiles (length 1 unit), red tiles (length 2 units), green tiles (length 3 units) and blue tiles (length 4 units),
find all the different ways to cover the entire area.

For example: when N=5, there are 15 ways to fill the area.

Input format:
A natural number N

Output format:
A row of numbers, representing the total number of different methods

Input sample:
5

Sample output:
15
'''

def tiles(n):

    cache_list=[0]*(n+1)
    cache_list[0]=1

    #dynamic programming:
    # lying n-unit problem, while removing one tile with i units, the problem become n-i units problem
    # and the n-unit problem become the sum of n-1, n-2, n-3, n-4 unit problem
    for i in range(1,n+1):
        if i<=4:
            cache_list[i]=sum(cache_list[:i])
        else:
            cache_list[i] = sum(cache_list[i-4:i])

    return cache_list[n]

def tiles_rec(n,cache_list):
    #recusion method
    if n==1:
        cache_list[1]=1
        return 1
    elif n==2:
        cache_list[2] = 2
        return 2
    elif n==3:
        cache_list[3] = 4
        return 4
    elif n==4:
        cache_list[4] = 8
        return 8

    else:
        #to be created a cache list to reduce complexity
        return tiles_rec(n-1,[0]*(n+1))+tiles_rec(n-2,[0]*(n+1))+tiles_rec(n-3,[0]*(n+1))+tiles_rec(n-4,[0]*(n+1))


if __name__ == "__main__":
    n= 6# int(input())
    #print(tiles(n))
    print(tiles_rec(n,[0]*(n+1)))






