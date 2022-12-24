def factorial(n):
    if n <= 1:
        return 1    # 1. 여기 1 반환
    
    return n * factorial(n - 1) # 2. 여기에 return을 꼭
    

N = int(input())
print(factorial(N))