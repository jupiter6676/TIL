import sys
from collections import deque

input = sys.stdin.readline
q = deque()

for _ in range(int(input())):
    ip = input().split()
    com = ip[0]

    if com == 'push_front':
        q.appendleft(int(ip[1]))
    elif com == 'push_back':
        q.append(int(ip[1]))
    elif com == 'pop_front':
        print(q.popleft() if q else -1)
    elif com == 'pop_back':
        print(q.pop() if q else -1)
    elif com == 'size':
        print(len(q))
    elif com == 'empty':
        print(0 if q else 1)
    elif com == 'front':
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)