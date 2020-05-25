import multiprocessing


# 显示信息的任务
def show_info(name, age):
    print(name, age)


if __name__ == '__main__':
    # 创建子进程
    # 以元组方式传参数,元组里的元素顺序要和函数参数保持一致
    # sub_process = multiprocessing.Process(target=show_info, args=('李四', 20))

    # 以字典方式传参数，字典里的key和函数参数名要保持一致
    # sub_process = multiprocessing.Process(target=show_info, kwargs={'name':'李四','age':20})

    # 以元组和字典混合方式传参数
    sub_process = multiprocessing.Process(target=show_info, args=('李四',), kwargs={'age': 20})

    # 启动进程
    sub_process.start()
