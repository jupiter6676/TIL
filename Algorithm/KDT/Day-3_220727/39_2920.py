notes = list(map(int, input().split()))

# 일단 처음 2개 원소를 비교하자
# 1. ascending or mixed
if notes[0] < notes[1]:
    is_ascending = True
    is_mixed = False

    for i in range(1, len(notes) - 1):
        if notes[i] < notes[i + 1]:
            continue
        else:
            is_ascending = False
            is_mixed = True
            break

    if is_ascending == True:
        print('ascending')
    if is_mixed == True:
        print('mixed')

# 2. descending or mixed
else:
    is_descending = True
    is_mixed = False

    for i in range(1, len(notes) - 1):
        if notes[i] > notes[i + 1]:
            continue
        else:
            is_descending = False
            is_mixed = True
            break

    if is_descending == True:
        print('descending')
    if is_mixed == True:
        print('mixed')

'''
# 천재 코드
lst = list(map(int, input().split()))

if lst == sorted(lst):
    print('ascending')
elif lst == sorted(lst, reverse=True):
    print('descending')
else:
    print('mixed')
'''