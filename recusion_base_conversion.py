'''
Base conversion
Given a number in base M, please convert it to base N

Input format:
Two lines, the first line has two digits, which are M and N in decimal notation, separated by spaces; where M and N satisfy 2 ≤ M and N ≤ 36
The second line has the number to be converted, the part of each digits exceeding 9 is represented by capital letters A-Z from 10 to 36;
input data should ensure the largest number of digits not exceed M

Output format:
A line of string, representing the converted N number

Input sample:
8 16
473

Sample output:
13B
'''

#the main function
def m_to_n_base(m,n,input_m_base):
    # set global variable which would be use in the following functions
    global library
    library = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # phase 1: convert M_base into decimal
    m_decimal=m_to_decimal(m,input_m_base)
    # phase 2: convert decimal into N_base
    return decimal_to_n(m_decimal,n)

# phase 1: convert M_base into decimal
def m_to_decimal(m,input_m_base):
    # set initial variables
    digits=len(str(input_m_base))
    sum=0
    # iteratively calculate the sum
    for d,i in enumerate(str(input_m_base)):
        # set variables in the loop
        power=digits-d-1
        index=library.index(i)
        # sum up
        sum+=index*m**power
    return sum

# phase 2: convert decimal into N_base
def decimal_to_n(m_decimal,n):
    # recursion: reduce the complexity of the problem and self-referential
    if m_decimal>0:
        return  decimal_to_n(m_decimal//n,n)+library[m_decimal%n]
    # recursion stop condition: m_decimal == 0
    else:
        return ''


if __name__ == "__main__":
    m,n= 8,16
    #m, n = map(int, input().split())
    input_m_base = 471
    #input_m_base = input()

    print(m_to_n_base(m, n, input_m_base))