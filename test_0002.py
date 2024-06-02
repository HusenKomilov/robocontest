a = input()
c = a.split()


if int(c[0]) == int(c[1]):
    print('=')
if int(c[0]) > int(c[1]):
    print('>')
if int(c[0]) < int(c[1]):
    print('<')
