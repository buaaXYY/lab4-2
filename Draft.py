class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x +=dx
        self.y +=dy

    def distance(self, other):
        lens =  ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return f'{lens:.2f}'


d1 = Point(10, 28)
d1.move_to(50, 89)  # 表示移动到这个点（50,89）
d1.move_by(10, 10)  # 表示在原坐标的基础上移动，移动后的点为（20,38）


class Line:
    # start和end是Point类实例化的对象
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def length(self):
        # 返回练习一中的距离方法
        return self.start.distance(self.end)

    def relationship(self, other):
        # 给四个点
        sx1, sy1, ex1, ey1 = self.start.x, self.start.y, self.end.x, self.end.y
        sx2, sy2, ex2, ey2 = self.start.x, self.start.y, self.end.x, self.end.y

        # 斜率法判断两条线之间的关系，斜率不等则相交
        if (ey1 - sy1) / (ex1 - sx1) != (ey2 - sy2) / (ex2 - sx2):
            print('相交')
        else:
            print('平行')


if __name__ == "__main__":
    p1 = Point(2, 3)
    p2 = Point(4, 5)
    p3 = Point(8, 9)
    p4 = Point(10, 12)

    print(p3.distance(p4))      # 计算两个点的距离
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    line1.relationship(line2)   #判断两条直线的关系