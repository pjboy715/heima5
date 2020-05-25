# 死锁：一直等待对方释放锁的情景叫做死锁
import threading

# 创建互斥锁
lock = threading.Lock()


def get_value(index):
    lock.acquire()
    my_list = [1, 4, 6]
    if index >= len(my_list):
        print('下标越界：', index)
        # 取值失败，也许要释放互斥锁，不要影响后面的线程去取值
        lock.release()
        return
    value = my_list[index]
    print(value)
    lock.release()


if __name__ == '__main__':
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()
