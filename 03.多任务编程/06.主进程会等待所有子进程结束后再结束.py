import multiprocessing
import time


def task():
    # for i in range(10):
    while True:
        print('任务执行中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=task)
    # 将子进程设置为守护主进程，以后主进程退出子进程直接销毁
    # sub_process.deamon = True
    sub_process.start()

    # 主进程延时0.5秒
    time.sleep(0.5)
    # 退出主进程之前，先让子进程进行销毁
    sub_process.terminate()
    print('over')

# 结论：主进程会等待子进程执行完成以后程序再退出
