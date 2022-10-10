"""Week3 Test Cases Huffman Encoding"""

from src.course3.week3.huffman import (
    make_huffman_tree,
    get_encoding,
    get_max_length,
    get_min_length,
)


def test_huffman():
    huffman_tree = make_huffman_tree(
        {"a": 0.04, "b": 0.3, "c": 0.2, "d": 0.4, "e": 0.06}
    )

    huffman_encoding = get_encoding(huffman_tree)

    assert huffman_encoding == {
        "a": "1100",
        "b": "10",
        "c": "111",
        "d": "0",
        "e": "1101",
    }

    assert get_min_length(huffman_encoding) == 1

    assert get_max_length(huffman_encoding) == 4
