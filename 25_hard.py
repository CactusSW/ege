import math

def is_square(x):
    res = math.sqrt(x)
    return res.is_integer()

def find_div(n):
    res = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    res = sorted(res)
    return res

def find_div_odd(n):
    lst = set()
    res = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            lst.add(i)
            lst.add(n // i)
    for i in lst:
        if i % 2 == 1:
            res.append(i)
    res = sorted(res)
    return res

c = 0
for i in range(500000, 10**10):
    if len(find_div(i)) == 0 or len(find_div_odd(i)) == 0:
        m = 0
        r = 0
        continue
    else:
        m = max(find_div(i)) + min(find_div(i))
        r = sum(find_div_odd(i)) // len(find_div_odd(i))
    if is_square(m*r):
        print(i, m*r)
        c += 1
    if c >= 5:
        break

