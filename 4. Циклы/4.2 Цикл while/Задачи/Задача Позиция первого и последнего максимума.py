max = 0
index = 1
last_max = 0
first_max = 0
while (a := int(input(':'))) != 0:
    if a > max:
        max = a
        first_max = index
    if a == max:
        last_max = index
    index += 1
print(first_max,';',last_max)