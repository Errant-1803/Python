a = int(input('1) '))
b = int(input('2) '))
c = int(input('3) '))
h = max(a, b, c)
c1 = min(a, b, c)
c2 = (a + b + c) - (h + c1)
if c1 + c2 >= h:
    print('не существует')
elif (c1 ** 2 + c2 ** 2) < h ** 2:
    print("тупоугольный")
elif (c1 ** 2 + c2 ** 2) > h ** 2:
    print('остроугольный')
elif (c1 ** 2 + c2 ** 2) == h ** 2:
    print('прямоугольный')