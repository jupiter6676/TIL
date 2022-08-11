fbi_list = list()

for i in range(1, 6):
    person = input()

    if 'FBI' in person:
        fbi_list.append(i)

if fbi_list:
    print(*fbi_list)
else:
    print('HE GOT AWAY!')