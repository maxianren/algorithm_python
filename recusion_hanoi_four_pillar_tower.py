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

def best_hanoi_4_tower(m):
    if m ==1:
        return 1
    elif m==0:
        return 0
    #when m > 1, list all the possible solurions and select the best
    else:
        hanoi_4_list = []
        for n in range(1, m):
            h_4 = hanoi_4_tower(n, m)
            hanoi_4_list.append(h_4)
        return min(hanoi_4_list)

def hanoi_4_tower(n,m):
    if m > n:
        return hanoi_3_tower(n) + 2 * hanoi_4_tower(n, m - n)
    #Recursion termination condition
    else:
        return best_hanoi_4_tower(m)

def hanoi_3_tower(m):
    #Recursion termination condition
    if m==1:
        return 1
    else:
        return 1+2*hanoi_3_tower(m-1)

if __name__ == "__main__":
    m = 9#int(input())

    print(best_hanoi_4_tower(m))