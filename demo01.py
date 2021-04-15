""" # print  """

""" print("helloworld!") #字符串 str
#print(3333) #整数  int
print(2.22) #小数 float
print(True) #布尔值   bool    False 首字母要大写！
print(())  #元组 tuple
print([])  #数组  list
print({}) #字典 dict """
 
# print("哈哈",222)
# print("哈哈"+"嘻嘻") #字符串拼接  
# print("哈哈"*100)  #输出100个哈哈
# print(2+2*(5-1)) #数学运算
# print(2>3)#布尔值

# """ #多行注释
""" 变量
#赋值 """
# name = "张三" #把张三这个值赋值给name这个变量  变量名小写
# print(name)
#input   特点： 不论输入是什么都默认为字符串 """
# a = input("请输入第一个数：")
# b = input("请输入第二个数：")
# print(a+b)   #此处结果为字符串拼接

# print(type("哈哈哈"))
# print(type(2333))
# print(type(2.3))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))
  
"""  数据转换 
  任何数据都可以转换成字符串，除了none 
  整数和小数可以互相转换
  字符串转换为其他类型的数据，必须满足长得像这个条件  """
# a = str(2444)
# print(type(a))
# #数字相加
# a = float(input("请输入第一个数："))
# b = float(input("请输入第二个数："))
# print(a+b)   #此处结果数值

# a = "哈哈哈"
# print(len(a))

a = input("请输入一段文字：")
b = input("请输入一段文字：")
print(len(a+b))