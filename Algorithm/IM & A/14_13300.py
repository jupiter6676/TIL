# 행이 2개 (여 0, 남 1)
# 열이 6개 (1학년 ~ 6학년 → 0학년 ~ 5학년)
stu = [[0] * 6 for _ in range(2)]

N, K = map(int, input().split())

for _ in range(N):
    gender, grade = map(int, input().split())

    stu[gender][grade - 1] += 1

cnt = 0
for i in range(2):
    for j in range(6):
        if stu[i][j] != 0:
            if stu[i][j] > K:
                cnt += stu[i][j] // K if stu[i][j] % K == 0 else stu[i][j] // K + 1
            else:
                cnt += 1

print(cnt)

'''
16 3
0 1
0 1
0 1
0 2
0 2
0 2
0 3
0 3
0 4
0 3
0 3
0 6
0 5
0 5
0 5
0 6
'''