# 일반적인 CD 음질(44.1KHz, 16bit, 스테레오)로 1초 동안 저장하려면
# 44100 * 16 * 2 * 1 bit의 저장공간이 필요한데,
# 44100 * 16 * 2 * 1 / (8 * 1024 * 1024) 로 계산하면
# 약 0.168 MB 정도가 필요

# 1 Byte = 8 Bit
# 1024**2 Byte = 1 MB

h, b, c, s = map(int, input().split())

# 필요 저장공간 (bit)
bit = h * b * c * s

# bit to MB
MB = bit / (8 * (1024**2))

print(format(MB, '.1f'), 'MB')