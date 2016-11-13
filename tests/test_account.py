import unittest
from testdata import valid_seeds, valid_sks, valid_vks, valid_addrs, addr_vers, valid_addr_pubsks, valid_addr_pubvks
from context import moneropy

acc = moneropy.account

class TestAccount(unittest.TestCase):

    def test_get_view_key(self):
        def T(sk, vk):
            self.assertEqual(acc.get_view_key(sk), vk)

        for i in range(len(valid_sks)):
            T(valid_sks[i], valid_vks[i])

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

    def test_decode_addr(self):
        def T(addr, vers, pubsk, pubvk):
            vers_, pubsk_, pubvk_ = acc.decode_addr(addr)
            self.assertEqual(vers_, vers)
            self.assertEqual(pubsk_, pubsk)
            self.assertEqual(pubvk_, pubvk)

        for i in range(len(valid_addrs)):
            T(valid_addrs[i], addr_vers, valid_addr_pubsks[i], valid_addr_pubvks[i])

    def test_encode_addr(self):
        def T(vers, pubsk, pubvk, addr):
            self.assertEqual(acc.encode_addr(vers, pubsk, pubvk), addr)

        for i in range(len(valid_addr_pubsks)):
            T(addr_vers, valid_addr_pubsks[i], valid_addr_pubvks[i], valid_addrs[i])

    def test_check_address_viewkey(self):
        def T(addr, privViewKey):
            self.assertTrue(acc.check_address_viewkey(addr, privViewKey))

        def T2(addr, privViewKey):
            self.assertFalse(acc.check_address_viewkey(addr, privViewKey))

        # Test valid view keys
        for i in range(len(valid_addrs)):
            T(valid_addrs[i], valid_vks[i])

        # Test invalid view keys (using mis-matched vk/addr pair)
        for i in range(len(valid_addrs)):
            j = (i+1) % len(valid_addrs)
            T2(valid_addrs[i], valid_vks[j])

if __name__ == '__main__':
    unittest.main()
