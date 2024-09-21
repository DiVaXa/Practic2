numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a = 1
n = 15
print (numbers)
for number in range(a, n + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
primes = [2,3,5,7,11,13]
not_primes = [1,4,6,8,9,10,12,14,15]
print ('Primes:',primes)
print ('Not_primes:',not_primes)