from math import sqrt
from typing import List
import matplotlib.pyplot as plt

from common.point import Point


class DouglasPeucker:
    def __init__(self, points: List[Point], tolerance: float):
        """
        道格拉斯-普克轨迹压缩算法
        :param points: 轨迹点
        :param tolerance: 最大距离阈值
        """
        self.points = points
        self.tolerance = tolerance
        self.compressed_points = []

    @staticmethod
    def calc_height(start_point: Point, end_point: Point, point: Point):
        x1, y1 = start_point.x, start_point.y
        x2, y2 = end_point.x, end_point.y
        x3, y3 = point.x, point.y
        area = 0.5 * abs(x1 * y2 - x2 * y1 + x2 * y3 - x3 * y2 + x3 * y1 - x1 * y3)
        bottom = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        return 2 * area / bottom

    def dp(self, start_index: int, end_index: int):
        max_distance = 0.0
        max_distance_index = 0
        for index in range(start_index + 1, end_index):
            distance = self.calc_height(self.points[start_index], self.points[end_index], self.points[index])
            if distance > max_distance:
                max_distance = distance
                max_distance_index = index
        if max_distance > self.tolerance and max_distance_index != 0:
            # print(start_index, max_distance_index, end_index)
            self.dp(start_index, max_distance_index)
            self.compressed_points.append(self.points[max_distance_index])
            self.dp(max_distance_index, end_index)

    def compress(self):
        if self.points is None or len(self.points) < 3:
            return self.points
        n = len(self.points)
        i, j = 0, n - 1
        # 保留首尾并保持加入结果集的点的顺序
        self.compressed_points.append(self.points[i])
        self.dp(i, j)
        self.compressed_points.append(self.points[j])
        return self.compressed_points


if __name__ == '__main__':
    data = []
    with open("./data/traj.txt", "r") as f:
        for line in f.readlines():
            temp = line.split(",")
            data.append(Point(temp[0], float(temp[1]), float(temp[2])))
    dp = DouglasPeucker(data, 10)
    res = dp.compress()
    for p in res:
        print("{},{},{}".format(p.pid, p.x, p.y))
    print("compress rate: %.2f" % (len(res) / len(data)))
    # 可视化
    raw_x = [p.x for p in data]
    raw_y = [p.y for p in data]
    compressed_x = [p.x for p in res]
    compressed_y = [p.y for p in res]
    plt.subplot(1, 2, 1)
    plt.plot(raw_x, raw_y, marker='o')
    plt.title("RAW")
    plt.subplot(1, 2, 2)
    plt.plot(compressed_x, compressed_y, marker='o')
    plt.title("COMPRESSED")
    plt.show()
    print("ok")
