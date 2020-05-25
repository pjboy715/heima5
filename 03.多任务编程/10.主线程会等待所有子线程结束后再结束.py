import threading
import time


def task():
    while True:
        print('任务执行中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # deamon = True 表示创建的子线程守护主线程，主线程退出子线程直接销毁
    # sub_thread = threading.Thread(target=task,daemon=True)

    sub_thread = threading.Thread(target=task)
    # 将子线程设置为守护主线程
    sub_thread.setDaemon(True)
    sub_thread.start()

    # 主线程延时执行1秒
    time.sleep(1)

    print('over')
    exit()
