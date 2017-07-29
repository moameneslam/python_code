# make it print 0 at the output
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
        if x > 3.13 and x < 3.15:
            return math.sin(x)
            print("!")
        else:
            return lambda n: n + x


class Error(Exception):
    pass


class InputError(Exception):

    def __init__(self):
        pass
inp = float(input("please enter a number"))
try:
    ref = two()
    x = ref.one(random.random())
    j = ref.function(inp)
    if inp == 0.0:
        raise InputError()
except InputError:
    print("Cheater! can't input 0!")
print(math.floor(j))
