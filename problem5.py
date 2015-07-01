def roll_down(num, iteration):
    if num % iteration == 0:
        print "%s and iteration %s" % (num, iteration)
        return True
    return False

def logic():
    num = 1
    while True:
        iteration = 20
        while roll_down(num, iteration):
            iteration = iteration - 1
            if iteration == 1:
                return "The number is %s" % (num)
        num += 1

print logic()