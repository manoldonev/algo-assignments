
import sys
import math


def traveling_salesman_problem(points):
    source = points[0]
    # make sure points are sorted by x coordinate (assignment data already sorted)
    points.sort()

    source_index_after_sort = points.index(source)
    explored = set([source_index_after_sort])
    n = len(points) - 1
    total_distance = 0
    index = source_index_after_sort
    while n > 0:
        nearest_neighbor_index, nearest_distance = _find_nearest_neighbor_index(
            index, points, explored)

        explored.add(nearest_neighbor_index)
        total_distance += nearest_distance
        index = nearest_neighbor_index
        n -= 1
    else:
        total_distance += _calculate_euclidean_distance(
            points[nearest_neighbor_index], points[source_index_after_sort])

    return total_distance


def _find_nearest_neighbor_index(source_index, points, explored):
    n = len(points)
    source = points[source_index]
    min_distance = sys.maxsize
    min_distance_index = -1

    index = source_index - 1
    while True:
        if index < 0:
            break

        if index not in explored:
            point = points[index]
            distance = _calculate_euclidean_distance(source, point)
            if min_distance > distance:
                min_distance = distance
                min_distance_index = index
            # choose lower original index to break ties
            elif min_distance == distance and points[index][2] < points[min_distance_index][2]:
                min_distance_index = index

            # x coordinates are guaranteed to be sorted
            if min_distance < abs(source[0] - point[0]):
                break

        index -= 1

    index = source_index + 1
    while True:
        if index == n:
            break

        if index not in explored:
            point = points[index]
            distance = _calculate_euclidean_distance(source, point)
            if min_distance > distance:
                min_distance = distance
                min_distance_index = index
            # choose lower original index to break ties
            elif min_distance == distance and points[index][2] < points[min_distance_index][2]:
                min_distance_index = index

            # x coordinates are guaranteed to be sorted
            if min_distance <= abs(source[0] - point[0]):
                break

        index += 1

    return min_distance_index, min_distance


def _calculate_euclidean_distance(point1, point2):
    x1, y1, _ = point1
    x2, y2, _ = point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
