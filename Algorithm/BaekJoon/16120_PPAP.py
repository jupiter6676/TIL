string = input()
stack = list()

ppap = ['P', 'P', 'A', 'P']

if string == 'PPAP' or string == 'P':
    print('PPAP')

else:
    for ch in string:
        stack.append(ch)

        if stack[-4 :] == ppap:
            for _ in range(3):
                stack.pop()

    if stack == ['P'] or stack == ppap:
        print('PPAP')
    else:
        print('NP')