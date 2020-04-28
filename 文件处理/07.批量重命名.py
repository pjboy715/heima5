# 将文件夹内所有文件重命名 Python_xxxx
# 将文件夹内所有文件重命名删除Python_

import os

# 构造条件数据
flag = 2

# 1.找到所有文件：获取文件夹的目录列表
file_list = os.listdir()
print(file_list)

# 2.构造名字
for i in file_list:
    if flag == 1:
        # 添加前缀
        new_name = 'Python_' + i
    elif flag == 2:
        # 删除前缀
        num = len('Python_')
        new_name = i[num:]
    # 3.重命名
    os.rename(i, new_name)
