import math

def is_composite(num):
    if num % 2 == 0 and num != 2:
        return True
    return False

def is_prime(num):
    if is_composite(num):
        return False
    upper = math.ceil(math.sqrt(num))
    x = 3
    # iterate through all possible factors
    while x <= upper:
        # If number has remainder = 0, False
        if num % x == 0:
            return False
        x += 1
    return True

y = 1
i = 2
while y <= 10001:
    if is_prime(i):
        print "%s, %s" % (y, i)
        y += 1
    i += 1
