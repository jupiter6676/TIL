import sys
input = sys.stdin.readline

# idx 파일이 가장 큰 파일이라 가정 (오름차순 정렬)
# 0 ~ idx - 1번째의 파일과 idx 파일을 비교
# → start 파일이 idx 파일의 90%보다 크면 start ~ idx 파일 모두 검사해야 함
def binarySearch(idx):
    start = 0
    end = idx - 1

    while start <= end:
        mid = (start + end) // 2

        if files[mid] < files[idx] * 0.9:
            start = mid + 1

        else:
            end = mid - 1

    return idx - start

'''main'''
N = int(input())
files = list(map(int, input().split()))
files.sort()

cnt = 0
for i in range(N):
    cnt += binarySearch(i)

print(cnt)