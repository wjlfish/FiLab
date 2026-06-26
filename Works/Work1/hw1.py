# 王嘉麟 2023141010176
# 金融工程实验 小作业1

# 1. 基本数据类型
a = 42
b = 3.14
c = True

print(type(a))
print(type(b))
print(type(c))

# 验证动态类型
a = "now I'm a string"
print(type(a))

# 2. 字符串操作
s = "hello world"
print(s[0])
print(s[-1])

s1 = "hello"
s2 = " python"
s3 = s1 + s2
print(s3.upper())

# 3. 数据结构
my_list = [1, "apple", 3.5, True]
print(my_list)

my_list.append("new_item")
print(my_list)

my_list.remove(3.5)
print(my_list)

# 字典
my_dict = {"name": "alice", "age": 20, "score": 95}
print(my_dict["age"])

my_dict["age"] = 21
print(my_dict)

# 4. 控制结构
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)

# 判断正负零
num = -5
if num > 0:
    print("正数")
elif num < 0:
    print("负数")
else:
    print("零")

# 5. 函数式编程
def square_list(nums):
    return [x ** 2 for x in nums]

result = square_list([1, 2, 3, 4, 5])
print(result)

# 用map和lambda实现同样的功能
result2 = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(result2)
