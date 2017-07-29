class passmarks():

    # x = 50
    # y = 70
    # z = 120
    def validate(self, x, y, z):
        if x and y and z in range(150):
            print("valid marks!")
            subjectsfail = 0
            if x in range(70):
                # print("1 subject failed")
                subjectsfail += 1
            if y in range(70):
                # print("1 subject failed")
                subjectsfail += 1
            if z in range(70):
                # print("1 subject failed")
                subjectsfail += 1
            return subjectsfail
        else:
            print("invalid figures!")

    def whattodo(self, subjectsfail):
        if subjectsfail == 0:
            print("carry on!")
        if subjectsfail == 1:
            print("repeat the subject!")
        if subjectsfail == 2:
            print("repeat the year!")
        if subjectsfail == 3:
            print("Go home!")


def main():
    John = passmarks()
    x = John.validate(20, 40, 69)
    John.whattodo(x)


main()
