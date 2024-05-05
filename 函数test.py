def say_hi():
    print("hhhhhh")


res = say_hi()
print("res============== %s" % res)
print("res============== %s" % type(res))


def sumTest(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    result = x + y
    print(f"{x} + {y} = {result}")


sumTest(8, 6)

print("ttttttttttttt---")

# 全局变量在函数中 只是局部变量  除非使用global
num = 800
print("======num,", num)


def add(x):
    x = x + 100
    print("xxxxxxxxxxxxxx=", x)


def originalValue(xy):
    print(xy)


add(num)
originalValue(num)
print("final num ====", num)


def addTest():
    global num
    num += 100
    print("xxxxxxxxxxxxxxaddTest=", num)


addTest()
print("=======number值 %d" % num)
