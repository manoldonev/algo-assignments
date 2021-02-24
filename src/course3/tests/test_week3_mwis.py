"""Week3 Test Cases Maximum-Weight Independent Set"""

from week3.mwis import calculate_maximum_weight_independent_set, reconstruct_weight_independent_set


def test_mwis():
    graph_list = [7, 1, 2, 5, 8, 9, 7]
    max_weights = calculate_maximum_weight_independent_set(graph_list)

    assert max_weights == [0, 7, 7, 9, 12, 17, 21, 24]

    max_weight_independent_set = reconstruct_weight_independent_set(
        graph_list, max_weights)

    assert max_weight_independent_set == {0: 7, 2: 2, 4: 8, 6: 7}
