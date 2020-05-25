import threading
import time


def sing():
    # 获取当前线程
    print(threading.current_thread())
    for i in range(3):
        print('唱歌中...')
        time.sleep(0.2)


def dance():
    # 获取当前线程
    print(threading.current_thread())
    for i in range(3):
        print('跳舞中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 获取当前线程
    print(threading.current_thread())
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()
