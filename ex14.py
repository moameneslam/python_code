string = "aabbccc"

for j in range(65, 92):

    letter = 0
    for i in string:
        ascii = int(format(ord(i), 'd'))

        if ascii == j or ascii == j + 32:
            letter += 1
    #print(chr(ascii), letter)

    if letter > 0:
        ascii = j
        print(chr(ascii), letter)
