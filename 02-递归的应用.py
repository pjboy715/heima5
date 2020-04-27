# 递归特点：函数内部自己调用自己；必须有出口

def sum_num(num):
    # 如果是1，直接返回1 -- 出口
    if num == 1:
        return 1
    # 如果不是1，重复执行累加并返回结果
    return num + sum_num(num - 1)


sum_result = sum_num(100)
print(sum_result)
