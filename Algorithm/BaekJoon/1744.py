N = int(input())
positive = list()
negative = list()   # 0 이하의 모든 수

for _ in range(N):
    num = int(input())

    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

total = 0

# 1. 양수의 배열
for i in range(0, len(positive) - 1, 2):
    # 한 수가 1일 때
    if positive[i] == 1 or positive[i + 1] == 1:
        total += positive[i] + positive[i + 1]
    # 두 수가 모두 1 이상일 때
    else:
        total += positive[i] * positive[i + 1]

# positive 배열 길이가 홀수일 때
if len(positive) % 2:
    total += positive[-1]   # 마지막 원소(젤 작음)를 더하기

# 2. 음수, 0의 배열
for i in range(0, len(negative) - 1, 2):
    # 더하는 것보다 곱하는 게 더 큼
    total += negative[i] * negative[i + 1]

if len(negative) % 2:
    total += negative[-1]

print(total)

'''
5
-1
-2
-3
-4
-5

25

----
5
-537
81
-435
257
157

274025

---
5
-5
-2
-3
0
0

15
'''