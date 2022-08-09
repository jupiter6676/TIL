# AXIS, Q1, Q2, Q3, Q4
quadrant = [0] * 5

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    if x == 0 or y == 0:
        quadrant[0] += 1

    elif x > 0 and y > 0:
        quadrant[1] += 1

    elif x < 0 and y > 0:
        quadrant[2] += 1

    elif x < 0 and y < 0:
        quadrant[3] += 1

    else:
        quadrant[4] += 1

print('Q1:', quadrant[1])
print('Q2:', quadrant[2])
print('Q3:', quadrant[3])
print('Q4:', quadrant[4])
print('AXIS:', quadrant[0])