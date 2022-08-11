X = int(input())
N = int(input())

total = 0

for _ in range(N):
    price, cnt = map(int, input().split())

    total += price * cnt

print('Yes' if X == total else 'No')