"""
    数据容器
    列表 list
        有序、可重复、大小上限  2**63-1、容纳不容类型元素、可以修改
    元组 tuple
       只读不可修改、有序可重复、\容纳不容类型元素\嵌套list list可修改
    字符串 str
        有序、不支持修改 replace实际是生成新的字符串

    序列
       内容连续、有序 可以使用下标索引的 容器 比如上面三种
    集合 set
        不支持元素重复、且无序、不支持下标索引、允许修改
    字典 dict
        key->value
"""

# 列表 list

list_test = ["aa", "vvv", "www"]
print(list_test)
print(type(list_test))
list_test = ["aa", 9888, True, [1, 23]]

print(list_test)
print(type(list_test))
print(list_test[3][0])
print(list_test[-2])

#list查找元素下标 不存在报错
print(f"9888对应的下标索引%s" % list_test.index(9888))
#修改特定下标索引值
list_test[0] = "xxxx"
print(f"list_test修改元素结果后 %s" % list_test)

#插入
list_test.insert(1, "yyyy")
print(f"list_test插入元素结果后{list_test}")
#追加单个
list_test.append("python")
print(f"list_test追加元素结果后{list_test}")

#追加一批
list_test.extend(["ddd", "zzzz", False])
print(f"list_test追加一批元素结果后{list_test}")
#del 删除
del list_test[2]
print(f"list_test删除元素结果后{list_test}")

#pop取出 移除
eleinfo = list_test.pop(4)
print(f"list_test通过pop元素结果后{list_test}")

#remove
list_test.remove(False)
print(f"list_test通过remove元素结果后{list_test}")
#统计
count = list_test.count(True)
print(f"list_test通过count元素结果后{count}")

print(f"list_test通过len元素结果后{len(list_test)}")

list_test.clear()
print(f"list_test通过clear元素结果后{list_test}")


#遍历

def list_while_fun():
    my_list = ["daa", True, "xsds", 66]
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1


list_while_fun()

#元组  单个元素需要写逗号

t1 = ("111", True, 88)
t2 = ()
t3 = tuple()
print(f"元组类型=========={type(t1)},值{t1}")
print(f"元组类型=========={type(t2)},值{t2}")
print(f"元组类型=========={type(t3)},值{t3}")
#元组  单个元素需要写逗号
t4 = ("111")
print(f"元组t4类型=========={type(t4)},值{t4}")
t5 = ("111",)
print(f"元组t5类型=========={type(t5)},值{t5}")
#元组 支持下标索引

print(f"元组t1 下标1值=========={type(t1)},值{t1.index(1)}")

print(f"元组t1 len值=========={type(t1)},值{len(t1)}")

#字符串  不支持修改 replace实际是生成新的字符串
my_str = " sdhjsdcjk s dafeng "

print("mystr==========%s" % my_str)
print("mystr==========%s" % my_str.replace("s", "a"))
#strip 默认去除首尾空格
print("mystr==========%s" % my_str.strip())

#序列切片

#list切片
qiepian_list = [1, 2, 4, 5, 6, 8, 9]
result1 = qiepian_list[1:4]  #步长默认 为1 可不写
print("result1r==========%s" % result1)

#字符串切片 步长为2

my_qp_str = "987weqwj"
result_str = my_qp_str[::2]
print("result_str==========%s" % result_str)

result_str2 = my_qp_str[::-1]
print("result_str2==========%s" % result_str2)

#集合

s1 = set()
s2 = {"da", "da", "www", True, 99}

print(f"集合s1========={type(s1)},值{s1}")
print(f"集合s2========={type(s2)},值{s2}")
s2.add("python");
print(f"集合s2 add========={type(s2)},值{s2}")
s2.remove("da");
print(f"集合s2 remove========={type(s2)},值{s2}")

s3 = {"da", "www", True, 99, False, "linux"}
s4 = s2.difference(s3)
print(f"集合s4========={type(s4)},值{s4}")
s2.difference_update(s3)
print(f"集合s2difference_update=========值{s2}")

#字典

my_dict = {"dafeng": "test", "ljj": "nn"}
my_dict22 = dict()
my_dict3 = {}
print(f"my_direct1========={type(my_dict)},值{my_dict}")
print(f"my_direct2========={type(my_dict22)},值{my_dict22}")
print(f"my_direct3========={type(my_dict3)},值{my_dict3}")
value = my_dict["dafeng"]
print(f"my_direct3========={type(my_dict3)},值{value}")
my_dict["study"] = "python"
print(f"my_direct1========={type(my_dict)},值{my_dict}")
my_dict.pop("ljj")
print(f"my_direct1========={type(my_dict)},值{my_dict}")
keys = my_dict.keys();
print(f"my_direct keys========={type(my_dict)},值{keys}")

for x in keys:
    print(my_dict[x])

print(f"my_direct1========={type(my_dict)},值{len(my_dict)}")

print(f"list(my_dict)========={type(list(my_dict))},值{list(my_dict)}")

print(f"list(my_dict)========={type(list(my_dict))},值{sorted(list(my_dict),reverse=True)}")