import multiprocessing
import time

# 定义全局变量列表
g_list = list()


# 添加数据的任务
def add_data():
    for i in range(3):
        g_list.append(i)
        print('add', i)
        time.sleep(0.2)


# 读取数据的任务
def read_data():
    print('read', g_list)


if __name__ == '__main__':
    # 添加数据子进程
    add_prosess = multiprocessing.Process(target=add_data)
    # 读取数据子进程
    read_prcess = multiprocessing.Process(target=read_data)

    # 启动进程
    add_prosess.start()
    read_prcess.start()
