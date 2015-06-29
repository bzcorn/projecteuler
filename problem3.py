# 600851475143
def factor(num):
    list = []
    if not num % 2:
        half = ((num - 1)/2)
    else:
        half = (num/2)
    i=1
    while i < half:
        if num % i == 0:
            list.append(i)
        i += 1
    return list

print factor(600851475143)