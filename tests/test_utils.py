import unittest
from testdata import hexes, ints
from context import moneropy

utils = moneropy.utils

class TestUtils(unittest.TestCase):

    def test_hexStrToInt(self):
        def T(h, i):
            self.assertEqual(utils.hexStrToInt(h), i)

        for i in range(len(hexes)):
            T(hexes[i], ints[i])

    def test_intToHexStr(self):
        def T(i, h):
            self.assertEqual(utils.intToHexStr(i), h)

        for i in range(len(ints)):
            T(ints[i], hexes[i])


if __name__ == '__main__':
    unittest.main()
