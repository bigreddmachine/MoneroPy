import unittest
from testdata import valid_sks, hashed_valid_sks, reduced_hashed_valid_sks, public_from_valid_sks
from context import moneropy

cn = moneropy.cryptonote

class TestCryptonote(unittest.TestCase):

    def test_cn_fast_hash(self):
        def T(sk, hashed_sk):
            self.assertEqual(cn.cn_fast_hash(sk), hashed_sk)

        for i in range(len(valid_sks)):
            T(valid_sks[i], hashed_valid_sks[i])

    def test_sc_reduce(self):
        def T(hashed_sk, red_hashed_sk):
            self.assertEqual(cn.sc_reduce(hashed_sk), red_hashed_sk)

        for i in range(len(hashed_valid_sks)):
            T(hashed_valid_sks[i], reduced_hashed_valid_sks[i])


    def test_public_from_secret(self):
        def T(sk, public):
            self.assertEqual(cn.public_from_secret(sk), public)

        for i in range(len(valid_sks)):
            T(valid_sks[i], public_from_valid_sks[i])



if __name__ == '__main__':
    unittest.main()
