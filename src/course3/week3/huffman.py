import sys

from heapq import heapify, heappop, heappush


def make_huffman_tree(symbols):
    node_list = [HuffmanNode(weight, symbol) for symbol, weight in symbols.items()]
    heapify(node_list)

    n = len(symbols)
    while n > 1:
        smallest_node = heappop(node_list)
        second_smallest_node = heappop(node_list)

        heappush(
            node_list,
            HuffmanNode(
                weight=smallest_node.weight + second_smallest_node.weight,
                zero=smallest_node,
                one=second_smallest_node,
            ),
        )

        n -= 1

    return node_list[0]


def get_encoding(tree):
    return _flatten_to_dict(tree)


def get_max_length(encoding):
    max_length = 0
    for codeword in encoding.values():
        max_length = max(max_length, len(codeword))

    return max_length


def get_min_length(encoding):
    min_length = sys.maxsize
    for codeword in encoding.values():
        min_length = min(min_length, len(codeword))

    return min_length


def _flatten_to_dict(tree, codeword="", code_dict=None):
    if code_dict is None:
        code_dict = {}

    if tree.symbol:
        if codeword == "":
            codeword = "0"

        code_dict[tree.symbol] = codeword
    else:
        _flatten_to_dict(tree.zero, codeword + "0", code_dict)
        _flatten_to_dict(tree.one, codeword + "1", code_dict)

    return code_dict


class HuffmanNode:
    def __init__(self, weight, symbol=None, zero=None, one=None):
        self.weight = weight
        self.symbol = symbol
        self.zero = zero
        self.one = one

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f"{self.symbol}: {self.weight}"


# class HuffmanCompression:
#     def __init__(self, symbol_weights):
#         self.weights = symbol_weights
#         self._encoding = None
#         self._build()

#     def _build(self):
#         node_list = [HuffmanNode(weight, symbol)
#                      for symbol, weight in self.weights.items()]
#         heapify(node_list)

#         n = len(self.weights)
#         while(n > 1):
#             smallest_node = heappop(node_list)
#             second_smallest_node = heappop(node_list)

#             heappush(node_list,
#                      HuffmanNode(weight=smallest_node.weight + second_smallest_node.weight,
#                                  zero=smallest_node,
#                                  one=second_smallest_node))

#             n -= 1

#         self._tree = node_list[0]
#         self._encoding = _flatten_to_dict(self._tree)

#     def get_encoding(self):
#         return self._encoding

#     def encode(self, text):
#         pass

#     def decode(self, binary_text):
#         pass
