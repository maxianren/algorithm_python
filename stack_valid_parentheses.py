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

def pairBracket(str):
    s=Stack()
    balanced=True
    index=0
    #check every symbol in the list-------------------------------
    while index<len(str) and balanced:
        symbol =str[index]

        if symbol in '([{':
            print('right: ', symbol)#debug mark point
            s.push(symbol)
        else:
            print('----------------\nleft: ',symbol)#debug mark point

            if s.isEmpty() is True:
                return False
            else:
                stack_top = s.pop()
                if match_symbol(stack_top,symbol) is False:
                    return False
        index+=1

    if s.isEmpty():
        return True
    else:
        return False

def match_symbol(top, new):
    left = '([{'
    right=')]}'
    if left.index(top)==right.index(new):
        return True
    else:
        return False

str='())))'#input()
print(pairBracket(str))