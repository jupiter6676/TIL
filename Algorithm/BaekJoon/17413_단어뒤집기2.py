words = input()

tmp = ''
is_tag = False

for i in range(len(words)):
    if words[i] == '<':
        if len(tmp) > 0:
            print(tmp[::-1], end='')
        
        is_tag = True
        tmp = ''


    if is_tag:        
        if words[i] == '>':
            print(tmp + '>', end='')
            tmp = ''
            is_tag = False

        elif words[i] == ' ':
            print(tmp, end=' ')
            tmp = ''

        else:
            tmp += words[i]

    else:
        if words[i] == ' ':
            print(tmp[::-1], end=' ')
            tmp = ''

        else:
            tmp += words[i]

print(tmp[::-1])