
try:
    f = open("D:/python/python-learn/dafeng-learn/hello.txt", "r", encoding="UTF-8")
except:
    print("异常了")


try:
    print(1/0)
except ZeroDivisionError as e:
    print(f"============={e}")

#多个单个异常

try:
    print(name)
except (NameError,ZeroDivisionError) as e:
    print(f"================={e}")

#捕获所有异常

try:
    f = open("D:/python/python-learn/dafeng-learn/hello.txt", "r", encoding="UTF-8")
except Exception as e:
    print(f"8888888888888==={e}")
else:
    print("开心啦啦啦啦啦啦啦")

try:
    print("9999999999999999")
except Exception as e:
    print(f"99999999999==={e}")
else:
    print("开心啦啦啦啦啦啦啦")
finally:
    print("牛您牛牛牛牛牛")