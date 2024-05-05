name = "xewefe"
for x in name:
    print(x)

print("1111111111111111111")
#  range 从默认0开始  左开右闭

for x in range(1,9):
    print(x)

print("=-=========================")

for x in range(5,9,2):
    print(x)

print("2222222222222")
for y in range(10):
    print("送玫瑰花 %d" % y)

print("99乘法表输出=====================")

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i} ={j * i}\t", end='')
    print()

print("contineu=========================")

for i in range(1,8):
    print("哈哈哈哈 %d" % i)
    continue
    print("啦啦啦啦")


print("break========================")

for i in range(1,100):
    print("嘿嘿嘿嘿额 %d" %i)
    if i == 10:
        break
    print("牛牛牛牛牛 %d" % i)