class Washer():
    def __init__(self):
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f'洗衣机宽度是:{self.width}')
        print(f'洗衣机高度是:{self.height}')


haier = Washer()
haier.print_info()
