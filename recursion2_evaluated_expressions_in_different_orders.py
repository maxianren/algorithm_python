'''
Given an expression string, find all possible results in different evaluation orders

Input format:
One line of string, containing only 0-9 and operators +, -, and *
Note: The string guarantees that the three operators are all numeric characters

Output format:
All possible results that are not repeated, sorted from smallest to largest and separated by a comma ","

Input sample:
2*3-4*5

Sample output:
-34,-14,-10,10

Note:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
'''

def findWays(expr):
    # transform a string into numbers and operatos
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)

    #empty dictionary used as cache to reduce recursion
    known_res={}
    #recursion function
    res=list(set(solutions(nums, ops,known_res)))
    res_sorted=sorted(res)
    return res_sorted


def solutions(nums,ops,known_res):

    #Recursion termination condition: when the input number list has only 1 element
    if len(nums)==1:
        #the result is saved as a list
        return [nums[0]]

    # a list is used to save the final result
    res_list = []
    # divide the input into 2 parts and solve them individually, the loop represent different ways to divide the list
    for i in range(1, len(ops) + 1):
        op = ops[i - 1]
        left = solutions(nums[:i], ops[:i - 1], known_res)
        right = solutions(nums[i:], ops[i:], known_res)

        # the results of the left part and the right part are saved in separated lists, cross operate each element in 2 lists
        for l in left:
            for r in right:
                # if the input is already in the dictionary, return the value in the dictionary
                if (l, r, op) in known_res:
                    res_list.append(known_res[(l, r, op)])

                # if the input is not in the dictionary, proceed the operation
                else:
                    res = math_op(int(l), int(r), op)
                    #save the result in the dictionary for further inquery
                    known_res[(l, r, op)] = res
                    res_list.append(res)
    return res_list


def math_op(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    else:
        return a*b

if __name__ == "__main__":
    expr='2*3+2*4-6'#input()
    print(",".join(str(f) for f in findWays(expr)))