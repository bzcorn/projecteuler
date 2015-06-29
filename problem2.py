i = 1
answer = 0
check = 0

def fib(n):
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b

print fib(10)
