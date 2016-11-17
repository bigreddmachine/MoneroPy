import unittest
from testdata import hexes, ints, extra_hex, extra_bin, extra_pub, extra_payid
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

    def test_parse_extra_hex(self):
        def T(h, pub, pid):
            pub_, pid_ = utils.parse_extra_hex(h)
            self.assertEqual(pub_, pub)
            self.assertEqual(pid_, pid)

        for i in range(len(extra_hex)):
            T(extra_hex[i], extra_pub[i], extra_payid[i])

    def test_parse_extra_bin(self):
        def T(b, pub, pid):
            pub_, pid_ = utils.parse_extra_bin(b)
            self.assertEqual(pub_, pub)
            self.assertEqual(pid_, pid)

        for i in range(len(extra_bin)):
            T(extra_bin[i], extra_pub[i], extra_payid[i])


if __name__ == '__main__':
    unittest.main()
