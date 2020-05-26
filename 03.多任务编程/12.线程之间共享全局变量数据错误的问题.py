import threading

# 全局变量
g_num = 0


def task1():
    for i in range(1000000):
        # 声明全局变量，并修改
        global g_num
        g_num = g_num + 1
    print('task1:', g_num)


def task2():
    for i in range(1000000):
        # 声明全局变量，并修改
        global g_num
        g_num = g_num + 1
    print('task2:', g_num)


if __name__ == '__main__':
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    first_thread.start()
    # 线程等待(join)
    first_thread.join()
    second_thread.start()
