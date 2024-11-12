n = int(input('кол-во грибов: '))
n1 = n % 10
n2 =n % 100
if 11 <= n2 <= 14:
    print('грибов')
elif n1 == 1:
    print('гриб')
elif 2 <= n1 <= 4:
    print('гриба')
else:
    print('грибов')