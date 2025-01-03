def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        sum_ = sum(args)
        n = 0
        for i in range(2, sum_ // 2 + 1):
            if sum_ % i == 0:
                n = n +1
        if n <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)