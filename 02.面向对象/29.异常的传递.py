# 1.尝试只读打开test.txt，文件存在读取内容，不存在提示用户
# 2.循环读取内容，当无内容时退出循环，如果用户意外终止，提示用户已经被意外终止
import time

try:
    f = open('test.txt', 'r')
    # 尝试循环读取内容
    try:
        while True:
            con = f.readline()
            # 如果读取完成退出循环
            if len(con) == 0:
                break
            time.sleep(3)
            print(con)
    except:
        # 在命令提示符中如果按下ctrl+c结束终止的键
        print('程序被意外终止')
except:
    print('该文件不存在')
