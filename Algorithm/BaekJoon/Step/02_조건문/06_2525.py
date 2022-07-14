H, M = map(int, input().split())
time = int(input())

minute = (M + time) % 60
hour = H + (M + time) // 60

if hour >= 24:
    hour %= 24

print(hour, minute)