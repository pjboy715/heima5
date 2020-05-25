import multiprocessing
import time


def task():
    time.sleep(1)
    # 获取当前进程
    print(multiprocessing.current_process)


if __name__ == '__main__':
    # 循环创建大量进程，测试进程之间是否无序
    for i in range(20):
        # 每次循环创建一个子进程
        sub_thread = multiprocessing.Process(target=task)
        # 启动进程
        sub_thread.start()

# 结论：进程之间执行是无序的，由操作系统调度决定的
