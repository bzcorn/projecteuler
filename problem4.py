def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

x = 1
y = 1
palindrome_list = []
while x < 1000:
    while y < 1000:
        if is_palindrome(x * y):
            palindrome_list.append(x * y)
        y += 1
    y = 1
    x += 1

print max(palindrome_list)
#print get_reverse(10)