
import itertools


def calculate_maximum_weight_independent_set(graph_list):
    max_weights = [0, max(0, graph_list[0])]

    index = 2
    for vertex_weight in itertools.islice(graph_list, 1, None):
        max_weights.append(max(max_weights[index - 1],
                               max_weights[index - 2] + vertex_weight))
        index += 1

    return max_weights


def reconstruct_weight_independent_set(graph_list, max_weights):
    result = {}

    index = len(graph_list)
    while index >= 2:
        vertex_weight = graph_list[index - 1]
        if max_weights[index - 1] >= max_weights[index - 2] + vertex_weight:
            index -= 1
        else:
            result[index - 1] = vertex_weight
            index -= 2

    if index == 1:
        vertex_weight = graph_list[0]
        result[index - 1] = vertex_weight

    return result
