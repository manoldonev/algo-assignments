
from src.course4.week4.two_sat import papadimitriou, reduce_clauses


def test_2sat_3clauses():
    clauses = [(1, -2), (-1, -2), (2, -3)]
    assert papadimitriou(clauses)


def test_2sat_3clauses_with_reduce():
    clauses = [(1, -2), (-1, -2), (2, -3)]
    reduced_clauses = reduce_clauses(clauses)
    assert len(reduced_clauses) == 0
    assert papadimitriou(reduced_clauses)


def test_2sat_4clauses():
    clauses = [(1, 2), (-1, 3), (3, 4), (-2, -4)]
    assert papadimitriou(clauses)


def test_2sat_4clauses_with_reduce():
    clauses = [(1, 2), (-1, 3), (3, 4), (-2, -4)]
    reduced_clauses = reduce_clauses(clauses)
    assert len(reduced_clauses) == 0
    assert papadimitriou(reduced_clauses)


def test_2sat_4clauses_unsatisfiable():
    clauses = [(1, -2), (-1, 2), (-2, 4), (-2, -4), (2, 4), (2, -4)]
    assert not papadimitriou(clauses)


def test_2sat_4clauses_with_reduce_unsatisfiable():
    clauses = [(1, -2), (-1, 2), (-2, 4), (-2, -4), (2, 4), (2, -4)]
    reduced_clauses = reduce_clauses(clauses)
    assert len(reduced_clauses) == 6
    assert not papadimitriou(reduced_clauses)


def test_2sat_400_clauses():
    clauses = []
    with open("src/course4/week4_2sat_400.txt") as handle:
        handle.readline()
        for line in handle:
            x, y = line.split()
            clauses.append((int(x), int(y)))

    assert papadimitriou(clauses)

    reduced_clauses = reduce_clauses(clauses)
    assert len(reduced_clauses) == 5
    assert papadimitriou(reduced_clauses)


def test_2sat_800_clauses():
    clauses = []
    with open("src/course4/week4_2sat_800.txt") as handle:
        handle.readline()
        for line in handle:
            x, y = line.split()
            clauses.append((int(x), int(y)))

    reduced_clauses = reduce_clauses(clauses)
    assert papadimitriou(reduced_clauses)


def test_2sat_800_clauses_unsatisfiable():
    clauses = []
    with open("src/course4/week4_2sat_800_2.txt") as handle:
        handle.readline()
        for line in handle:
            x, y = line.split()
            clauses.append((int(x), int(y)))

    reduced_clauses = reduce_clauses(clauses)
    assert not papadimitriou(reduced_clauses)
