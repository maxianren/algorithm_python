'''
The issue of the Hanoi Tower originated from an ancient Indian legend.
For the original Hanoi Tower game, there are only three pillars available for players to operate.
As a result, the original legend requires more than 1.8*10^19 steps to solve the problem.

The number of required steps can be greatly reduced by adding columns.
Find the minimum number of steps to complete the migration under the restriction below:
- the number of plates is given,
- the number of pillars is 4 (that is, the limit is 4 pillars)
- the other rules of the original legend are not changed.

Input format:
A non-negative integer M, M represents the number of disks, M<=1000.

Output format:
A non-negative integer that represents the minimum number of steps to complete the migration.

Input sample:
3

Sample output:
5
'''

#the main function

def best_hanoi_4_tower(m,cache_4,cache_3):
    if m ==0:
        cache_4[0] = 0
        return 0
    # Recursion termination condition
    elif m==1:
        cache_4[1] = 1
        return 1

    else:
        for n in range(1, m):

            # result of hanoi3
            if cache_3[n]==None:
                res_3= hanoi_3_tower(n)
                cache_3[n]=res_3
            # consult previous result that already saved in cache list
            else:
                res_3=cache_3[n]

            #result of reduced haoi4
            if cache_4[m-n]==None:
                res_4=best_hanoi_4_tower(m - n,cache_4,cache_3)
            # consult previous result that already saved in cache list
            else:
                res_4 = cache_4[m - n]

            #result of desired haoi4: sum of reduced hanoi4 and hanoi3
            res=res_3+2*res_4

            #results of the best hanoi4 solution
            if cache_4[m] == None:
                cache_4[m]=res
            # consult previous result that already saved in cache list
            else:
                # keep updating the haoi result
                if res < cache_4[m]:
                    cache_4[m]=res

        return cache_4[m]



def hanoi_3_tower(n):
    #Recursion termination condition
    if n==1:
        return 1
    else:
        h=1+2*hanoi_3_tower(n-1)
        return h

if __name__ == "__main__":
    m = 3#int(input())

    print(best_hanoi_4_tower(m,(m+1)*[None],(m+1)*[None]))