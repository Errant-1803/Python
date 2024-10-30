n1 = int(input())
hours = n1 // 3600
minutes = n1 % 3600 // 60
seconds = n1 % 60
print(f'{hours}:{minutes}:{seconds}')