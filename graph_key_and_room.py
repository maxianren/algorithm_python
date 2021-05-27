'''
There are N rooms, and you are in room 0 at the beginning. Each room has a different number: 0, 1, 2,..., N-1,
and there may be some keys in the room that will allow you to enter the next room.

Formally, there is a key list rooms[i] for each room i, and each key rooms[i][j] is represented by an integer in [0,1,...,N-1],
where N = rooms.length. The key rooms[i][j] = v can open the room numbered v.

Initially, all rooms except room 0 were locked.
You can freely move back and forth between rooms.
Please judge whether you can finally open all the rooms.

Input format:
One-line nested list, the length of the list is N, given in a legal Python expression format

Output format:
True or False, it means whether you can enter each room

Input sample:
[[1],[2],[3],[]]

Sample output:
True
'''


def canVisitAll(rooms):
    opened=[0]
    stack=[]
    roomsLst = [i for i in range(len(rooms))]

    while rooms[0]:
        key=rooms[0].pop()
        stack.append(key)
        opened.append(key)

    while stack:
        current=stack.pop(0)
        while rooms[current]:
            key=rooms[current].pop()
            if key not in opened:
                stack.append(key)
                opened.append(key)

    if sorted(opened)==roomsLst:
        return True
    else:
        return False


if __name__ == "__main__":
    rooms = [[3,2,1],[],[],[1,2]] #eval(input())
    print(canVisitAll(rooms))