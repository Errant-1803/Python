n = int(input('введите кол-во чисел: '))
pos = 0
neg = 0
z = 0
for i in range(n):
    x = int(input())
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    else:
        z += 1
print(f'Положительные: {pos}')
print(f'Отрицательные: {neg}')
print(f'Нули: {z}')
