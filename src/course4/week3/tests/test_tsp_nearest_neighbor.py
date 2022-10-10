import math

from src.course4.week3.tsp_nearest_neighbor import traveling_salesman_problem


def test_tsp_50_cities():
    points = []
    with open("src/course4/week3_nn.txt") as handle:
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
    points = []
    with open("src/course4/week3_nn.txt") as handle:
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
    points = []
    with open("src/course4/week3_nn_unsorted.txt") as handle:
        handle.readline()
        for line in handle:
            index, x, y = line.split()
            points.append((float(x), float(y), int(index)))

    distance = traveling_salesman_problem(points)
    assert math.floor(distance) == 29777
