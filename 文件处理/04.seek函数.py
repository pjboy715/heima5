'''
语法：文件对象.seek(偏移量，起始位置) 0开头 1当前 2结尾
'''
# 1.r模式改变指针至结尾
# f = open('test.txt', 'r+')
#
# f.seek(0, 2)
#
# content = f.read()
# print(content)
#
# f.close()

# 2.a模式改变指针至开头
f = open('test.txt', 'a+')

f.seek(0, 0)

content = f.read()
print(content)

f.close()
