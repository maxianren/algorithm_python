'''
Base sort

Implement a radix sorting algorithm for sorting positive integers in decimal base from small to large.

The idea is to keep 10 queues (queue 0, queue 1...queue 9, queue main).
At the beginning, all the numbers are in the main queue without sorting.

In the first pass, all the numbers are placed in the corresponding queues 0-9 according to their decimal units (0-9).
After all are placed, the numbers in each queue are combined and arranged into the main queue according to the FIFO order.

In the second pass, take the number from the head of the main queue, and put it into the corresponding queue 0-9 according to the value of its ten digits.
After all are placed, the numbers of each queue are still merged into the main queue according to the FIFO order.

On the third trip, displace in hundreds digits and merge again; on the fourth trip, displace in thousands digits and merge again.
Until the most digits are put out and merged, the main queue will be a sequence of numbers.

Input format:
A list mylist, where mylist contains some positive integers that need to be sorted.
The positive integers are different from each other and all do not exceed 100000, and the total number is between 1 and 1000.

Output format:
A list of the same length as mylist.

Input sample:
[8, 91, 34, 22, 65, 30, 4, 55, 18]

Sample output:
[4, 8, 18, 22, 30, 34, 55, 65, 91]

'''

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def func(S):

    #create 10 queues to represent 10-based n digits, each of which is called Q[n]
    Q=[Queue() for i in range(10)]

    #initialise the main queue with the input list
    q_main=Queue()
    for s in S:
        q_main.enqueue(s)

    #compare every digit with loop
    for n in range(10):

        #enqueue all the element from main queue into corrispondnt digit queues
        while not q_main.isEmpty():
            #the element to check
            q=q_main.dequeue()
            #the value on n-digits
            n_digit=q//10**n%10
            #enqueue the element into corrispondent queue
            Q[n_digit].enqueue(q)

        #put elements from digit queues back to the main queue
        for q in Q:
            while not q.isEmpty():
                q_main.enqueue(q.dequeue())

    return q_main.items



if __name__ == "__main__":
    #S = [8, 91, 34, 22, 65, 30, 4, 55, 18]
    S = eval(input())
    print(func(S))

