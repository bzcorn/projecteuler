i = 0
sum = 0

def get_multiple(num, multiple):
    if (num % multiple == 0):
        return True
    else:
        return False
    print i

while i < 1000:
    if get_multiple(i, 3) or get_multiple(i, 5):
        sum += i
    i += 1

print sum