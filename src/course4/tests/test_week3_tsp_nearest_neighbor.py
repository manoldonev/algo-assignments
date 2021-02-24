
import math
import os

from week3.tsp_nearest_neighbor import traveling_salesman_problem


def test_tsp_50_cities():
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    path = os.path.join(__location__, "week3_nn.txt")

    points = []
    with open(path) as handle:
        handle.readline()
        n = 0
        for line in handle:
            index, x, y = line.split()
            points.append((float(x), float(y), int(index)))
            n += 1
            if n == 50:
                break

    distance = traveling_salesman_problem(points)
    assert math.floor(distance) == 2470


def test_tsp_1000_cities():
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    path = os.path.join(__location__, "week3_nn.txt")

    points = []
    with open(path) as handle:
        handle.readline()
        n = 0
        for line in handle:
            index, x, y = line.split()
            points.append((float(x), float(y), int(index)))
            n += 1
            if n == 1000:
                break

    distance = traveling_salesman_problem(points)
    assert math.floor(distance) == 48581


def test_tsp_1000_cities_unsorted():
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    path = os.path.join(__location__, "week3_nn_unsorted.txt")

    points = []
    with open(path) as handle:
        handle.readline()
        for line in handle:
            index, x, y = line.split()
            points.append((float(x), float(y), int(index)))

    distance = traveling_salesman_problem(points)
    assert math.floor(distance) == 29777
