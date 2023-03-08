# import sys
# input = sys.stdin.readline

# N = int(input())

# S = dict()
# for k in range(1, 21):
#     S[k] = 0

# for _ in range(N):
#     line = input().split()

#     command = line[0]
#     if len(line) == 2:
#         num = int(line[1])

#     if command == 'add':
#         S[num] = 1
#     elif command == 'remove':
#         S[num] = 0
#     elif command == 'check':
#         print(S[num])
#     elif command == 'toggle':
#         S[num] = int(not S[num])
#     elif command == 'all':
#         for k in range(1, 21):
#             S[k] = 1 
#     else:   # empty
#         for k in range(1, 21):
#             S[k] = 0

import sys
input = sys.stdin.readline

N = int(input())

S = 0

for _ in range(N):
    line = input().split()

    command = line[0]
    if len(line) == 2:
        num = int(line[1])

    if command == 'add':
        S |= 1 << (20 - num)    # or
    elif command == 'remove':
        S &= ~(1 << (20 - num)) # not → and
    elif command == 'check':
        print(1 if S & (1 << (20 - num)) else 0)
    elif command == 'toggle':
        S ^= 1 << (20 - num)    # xor
    elif command == 'all':
        S = (1 << 21) - 1
    else:   # empty
        S = 0

    print(bin(S))

'''
S = 0000 0000 0000 0000 0000

add 1
S = 1000 0000 0000 0000 0000

add 2
S = 1100 0000 0000 0000 0000

remove 2
S = 1000 0000 0000 0000 0000

toggle 3
S = 1010 0000 0000 0000 0000

all
S = 1111 1111 1111 1111 1111

toggle 10
S = 1111 1111 1011 1111 1111

remove 20
S = 1111 1111 1011 1111 1110

empty
S = 0000 0000 0000 0000 0000

toggle 1
S = 1000 0000 0000 0000 0000

toggle = 1
S = 0000 0000 0000 0000 0000
'''