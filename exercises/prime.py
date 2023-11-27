def prime_check(num):
    if num <= 2:
        return True
    for n in range(2, num):
        if (num % n) == 0:
            return False
    return True
number = int(input('Choose a number: '))
print(prime_check(number))