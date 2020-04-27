# credits(func,lst),其中func必须有两个参数。每次func计算的结果继续和序列的下一个元素做累积计算
# 注意：reduce()传入的参数func必须接收两个参数

list1 = [1, 2, 3, 4, 5]

# 1.导入模块
import functools


# 2.定义功能函数
def func(a, b):
    return a + b


# 调用reduce,计算列表的累加求和
result = functools.reduce(func, list1)
print(result)
