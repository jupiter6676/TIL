import sys
import math
input = sys.stdin.readline

def is_prime(num):
    num = int(num)

    if num == 0 or num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True

def dfs(n, length):
    if length == N:
        print(n)
        return

    for i in range(10):
        n += str(i)

        if is_prime(n):
            dfs(n, length + 1)

        n = n[:-1]


'''main'''
N = int(input())
dfs('', 0)