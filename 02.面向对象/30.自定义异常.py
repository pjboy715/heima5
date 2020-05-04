# 1.自定义异常类，继承Exception
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    # 设置抛出异常的描述信息
    def __str__(self):
        return f'输入的长度是{self.length}个字符，不能少于{self.min_len}个字符'


def main():
    # 2.抛出异常:用户输入密码，如果长度小于3，抛出异常
    try:
        password = input('请输入密码:')
        if len(password) < 3:
            # 抛出异常类创建的对象
            raise ShortInputError(len(password), 3)
    # 3.捕获异常
    except Exception as result:
        print(result)
    else:
        print('密码输入完成')


main()
