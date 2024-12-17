'''
a < b
'''
a = int(input('a = '))
b = int(input('b = '))
sum = 0
while a <= b:
    sum += a
    a += 1
print(sum)