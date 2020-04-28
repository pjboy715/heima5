# 家具类
class Furniturn():
    def __init__(self, name, area):
        # 家具名
        self.name = name
        # 家具占地面积
        self.area = area


# 房子类
class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def add_furniture(self, item):
        # 容纳家具
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 家具搬入后，房屋面积 = 之前剩余面积 - 家具面积
            self.free_area -= item.area
        else:
            print('家具面积太大，无法容纳该家具')

    def __str__(self):
        # 返回状态信息
        return f'房子地理位置在：{self.address}，' \
               f'房屋面积是：{self.area}，' \
               f'剩余面积是：{self.free_area}，' \
               f'家具有：{self.furniture}'


# 家具
bad = Furniturn('双人床', 6)
sofa = Furniturn('沙发', 10)
ball = Furniturn('篮球场', 200)

# 房子
jia1 = Home('北京', 100)

jia1.add_furniture(bad)
print(jia1)

jia1.add_furniture(sofa)
print(jia1)

jia1.add_furniture(ball)
print(jia1)
