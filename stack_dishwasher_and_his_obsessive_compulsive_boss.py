'''
Dishwasher John has an obsessive-compulsive boss Mike.
The restaurant has 10 dishes in total and the boss carefully number them from 0 to 9.
He asked John to wash the dishes according to the order from 0 to 9, and the washed_output plates_strt must be neatly stacked.

customers often come to pick up the dishes When John washes the dishes, each customer could only take 1 dish from the top of the dish pile.

Mike carefully recorded the number of the dishes taken by the customer at the checkout counter, such as "1043257689".
In this way he could know whether John followed his order to wash the dishes in the order of 0123456789.

Can you make accurate judgments like Mike?

Input format:
A string of length 10, which contains only the numbers from 0 to 9, and does not repeat, representing the number of the plate that the customer took in turn

Output format:
String: Yes or No, indicating that the dishes are washed_output in order, or the dishes are not washed_output in order

Input example 1:
1043257689

Output sample 1:
Yes

Input example 2:
4230178956

Output sample 2:
No
'''

def dish_wash_order_check(str):
    #save the input string into a list
    input_order=[int(x) for x in str]
    #simulate the process: start from plates 0-9, washing in the sink and output plates
    plates_strt=[p for p in range(9,-1,-1)]
    washed_output, washing_mid = [], []


    #main simulation process: check each input number in order
    for i_o in input_order:
        #the current number must be the largest among those in the washing sink, thus moving the plates in order from starting place utill the current number
        while i_o in plates_strt:
            washing_mid.append(plates_strt.pop())

        #moving plates away from washing sink in order until the current number is transferred
        while i_o in washing_mid:
            washed_output.append(washing_mid.pop())


    #check if the correct order is equal to the input order
    if washed_output==input_order:
        return 'Yes'
    else:
        return 'No'


if __name__ == "__main__":
    str='4230178956'#input()
    print(dish_wash_order_check(str))