# 1.尝试打开test.txt (r模式)，如果文件不存在，用(w模式)打开
'''
try:
    可能发生错误的代码
except 异常类型：
    如果捕获到该异常类型执行的代码
'''
try:
    f = open('test.txt', 'r')
except:
    f = open('test.txt', 'w')
