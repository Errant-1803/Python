max = 0
while True:
    a = int(input(': '))
    if a == 0:
        break
    elif a > max:
        max = a

print(max)
