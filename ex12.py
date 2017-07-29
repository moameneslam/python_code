class test():
    """docstring for ClassName"""

    def message(self):
        print("test!")

    def add(self, A, B):
        c = A + B
        return c

    def something(self):
        f = self.add(12, 11)
        return f

ref = test()
ref.message()
print(ref.add(6, 5))
print(ref.something())
ref.message()
