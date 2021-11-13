from math import sqrt
from typing import List

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
            # print(distance, max_distance)
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
