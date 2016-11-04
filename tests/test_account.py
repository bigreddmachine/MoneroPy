import unittest
from testdata import valid_seeds, valid_sks, valid_vks, valid_addrs
from context import moneropy

acc = moneropy.account

class TestAccount(unittest.TestCase):

    def test_account_from_seed(self):
        def T(seed, sk, vk, addr):
            sk_t, vk_t, addr_t = acc.account_from_seed(seed)
            self.assertEqual(sk_t, sk)
            self.assertEqual(vk_t, vk)
            self.assertEqual(addr_t, addr)

        for i in range(len(valid_seeds)):
            T(valid_seeds[i], valid_sks[i], valid_vks[i], valid_addrs[i])

    def test_account_from_spend_key(self):
        def T(sk, vk, addr):
            sk_t, vk_t, addr_t = acc.account_from_spend_key(sk)
            self.assertEqual(sk_t, sk)
            self.assertEqual(vk_t, vk)
            self.assertEqual(addr_t, addr)

        for i in range(len(valid_sks)):
            T(valid_sks[i], valid_vks[i], valid_addrs[i])


if __name__ == '__main__':
    unittest.main()
