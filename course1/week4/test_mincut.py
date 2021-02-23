"""Week4 Test Cases: Karger's Min Cut"""

import math
import unittest

from course1.week4.mincut import min_cut


class MinCutTests(unittest.TestCase):
    """Test cases for min cut."""

    def test_mincut(self):
        graph = {
            1: [2, 3, 4],
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
            min_cut_candidate = len(cut[list(cut.keys())[0]])

            if min_cut_candidate < result:
                result = min_cut_candidate

            trials -= 1

        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
