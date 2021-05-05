'''
A teacher wants to distribute candies to the children.
N children stand in a straight line, and the teacher will rate each child's behaviour.

You need to help the teacher distribute candies to these children according to the following requirements:
 - Each child is allocated at least 1 candy.
 - Among the neighboring children, the child with a higher score must get more candies.

So, how many sweets does the teacher need to prepare at least?

Input format:
A list, given as a valid Python expression in text format

Output format:
A row of numbers, indicating the minimum number of candies required to meet the allocation conditions

Input sample:
[1,2,2]

Sample output:
4
Note: The feasible allocation plan is 1, 2, and 1 candy;
the third child only gets 1 candy and it meets the conditions of the question
'''

def candy(ratings):
    #distribute 1 candy for each kid
    candy_list = len(lst) * [1]

    #scan from left to right: give an additional candy to whom has a higher score compared to the kid on his left
    for i in range(1,len(candy_list)):
        if ratings[i]>ratings[i-1]:
            candy_list[i]=candy_list[i-1]+1

    # scan from right to left: give an additional candy to whom has a higher score compared to the kid on his right
    for j in range(len(candy_list)-1,0,-1):
        if ratings[j-1] > ratings[j]:
            #because a scan from left to right has done, an additional candy is given only if the kid on the left has fewer or equal number of candy
            if candy_list[j-1] <= candy_list[j]:
                candy_list[j-1] = candy_list[j] + 1

    return sum(candy_list)


if __name__ == "__main__":
    lst = [1,0,2]#eval(input())
    print(candy(lst))