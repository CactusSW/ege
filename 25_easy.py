lst = []
for i in range(1, 10001):
    if i % 5 == 0 and i % 9 == 0:
        lst.append(str(i))

#  1!2?14*
for i in lst:
    for j in '0123456789':
        s = int(f'1{i}2{j}14')
        if s % 1917 == 0 and s < 10**8:
            print(s)
for i in lst:
    for j in '0123456789':
        for k in '0123456789':
            s = int(f'1{i}2{j}14{k}')
            if s % 1917 == 0 and s < 10**8:
                print(s)


