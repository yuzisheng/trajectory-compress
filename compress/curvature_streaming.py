from math import sqrt
from typing import List

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
        if abs(det) < 1e-10:
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
            # print(i, curvature, 1 / (curvature + 1e-10))
            if curvature > self.tolerance:
                compressed.append(self.points[i])
        compressed.append(self.points[n - 1])
        return compressed
