class UnionFind:
    """An implementation of union find data structure.
    It uses union by rank with path compression.
    """

    def __init__(self, count):
        self._elements = list(range(count))
        self._count = count
        self._rank = [0] * count

    def __len__(self):
        return self._count

    def find(self, key):
        indices = self._elements
        while key != indices[key]:
            parent_key = indices[key]
            # path compression
            indices[key] = indices[parent_key]
            key = indices[key]

        return key

    def union(self, key1, key2):
        indices = self._elements
        rank = self._rank

        key1_root = self.find(key1)
        key2_root = self.find(key2)

        if key1_root == key2_root:
            return

        self._count -= 1
        if rank[key1_root] < rank[key2_root]:
            indices[key1_root] = key2_root
        elif rank[key1_root] > rank[key2_root]:
            indices[key2_root] = key1_root
        else:
            indices[key2_root] = key1_root
            rank[key1_root] += 1
