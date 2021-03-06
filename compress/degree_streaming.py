import math
from math import sqrt, acos
from typing import List

from common.point import Point


class DegreeStreaming:
    def __init__(self, points: List[Point], tolerance: float):
        """
        基于角度的轨迹压缩算法
        :param points: 轨迹点
        :param tolerance: 最大角度阈值
        """
        self.points = points
        self.tolerance = tolerance

    @staticmethod
    def calc_degree(p1: Point, p2: Point, p3: Point) -> float:
        """
        计算三点所构建圆的曲率
        """
        x1, x2, x3, y1, y2, y3 = p1.x, p2.x, p3.x, p1.y, p2.y, p3.y
        a = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2))
        b = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        c = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2))
        if 2 * a * b < 1e-10:
            return 180
        else:
            cos_theta = (a * a + b * b - c * c) / (2 * a * b)
            return acos(cos_theta) * 180 / math.pi

    def compress(self):
        if self.points is None or len(self.points) < 3:
            return self.points
        compressed = []
        n = len(self.points)
        compressed.append(self.points[0])
        for i in range(1, n - 1):
            degree = self.calc_degree(self.points[i - 1], self.points[i], self.points[i + 1])
            # print(i, degree, self.tolerance)
            if degree < self.tolerance:
                compressed.append(self.points[i])
        compressed.append(self.points[n - 1])
        return compressed
