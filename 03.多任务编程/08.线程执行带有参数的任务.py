import threading


def show_info(name, age):
    print(name, age)


if __name__ == '__main__':
    # 元组传递参数
    # sub_thread = threading.Thread(target=show_info, args=('李四', 20))
    # sub_thread.start()

    # 字典传递参数
    sub_thread = threading.Thread(target=show_info, kwargs={'name': '李四', 'age': 20})
    sub_thread.start()
