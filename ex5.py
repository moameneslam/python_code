print("times tables. input ranges")
print("_______________________________")
x = int(input("input first integer"))
y = int(input("input second integer"))
if x <= y:
    for a in range(x, y + 1):
        for b in range(1, 11):
            out = a * b
            print("%d x %d = %d" % (a, b, out))
else:
    for a in range(x, y - 1, -1):
        for b in range(1, 11):
            out = a * b
            print("%d x %d = %d" % (a, b, out))
