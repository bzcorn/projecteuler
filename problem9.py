import math

x = 1
aList = []
while x <= 1000:
    aList.append(x * x)
    x += 1

i = 1
while i < len(aList):
    j = i + 1
    while j < len(aList):
        if (i**2 + j**2) in aList:
            k = math.sqrt(i**2 + j**2)
            if (i + j + k) == 1000:
                print "%s %s %s" % (i, j, k)
                print i * j * k
        j += 1
    i += 1