"""Week2 Test Cases Max Spacing for K-order Cluster Hamming Distance"""

from src.course3.week2.hamming import calculate_hamming_clusters


def test_hamming():
    number_strings = ['1 1 1 0 0 1 1 0 1 1 0 1 0 0 1 1 1 1 0 0 1 1 1 1',
                      '1 1 1 0 0 1 1 0 0 1 0 1 0 0 1 1 1 1 0 0 1 1 1 1',
                      '0 1 1 1 0 0 0 0 0 0 0 1 0 0 1 0 1 1 1 0 0 1 0 1',
                      '0 1 1 1 0 0 0 0 0 0 0 1 0 0 1 0 1 0 1 0 0 1 0 1',
                      '0 1 0 0 1 1 1 0 1 0 1 1 0 0 1 1 1 1 1 0 0 1 0 0',
                      '0 1 0 0 1 0 1 0 1 0 1 1 0 0 1 1 1 1 1 0 0 1 0 0']

    numbers = []
    for n in number_strings:
        numbers.append(int(n.replace(' ', ''), base=2))

    assert calculate_hamming_clusters(numbers) == 3
