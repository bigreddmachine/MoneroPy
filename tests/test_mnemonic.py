import unittest
from testdata import valid_seeds, valid_sks, invalid_seeds
from context import moneropy

mn = moneropy.mnemonic

class TestMnemonic(unittest.TestCase):

    def test_checksum_valid(self):
        def T(seed):
            self.assertTrue(mn.mn_validate_checksum(seed))

        for i in range(len(valid_seeds)):
            # Input 13 or 25 word seed.
            # Checks that last word matches checksum calculation
            T(valid_seeds[i])

    def test_checksum_invalid(self):
        def T(seed):
            self.assertFalse(mn.mn_validate_checksum(seed))

        for i in range(len(invalid_seeds)):
            T(invalid_seeds[i])

    def test_checksum(self):
        def T(seed, checksum):
            self.assertEqual(mn.mn_checksum(seed), checksum)

        for i in range(len(valid_seeds)):
            # Checksum is the last word in seed.
            T(valid_seeds[i], valid_seeds[i][-1])

            # Can also input seed with or without checksum.
            T(valid_seeds[i][:24], valid_seeds[i][-1])

    def test_mn_decode(self):
        def T(seed, sk):
            self.assertEqual(mn.mn_decode(seed), sk)

        for i in range(len(valid_seeds)):
            T(valid_seeds[i], valid_sks[i])

    def test_mn_encode(self):
        def T(sk, seed):
            self.assertEqual(mn.mn_encode(sk), seed)

        for i in range(len(valid_sks)):
            T(valid_sks[i], valid_seeds[i][:24])


if __name__ == '__main__':
    unittest.main()
