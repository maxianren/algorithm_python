'''
The Sierpinski carpet is a square fractal pattern:
Each carpet can be divided into 9 parts of equal size, in which the center is hollowed out, and the rest are composed of smaller carpets.

Now given the size of the carpet (number of rows) and the character elements that make up the carpet,
please print the corresponding carpet graphics.

Note: The cavity is represented by a half-width space;
when the length of the given character element is not 1, the number of spaces must correspond to the character length

Input format:
The input is two lines, which are the positive integer N of the carpet size and the element string c
Input data ensures that N is a positive integer power of 3

Output format:
Sierpinski carpet composed of N lines of strings with length N*len(c)

Input sample:
9
[]

Sample output:

[][][][][][][][][]
[]  [][] [][]   []
[][][][][][][][][]
[][][]      [][][]
[]  []      []  []
[][][]      [][][]
[][][][][][][][][]
[]  [][]  [][]  []
[][][][][][][][][]
'''

#the main function
def sierpinski(n, base_fig):
    #Recursion termination condition
    if n==3:
        return [base_fig*3,base_fig+' '*len(base_fig)+base_fig,base_fig*3]

    else:
        smaller_sierpinski=sierpinski(n/3,base_fig)
        m=len(smaller_sierpinski)

        #extend till m lines
        smaller_sierpinski+=smaller_sierpinski*2
        # from 0 to m lines: extend the element by repeating itself 2 times
        smaller_sierpinski[0:m]=[x*3 for x in smaller_sierpinski[0:m]]
        # from m to 2m lines: extend the element by adding m*input_length space, then repeating itself 1 time
        smaller_sierpinski[m:2*m]=[x+' '*len(base_fig)*m+x for x in smaller_sierpinski[m:2*m]]
        # from 0 to m lines: extend the element by repeating itself 2 times
        smaller_sierpinski[m*2:]=[x*3 for x in smaller_sierpinski[m*2:]]

        return smaller_sierpinski

if __name__ == "__main__":
    n= 81# int(input())
    base_fig='[]' #input()

    if n==0:
        print (' ')
    else:
        for s in sierpinski(n, base_fig):
            print (s)
