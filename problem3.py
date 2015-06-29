import math

def get_factors(num):
    factors = []
    i = 2
    while i < math.sqrt(num):
        if num % i == 0:
            factors.append(i)
        i += 1
    return factors

def is_list_prime(list):
    prime_numbers = []
    for item in list:
        i = 2
        flag = True
        while i < math.sqrt(item):
            if item % i == 0:
                flag = False
            i += 1
        if flag == True:
            prime_numbers.append(item)
    return prime_numbers

print max(is_list_prime(get_factors(600851475143)))
