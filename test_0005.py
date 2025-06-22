z = int(input())
if z == 0:
    print(-1)
else:
    n = abs(z)
    c = 0

    i = 1
    while i * i <= n:
        if n % i == 0:
            c += 1
            if i * i != n:
                c += 1
        i += 1

    res = c + 1 if c % 2 == 1 and z > 0 else c
    print(res)