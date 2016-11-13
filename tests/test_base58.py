import unittest
from testdata import valid_addrs, decoded_addrs
from context import moneropy

b58 = moneropy.base58

class TestBase58(unittest.TestCase):

    def test_encode(self):
        def T(dec_addr, addr):
            self.assertEqual(b58.encode(dec_addr), addr)

        for i in range(len(valid_addrs)):
            T(decoded_addrs[i], valid_addrs[i])

    def test_decode(self):
        def T(addr, dec_addr):
            self.assertEqual(b58.decode(addr), dec_addr)

        for i in range(len(valid_addrs)):
            T(valid_addrs[i], decoded_addrs[i])


if __name__ == '__main__':
    unittest.main()
