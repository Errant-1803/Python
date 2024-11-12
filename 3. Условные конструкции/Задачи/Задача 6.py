a = int(input('1) '))
b = int(input('2) '))
c = int(input('3) '))
h = a
c1 = a
c2 = a
if b > h:
    h = b
if c > h:
    h = c
if b < c1:
    c1 = b
if c < c1:
    c1 = c
c2 = (a + b + c) - (h + c1)
if c1 + c2 >= h:
    print('не существует')
elif (c1 ** 2 + c2 ** 2) < h ** 2:
    print("тупоугольный")
elif (c1 ** 2 + c2 ** 2) > h ** 2:
    print('остроугольный')
elif (c1 ** 2 + c2 ** 2) == h ** 2:
    print('прямоугольный')