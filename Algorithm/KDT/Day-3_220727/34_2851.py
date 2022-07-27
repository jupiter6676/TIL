mushroom = list()

for _ in range(10):
    mushroom.append(int(input()))

scores = list()   # 최대한 100에 가깝게
prefix_sum = 0
min_ = float('inf')

for s in mushroom:
    prefix_sum += s
    
    if abs(prefix_sum - 100) <= min_:   # 차이가 같으면, 가장 큰 수로 갱신
        min_ = abs(prefix_sum - 100)   # 100을 뺐을 때 최솟값
        closest_to_100 = prefix_sum

print(closest_to_100)