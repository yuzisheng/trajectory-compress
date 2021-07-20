from math import sqrt
from typing import List
import matplotlib.pyplot as plt

from common.point import Point


class CurvatureStreaming:
    def __init__(self, points: List[Point], tolerance: float):
        """
        基于曲率的轨迹压缩算法
        :param points: 轨迹点
        :param tolerance: 最小曲率阈值
        """
        self.points = points
        self.tolerance = tolerance

    @staticmethod
    def calc_curvature(p1: Point, p2: Point, p3: Point) -> float:
        """
        计算三点所构建圆的曲率
        """
        x1, x2, x3, y1, y2, y3 = p1.x, p2.x, p3.x, p1.y, p2.y, p3.y
        a, b, c, d = x1 - x2, y1 - y2, x1 - x3, y1 - y3
        e = ((x1 * x1 - x2 * x2) + (y1 * y1 - y2 * y2)) / 2.0
        f = ((x1 * x1 - x3 * x3) + (y1 * y1 - y3 * y3)) / 2.0
        det = b * c - a * d
        if abs(det) < 1e-5:
            # 若三点共线则半径无穷大且曲率为0
            return 0
        x0 = -(d * e - b * f) / det
        y0 = -(a * f - c * e) / det
        radius = sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2))
        # return radius
        return 1 / radius

    def compress(self):
        if self.points is None or len(self.points) < 3:
            return self.points
        compressed = []
        n = len(self.points)
        compressed.append(self.points[0])
        for i in range(1, n - 1):
            curvature = self.calc_curvature(self.points[i - 1], self.points[i], self.points[i + 1])
            # print(i, curvature, 1 / (curvature + 1e-5))
            if curvature > self.tolerance:
                compressed.append(self.points[i])
        compressed.append(self.points[n - 1])
        return compressed


if __name__ == '__main__':
    data = []
    with open("./data/1.txt", "r") as fr:
        for line in fr.readlines():
            temp = line.split(",")
            data.append(Point(temp[0], float(temp[1]), float(temp[2])))
    curv = CurvatureStreaming(data, 0.3)
    res = curv.compress()
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
