def sum_square(upper):
    x = 1
    num = 0
    while x <= upper:
        num = num + (x * x)
        x += 1
    return num

def square_of_sums(upper):
    x = 1
    num = 0
    while x <= upper:
        num = num + x
        x += 1
    return num * num

y = 100

print sum_square(100)
print square_of_sums(100)

print abs(sum_square(y) - square_of_sums(y))