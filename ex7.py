x = open("abc.txt", "r")
data = x.read()
x.close
x = open("abc.txt", "w")
print(data)
for char in data:
    if char == "Q" or char == "q":
        print("yay!")

        y = "*"
        x.write(y)
    else:
        x.write(char)
print("new")

x.close()
y = open("abc.txt", "r")
data1 = y.read()
print(data1)
