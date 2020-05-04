# 尝试执行打印num，捕获异常类型NameError，如果捕获到则打印有错误
try:
    print(num)
except NameError:
    print('试图访问的变量名不存在')