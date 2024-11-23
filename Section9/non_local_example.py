def spam1():
    def spam2():
        def spam3():
            z = " even more spam"
            z += y
            print("In spam3, locals are {}".format(locals()))
            return z

        y = " more " + x
        y += spam3()
        print("In spam2, locals are {}".format(locals()))
        return y

    x = "spam"  # x must be defined before spam2() is called
    x += spam2()  # do not combine these two lines
    print("In spam1, locals are {}".format(locals()))
    return x


print(spam1())
print(locals())
print(globals())
