import threading

# 全局变量
from typing import Any, Union

# 全局变量
g_num = 0

# 创建互斥锁 Lock
lock = threading.Lock()


# 循环100万次循环任务
def task1():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        # 声明全局变量，并修改
        global g_num
        g_num = g_num + 1
    print('task1:', g_num)
    # 释放锁
    lock.release()


def task2():
    lock.acquire()
    for i in range(1000000):
        # 声明全局变量，并修改
        global g_num
        g_num = g_num + 1
    print('task2:', g_num)
    lock.release()


if __name__ == '__main__':
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    first_thread.start()
    # 线程等待(join)
    # first_thread.join()
    second_thread.start()

    # 互斥锁可以保证同一时刻只有一个线程去执行代码，保证全局变量数据的准确
    # 线程等待和互斥锁都是把多任务改成单任务去执行，保证数据准确性，但是执行性能会下降
