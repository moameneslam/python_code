def one():
    print("I passed your function into a function")


def two(x):
    one()
    print("so you can function while you function")


def main():
    two(one)


main()
