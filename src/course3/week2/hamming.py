import itertools
from collections import defaultdict
from networkx.utils import UnionFind


def calculate_hamming_clusters(numbers):
    numbers_map = defaultdict(list)
    for index, node in enumerate(numbers):
        numbers_map[node].append(index)

    # no duplicates in the union find
    union_find = UnionFind(numbers_map)

    hamming_distance_one = [1 << i for i in range(24)]
    hamming_distance_two = [1 << i ^ 1 << j for i,
                            j in itertools.combinations(range(24), 2)]

    hamming_distances = [*hamming_distance_one, *hamming_distance_two]

    keys = list(numbers_map)
    for distance_mask in hamming_distances:
        for key in keys:
            key2 = key ^ distance_mask
            if numbers_map[key2]:
                union_find.union(key, key2)

    return len(list(union_find.to_sets()))
