#Пользователь вводит длину (height) и ширину (width) прямоугольника, программа должна посчитать и вывести его площадь и периметр

width = int(input('введите ширину: '))
height = int(input('введите длину: '))
print(f'S = {width} * {height} = {width * height}')
print(f'P = 2 * ({width} + {height}) = {2 * (width + height)}')