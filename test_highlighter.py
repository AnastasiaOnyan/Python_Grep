import unittest
 
import mygrep

CASES = [
    ([(13, 17), (18, 22), (25, 29), (29, 33), (52, 56)], "Bus Meow meo meow meow mmmeowmeowww Bus Bus Bus Meo meow", "Bus Meow meo \033[01;31m\033[Kmeow\033[m\033[K \033[01;31m\033[Kmeow\033[m\033[K mm\033[01;31m\033[Kmeow\033[m\033[K\033[01;31m\033[Kmeow\033[m\033[Kww Bus Bus Bus Meo \033[01;31m\033[Kmeow\033[m\033[K"),
    ([(0, 3), (8, 11)], "meow    meow", "\033[01;31m\033[Kmeo\033[m\033[Kw    \033[01;31m\033[Kmeo\033[m\033[Kw"),
    ([(6, 10), (11, 15), (24, 28)], "m meo meow meow Bus Bus meow Bus Meo Meow m", "m meo \033[01;31m\033[Kmeow\033[m\033[K \033[01;31m\033[Kmeow\033[m\033[K Bus Bus \033[01;31m\033[Kmeow\033[m\033[K Bus Meo Meow m"),
    ([(0, 4)], "meow", "\033[01;31m\033[Kmeow\033[m\033[K"),
    ([(0, 1)], "meow", "\033[01;31m\033[Km\033[m\033[Keow"),
    ([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)], "mmmmmm", "\033[01;31m\033[Km\033[m\033[K\033[01;31m\033[Km\033[m\033[K\033[01;31m\033[Km\033[m\033[K\033[01;31m\033[Km\033[m\033[K\033[01;31m\033[Km\033[m\033[K\033[01;31m\033[Km\033[m\033[K"),
    ([], "", ""), 
    ([(0, 0)], "m", "\033[01;31m\033[Km\033[m\033[K"),
    ([(0, -1)], "", ""),
    ([(0, 1)], "01929838(())(&^%$", "\033[01;31m\033[K0\033[m\033[K1929838(())(&^%$"),
    ([(0, -1)], "meow", "meow")
    ]

class TestHighlighter(unittest.TestCase):
    def test_func(self):
        for indices, line, expected_result in CASES:
            with self.subTest(indices=indices, line=line):
                self.assertEqual(mygrep.highlighter_func(indices, line), expected_result)
                
if __name__ == '__main__':
    unittest.main()
    



