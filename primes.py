def isprime(i):
    if i <= 1:
        # pass
        return False
    if i <= 3:
        return i
    if i % 2 == 0 or i % 3 == 0:
        # pass
        return False
    j = 5
    while j * j <= i:
        if i % j == 0 or i % (j + 2) == 0:
            # pass
            return False
        j = j + 6
    return i


for i in range(10, 1000):
    if isprime(i) == False:
        pass
    else:
        print(isprime(i))
