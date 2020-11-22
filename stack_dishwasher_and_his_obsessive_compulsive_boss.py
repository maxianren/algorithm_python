'''
Dishwasher John has an obsessive-compulsive boss Mike.
The restaurant has 10 dishes in total and the boss carefully number them from 0 to 9.
He asked John to wash the dishes according to the order from 0 to 9, and the washed plates must be neatly stacked.

customers often come to pick up the dishes When John washes the dishes, each customer could only take 1 dish from the top of the dish pile.

Mike carefully recorded the number of the dishes taken by the customer at the checkout counter, such as "1043257689".
In this way he could know whether John followed his order to wash the dishes in the order of 0123456789.

Can you make accurate judgments like Mike?

Input format:
A string of length 10, which contains only the numbers from 0 to 9, and does not repeat, representing the number of the plate that the customer took in turn

Output format:
String: Yes or No, indicating that the dishes are washed in order, or the dishes are not washed in order

Input example 1:
1043257689

Output sample 1:
Yes

Input example 2:
4230178956

Output sample 2:
No
'''


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def dish_wash_order_check(str):
    wash_stack=Stack()
    record_order=str
    plates=[p for p in range(9,-1,-1)]

    #check each digit of recoded order
    for r_o in record_order:


        if wash_stack.isEmpty():

            while plates!=[] and int(plates[-1])<=int(r_o):
                wash_stack.push(plates.pop())
            wash_stack.pop()

        elif int(r_o)==int(wash_stack.peek()):
            wash_stack.pop()

        else:
            return 'No'

    return 'Yes'





if __name__ == "__main__":
    str=input()
    print(dish_wash_order_check(str))