class Point:
    def __init__(self, pid: str, x: float, y: float):
        """
        轨迹点模型
        :param pid: 轨迹标识
        :param x: 经度
        :param y: 纬度
        """
        self.pid = pid
        self.x = x
        self.y = y