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


