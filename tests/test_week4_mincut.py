"""Week4 Test Cases: Karger's Min Cut"""

import math
from week4.mincut import min_cut


def test_mincut():
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 4],
        4: [1, 2, 3, 5],
        5: [2, 4]
    }

    n = len(graph)
    trials = math.ceil(n * n * math.log(n))

    result = n
    while trials > 0:
        cut = min_cut(graph)
        min_cut_candidate = len(cut[cut.keys()[0]])

        print min_cut_candidate

        if min_cut_candidate < result:
            result = min_cut_candidate

        trials -= 1

    assert result == 2
