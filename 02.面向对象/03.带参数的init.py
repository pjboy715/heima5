class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机宽度是:{self.width}')
        print(f'洗衣机高度是:{self.height}')


haier = Washer(10, 20)
haier.print_info()

samsung = Washer(20, 30)
samsung.print_info()
