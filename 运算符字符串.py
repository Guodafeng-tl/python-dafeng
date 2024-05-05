"""
  标识符命名  只允许 中文、英文、数字、下划线_ 这四类元素
  不推荐中文、数字不允许用在开头
  不可使用关键字 True False None ..
"""
andy = "安迪"
print(andy)

print("8+3=", 8 + 3)
print("8-3=", 8 - 3)
print("8*3=", 8 * 3)
print("8/3=", 8 / 3)
print("8//3=", 8 // 3)
print("8**3=", 8 ** 3)
print("8%3=", 8 % 3)

"""
 关于字符串
 三引号  用变量接收就是 字符串
"""

name_str = """dafeng"""
print(name_str)

name_str1 = '"aq1"'
print(name_str1)
name_str2 = "'aq2'"
print(name_str2)
name_str3 = "\"test3"
print(name_str3)

name_str4 = "\"test4\""
print(name_str4)

namea = "python"
nameb = "I love %s" % namea
print(nameb)

software = "2015"
money = 300000
info = "you know %s 级 平均薪资%s" % (software, money)
print(info)

"""
    %s  字符串占位
    %d   整数占位
    %f   浮点型占位
    m.n 宽度.精度 【m比数字本身宽度小 忽略】
"""

num1 = 888
num2 = 999.9998766
print("num1宽带2 %2d" % num1)
print("num1宽带5 %5d" % num1)
print("num2宽带2 小数5 %2.5f" % num2)
print("num2宽带1 小数6 %1.6f" % num2)
print("num2宽带3 小数6 %3.6f" % num2)
print("num2宽带6 小数7 %6.7f" % num2)
print("num2宽带4 小数7 %.7f" % num2)

# 字符串 格式化 快速写法 忽略精度可使用
a1 = "科技"
a2 = 2026
a3 = "落寞"
print(f"java：{a1},从{a2},开始{a3}")
