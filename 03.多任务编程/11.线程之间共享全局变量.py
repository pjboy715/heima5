import threading
import time

g_list = []


def add_data():
    for i in range(3):
        g_list.append(i)
        print('add:', i)
        time.sleep(0.2)
    print('添加数据完成：', g_list)


def read_data():
    print('read:', g_list)


if __name__ == '__main__':
    # 创建线程
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    # 启动线程
    add_thread.start()
    # 让当前线程执行完后继续执行
    add_thread.join()
    read_thread.start()

# 结论：因为多线程在一个进程内，线程之间共享全局变量
