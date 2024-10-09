number = int (input('Введите число от 3 до 20: '))
result = ''
for i in range(1,number):
    for j in range (1,number):
        if number % (i+j) == 0 and i<j:
            result += str(i)+str(j)
print (result)