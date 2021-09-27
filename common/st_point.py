class STPoint:
    def __init__(self, pid: str, x: float, y: float, t: int):
        """
        轨迹点模型
        :param pid: 标识
        :param x: 经度
        :param y: 纬度
        :param t: 时间
        """
        self.pid = pid
        self.x = x
        self.y = y
        self.t = t
