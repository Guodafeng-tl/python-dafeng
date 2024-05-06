f = open("D:/python/python-learn/dafeng-learn/test.txt", "r", encoding="UTF-8")
print(f"f==== {type(f)}")
print(f.read())
print(f.close())

f = open("D:/python/python-learn/dafeng-learn/test.txt", "r", encoding="UTF-8")
print(f"f==== {type(f)}")

lines = f.readlines()
print(f"f.readline==== {type(f.readlines())}")
print(f"line========{lines}")
print(f"line========{f.close()}")

with open("D:/python/python-learn/dafeng-learn/test.txt", "r", encoding="UTF-8") as test:
    for x in test:
        print(f"============{x}")

print("wwwwwwwwwwwwwwwwwwwww=")


#w模式  文件不存在 创建 、文件存在  覆盖文件内容
f = open("D:/python/python-learn/dafeng-learn/dafeng.txt", "w", encoding="UTF-8")
f.write("I LOVE PYTHON")
f.flush()
f.close()
print("sssssssssssssssssss")

#a模式文件不存在 创建文件、文件存在 追加文件内容


