
"""Week1 Test Cases: Strongly Connected Components"""

from src.course2.week1.scc import scc


def test_scc():
    graph = {
        'a': ['c'],
        'b': ['a'],
        'c': ['b'],
        'd': ['b', 'f'],
        'e': ['d'],
        'f': ['e'],
        'g': ['e', 'h'],
        'h': ['i'],
        'i': ['g']
    }

    assert scc(graph) == {'c': ['c', 'b', 'a'], 'd': [
        'd', 'f', 'e'], 'g': ['g', 'h', 'i']}


def test_scc_reversed_graph():
    graph = {
        'a': ['b'],
        'b': ['c', 'd'],
        'c': ['a'],
        'd': ['e'],
        'e': ['f', 'g'],
        'f': ['d'],
        'g': ['i'],
        'h': ['g'],
        'i': ['h']
    }

    assert scc(graph) == {'g': ['g', 'i', 'h'], 'd': [
        'd', 'e', 'f'], 'b': ['b', 'c', 'a']}


def test_scc_node_no_outbound_edges():
    graph = {
        'a': ['b'],
        'b': ['c', 'd'],
        'c': ['a'],
        'd': ['e'],
        'e': ['f', 'g'],
        'f': ['d'],
        'g': ['i'],
        'h': ['g'],
        'i': []
    }

    assert scc(graph) == {'i': ['i'], 'g': ['g'], 'h': [
        'h'], 'd': ['d', 'e', 'f'], 'b': ['b', 'c', 'a']}


def test_scc_no_edges():
    graph = {
        'a': [],
        'b': [],
        'c': []
    }

    assert scc(graph) == {'a': ['a'], 'c': ['c'], 'b': ['b']}


def test_scc_single_node():
    graph = {
        'a': []
    }

    assert scc(graph) == {'a': ['a']}


def test_scc_single_edge():
    graph = {
        'a': ['b'],
        'b': []
    }

    assert scc(graph) == {'a': ['a'], 'b': ['b']}
