class test():

    def __init__(self, a, b=0, c=0):
        self.i = a
        self.j = b
        self.k = c

    def __add__(self, x):
        return self.i * x.i


x = test(5)
y = test(6)
print(x + y)
