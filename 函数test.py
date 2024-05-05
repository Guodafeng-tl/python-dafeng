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


#位置参数
def addTest():
    global num
    num += 100
    print("xxxxxxxxxxxxxxaddTest=", num)


addTest()
print("=======number值 %d" % num)

print("=====================函数多返回值")


def test_return():
    return 1, 2, 3


x, y, z = test_return()
print("x=====", x)
print("y=====", y)
print("z=====", z)


#关键字传参

def user_return(name, age, sex):
    print(f"名字：{name},年龄{age},性别:{sex}")


user_return(name="ww", age=20, sex="男")

#缺省参数  默认值需要是 最后参数

print("缺省参数=============")


def user_return(name, age, sex='女'):
    print(f"名字：{name},年龄{age},性别:{sex}")


user_return(name="ww", age=20)

"""
    不定长 
        1.位置传递不定长    元组
        2，关键字传递不定长  字典
        
"""


#位置传递 元组
def not_define_len(*args):
    print(f"args类型==== {type(args)} args值=== {args}")


not_define_len("TOM", 888, "上海市")


#关键字不定长  字典
def key_not_define_len(**kargs):
    print(f"kargs类型==== {type(kargs)} kargs值=== {kargs}")


key_not_define_len(name="TOM", age=888, addr="上海市")


#函数作为参数传递

def test_computer_fun(test_computer):
    res = test_computer(6,7)
    print("test_computer_fun===",res)

def test_computer(x,y):
    return x+y

test_computer_fun(test_computer)

#lambda 匿名函数

def test_lambda_fun(test_computer):
    res = test_computer(6,7)
    print("test_computer_fun===",res)
test_lambda_fun(lambda x,y : x-y)