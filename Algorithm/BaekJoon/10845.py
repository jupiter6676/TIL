import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    line = input().split()

    command = line[0]
    if len(line) == 2:
        num = line[1]

    if command == 'push':
        queue.append(num)
    elif command == 'pop':
        print(queue.popleft() if queue else -1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        print(1 if not queue else 0)
    elif command == 'front':
        print(queue[0] if queue else -1)
    else:   # back
        print(queue[-1] if queue else -1)