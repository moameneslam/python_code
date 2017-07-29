#-------------------


#_---------------------------------------------------FUNCTIONS_--------


def intinput():
    x = int(input("input first integer"))
    return x


def intinput1():
    y = int(input("input second integer"))
    return y


def add(x, y):
    out = x + y
    return out


def sub(x, y):
    out = x - y
    return out


def div(x, y):
    out = x / y
    return out


def mult(x, y):
    out = x * y
    return out


def timesTable(x, y):
    if x <= y:
        for a in range(x, y + 1):

            out = a * y
            print("%d x %d = %d" % (a, y, out))
    else:
        for a in range(x, y - 1, -1):
            for b in range(1, 11):
                out = a * b
                print("%d x %d = %d" % (a, b, out))


def CONTINUEF():
    cont = input("do you want to continue? y/n")
    if cont == "n":
        main()


#-------------------------------------------------------------------------


def main():
    print("_________________calculator app____________")
    print("select from 6 choices:")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Division")
    print("4 Multiplication")
    print("5 times table")
    print("6 Quit program")
    print("___________________________________________")

    while True:
        select = int(input("make your selection "))
        if select == 1:
            x = intinput()
            y = intinput1()
            print(add(x, y))
            CONTINUEF()

        if select == 2:
            x = intinput()
            y = intinput1()
            print(sub(x, y))
            CONTINUEF()
        if select == 3:
            x = intinput()
            y = intinput1()
            print(div(x, y))
            CONTINUEF()

        if select == 4:
            x = intinput()
            y = intinput1()
            print(mult(x, y))
            CONTINUEF()
        if select == 5:
            x = int(input("enter the lower limit of yhe times table"))
            y = int(input("enter the lower limit of yhe times table"))
            print(timesTable(x, y))
            CONTINUEF()
        if select == 6:
            break


main()
