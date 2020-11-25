'''
Calculate how many events occurred in the past 10,000 milliseconds, including the current event;
that is, for each element k in the list, calculate how many elements in the entire list are between k-10000 and k (Both ends are included).

Input format:
A sorted list mylist, all elements are non-negative integers, record the occurrence time of each request, the unit is milliseconds.

Output format:
A list of the same length as mylist.

Input sample:
[0,10,100,1000,10000,20000,100000]

Sample output:
[1,2,3,4,5,2,1]

'''

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

def func(S):

    q=Queue()
    result_list=[]
    count_previous_repeat=0

    #check every element in the input list
    for s in S:

        #check if previous n items are the same, such as [0,1,1,1], mark with a counter
        if not q.isEmpty() and q.items[0]==s:
            count_previous_repeat+=1

        elif not q.isEmpty() and q.items[0]!=s:
            count_previous_repeat=0

        # add the testing element into the quene
        q.enqueue(s)

        # keep removing the last element in quene until the last one less than s-10000
        while s-10000> q.items[-1]:
            q.dequeue()

        # if the current element is the same sa the previous ones, then need to update the quantity of previous element in the output list
        n_result_list=len(result_list)

        ## remove previous repeated items
        while result_list!=[] and len(result_list) > n_result_list - count_previous_repeat:
            result_list.pop()
        ## update with new items
        while len(result_list) < n_result_list + 1:
            # the size of the quene is the result, which is appended at the end of the list
            result_list.append(q.size())


    return result_list

if __name__ == "__main__":
    #S = [0,0,0,1000,1000,10000,20000,100000] #test list
    S = eval(input())
    print(func(S))

