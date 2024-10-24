import unittest

import mygrep

CASES = [
    ("Bus Meow meo meow meow mmmeowmeowww Bus Bus Bus Meo meow", "meow", [(13, 17), (18, 22), (25, 29), (29, 33), (52, 56)]),
    ("meow    meow", "meo", [(0, 3), (8, 11)]),
    ("m meo meow meow Bus Bus meow Bus Meo Meow m", "meow", [(6, 10), (11, 15), (24, 28)]),
    ("meow", "meow", [(0, 4)]),
    ("meo meow meow Bus Bus meow Bus Meo Meow m", "meow", [(4, 8), (9, 13), (22, 26)]),
    ("meow", "m", [(0, 1)]),
    ("mmmmmm", "m", [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]),
    ("", "meow", []),#grep doesn't return anything 
    ("m", "meow", []),#grep doesn't return anything
    ("", "", [(0, -1)]),#grep returns an empty string
    ("01929838(())(&^%$", "0", [(0, 1)]),
    ("m", "m", [(0, 0)])
    ("meow", "", [(0, -1)]) #grep returns the whole string fron the file
]


class TestIndices(unittest.TestCase):
    def test_func(self):
        for line, pattern, expected_result in CASES:
            with self.subTest(line=line, pattern=pattern):
                self.assertEqual(mygrep.find_pattern_indices(line, pattern), expected_result)


if __name__ == '__main__':
    unittest.main()
