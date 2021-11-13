import matplotlib.pyplot as plt

from common.point import Point
from common.st_point import STPoint
from compress.degree_streaming import DegreeStreaming
from compress.douglas_peucker import DouglasPeucker
from compress.st_curvature_streaming import STCurvatureStreaming

if __name__ == '__main__':
    data = []
    with open("data/traj.txt", "r") as fr:
        for line in fr.readlines():
            temp = line.split(",")
            data.append(Point(temp[0], float(temp[1]), float(temp[2])))
    # plot raw traj
    raw_x = [p.x for p in data]
    raw_y = [p.y for p in data]
    plt.subplot(2, 2, 1)
    plt.plot(raw_x, raw_y, marker='o')
    plt.title("Raw Traj")

    # plot douglas peucker
    dp = DouglasPeucker(data, 5e-4)
    res1 = dp.compress()
    compressed_date1 = len(data) / len(res1)
    print("compress rate for douglas peucker: %.2f" % compressed_date1)
    compressed_x1 = [p.x for p in res1]
    compressed_y1 = [p.y for p in res1]
    plt.subplot(2, 2, 2)
    plt.plot(compressed_x1, compressed_y1, marker='o')
    plt.title("Douglas Peucker Compress Rate: %.2f" % compressed_date1)

    # plot degree streaming
    degree = DegreeStreaming(data, 140)
    res2 = degree.compress()
    compressed_date2 = len(data) / len(res2)
    print("compress rate for degree streaming: %.2f" % compressed_date2)
    compressed_x2 = [p.x for p in res2]
    compressed_y2 = [p.y for p in res2]
    plt.subplot(2, 2, 3)
    plt.plot(compressed_x2, compressed_y2, marker='o')
    plt.title("Degree Streaming Compress Rate: %.2f" % compressed_date2)

    # plot st curvature streaming
    st_data = []
    with open("data/traj.txt", "r") as fr:
        for line in fr.readlines():
            temp = line.split(",")
            st_data.append(STPoint(temp[0], float(temp[1]), float(temp[2]), int(temp[3])))
    curv = STCurvatureStreaming(st_data, 0.15)
    res3 = curv.compress()
    compressed_date3 = len(st_data) / len(res3)
    print("compress rate for st curvature streaming: %.2f" % compressed_date3)
    compressed_x3 = [p.x for p in res3]
    compressed_y3 = [p.y for p in res3]
    plt.subplot(2, 2, 4)
    plt.plot(compressed_x3, compressed_y3, marker='o')
    plt.title("ST Curvature Streaming Compress Rate: %.2f" % compressed_date3)

    plt.show()
    print("ok")
