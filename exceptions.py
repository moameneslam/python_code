import random
import math


class one():

    def message(self):
        print("test")


class two():

    def one(self, arg):

        self.arg = arg
        return self.arg

    def function(self, x):
        ref = one()
        ref.message()
        return lambda n: n + x
inp = int(input("please enter a number"))


class C(Exception):

    def __init__(self, value):
        self.param = value

    def __str__(self):
        return repr(self.parame)

try:
    ref = two()
    x = ref.one(random.random())
    j = ref.function(math.floor(x))
    raise Cheater("cant enter zero")

except Cheater(ref):

    print("error:" + ref.param)
    # print(j(inp))
