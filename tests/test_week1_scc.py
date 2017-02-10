
"""Week1 Test Cases: Strongly Connected Components"""

from week1.scc import scc


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

    assert scc(graph) == {'a': ['a', 'c', 'b'], 'd': [
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

    assert scc(graph) == {'a': ['a', 'b', 'c'], 'e': [
        'e', 'f', 'd'], 'g': ['g', 'i', 'h']}


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

    assert scc(graph) == {'i': ['i'], 'h': ['h'], 'e': [
        'e', 'f', 'd'], 'a': ['a', 'b', 'c'], 'g': ['g']}


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
