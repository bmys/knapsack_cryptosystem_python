import unittest

import Knapsack as ks


class KnapsackTest(unittest.TestCase):

    def test_public_key_generator(self):
        priv_key = [1, 2, 4, 10, 20, 40]
        pub_key = ks.create_public_key(priv_key, 53, 120)

        self.assertEqual(pub_key, [53, 106, 92, 50, 100, 80])

    def test_encode_msg_with_pub_k(self):
        priv_key = [1, 2, 4, 10, 20, 40]
        pub_key = ks.create_public_key(priv_key, 53, 120)
        msg = [int(i) for i in '111010']
        cipher = ks.to_cipher(msg, pub_key)
        self.assertEqual(cipher, 351)

    def test_decode_cipher(self):
        cipher = 351
        n = ks.inverse_mod(53, 120)
        plain = ks.to_plain(cipher, n, 120)
        self.assertEqual(plain, 27)

    def test_decode_encode(self):

        msg = [int(i) for i in '111010']
        priv_key = [1, 2, 4, 10, 20, 40]
        pub_key = ks.create_public_key(priv_key, 53, 120)

        cipher = ks.to_cipher(msg, pub_key)

        n = ks.inverse_mod(53, 120)
        decoded = ks.to_plain(cipher, n, 120)
        decoded = ks.encode(priv_key, decoded)

        self.assertEqual(decoded, msg)



