numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = 1
n = 15
for number in range(1, n + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                not_primes.append(number)
                break
            i -= 1
        else:
            primes.append(number)
print('Primes:', primes)
print('Not_primes:', not_primes)
