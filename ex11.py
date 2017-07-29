import math

ones = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
    0: ''
}
range1 = 1
range2 = 300


def singleDigits():
    for i in range(range1, range2 + 1):
        x = i % 10
        y = i % 100
        print(i)
        if i in range(10, 20):
            out1 = teens[y]
        if x == 0:
            pass
        else:
            out2 = ones[x]

        return (out1, out2)


def doubles():
    for i in range(range1, range2 + 1):
        x = i % 100
        y = x / 10
        z = (math.floor(y))
        if x not in range(10, 20):
            if z != 0 or 1:
                print(tens[z])


def main():
    print(doubles(), singleDigits())

# doubles()
# singleDigits()
