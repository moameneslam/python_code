from os import path
# import math


def keys():
    key = 12382723
    return key


def encode(data):
    filename = str(keys()) + ".txt"
    f = open(filename, "w")
    for i in data:
        m = format(ord(i), 'b')
        # binaries get xored wit the key. write replacer for number to keys
        x = int(m) ^ keys()
        # print(int(m))
        f.write(str(x) + ",")
        # print(x, ",")


def main():

    func = input("decrypt or encrypt?: ")
    if func == "encrypt":
        file = input("enter file name: ")
        if path.exists(file):
            print("file found!")
            print(file)

            x = open(file, "r")
            data = x.read()

            encode(data)
            # print(data)
        else:
            print("file not found!")

    else:
        file = input("enter file name: ")
        if path.exists(file):
            print("file found!")
            print(file)

            x = open(file, "r")
            data = x.read()

            decode(data)
            # print(data)
        else:
            print("file not found!")


def decode(data):
    string = ""
    out = open("out.txt", "w")
    for i in data:

        if i == ",":
            # print(string)
            x = int(string) ^ keys()
            string = ""
            y = str(x)
            z = int(y, 2)
            letter = chr(z)
            out.write(letter)
            # print(letter)
        else:
            string += str(i)
            # m = format(ord(i), 'b')
            # binaries get xored wit the key. write replacer for number to keys
            # x =
            # f.write(str(x))
        # print(x)


main()
