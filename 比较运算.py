import random

num = random.randint(1, 100)
print("num===",num)
guess_num = int(input("输入要猜测数字: "))
if guess_num == num:
    print("恭喜你猜测正确")
else:
    if guess_num > num:
        print("猜测大了")
    else:
        print("猜测小了")

age = 10

if age >= 18:
    print("俺已经成年")
    print("你好")
elif age == 10:
    print("10岁你好")
else:
    print("还年轻")
# print("666666==")
