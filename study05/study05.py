#字符串格式化
"""
收获:
1.在py中不仅可以利用元组将C的printf的用法带入py
2.而且还有独特的f-string的方式格式化字符串
"""

#C风格
"""
print("Var 1 = %s,Var 2 = %s, Var 3 = %s"%(1,2.2,"test"))

print("var = %010d." %120)
print("var = %-10d." %120)

print("var = %010f" % 3.1415)
print("var = %f" % 3.1415)
print("var = %.2f" % 3.1415)
"""

#f-string风格
"""
var1 = 10
var2 = 3.667788990011
var3 = "test"
print(f"var1={var2}var1={var2}var3={var3}")

print(f"var1 ={var1:10}.")
print(f"var3 ={var3:10}.")
print(f"var1 ={var1:<10}.")
print(f"var3 ={var3:>10}.")

print(f"var2 ={var2:.3f}")

print(f"var1 ={var1:08}")

print(f"var3 ={var3:>08}")

print(f"{1024} = 0x{1024:x}")

print(f"{{")
"""

#作业
"""
str1 = "Hello "
str2 = "world!"

print("%s%s" %(str1,str2))
print(f"{str1}{str2}")

name = input("名字:")
age = input("年龄:")
print(f"您的名字是:{name:>4}您的年龄是:{age:>3}")
print("您的名字是:%4s您的年龄是:%3s"%(name,age))

info = [
    ['user1', 345.6, 12, '黄金'],
    ['user2', 2345.6, 8, '白银'],
    ['user3555', 55345.6, 22, '钻石'],
]

print(f"用户名:{info[0][0]:<8}积分:{info[0][1]:<8}等级:{info[0][2]:<5}头衔:{info[0][3]:<4}")
print(f"用户名:{info[1][0]:<8}积分:{info[1][1]:<8}等级:{info[1][2]:<5}头衔:{info[1][3]:<4}")
print(f"用户名:{info[2][0]:<8}积分:{info[2][1]:<8}等级:{info[2][2]:<5}头衔:{info[2][3]:<4}")


str1 = "test1 "
str2 = "test2 "

Str3 = str1 + str2
print(f"Str3 = {Str3}")
Str3 = '%s%s'%(str1,str2)
print(f"Str3 = {Str3}")
Str3 = '{}{}'.format(str1,str2)
print(f"Str3 = {Str3}")
Str3 = f'{str1}{str2}'
print(f"Str3 = {Str3}")
"""


