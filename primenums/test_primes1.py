#!/usr/bin/env python3

import unittest

from primenums import Convergence


class TestMain(unittest.TestCase):

    # def tearDown(self):
    #     self.p.clear()

    def setUp(self):
        self.p = Convergence()
        self.p.clear()  # чтобы не мешал Синглтон

    def test_create_def(self):
        self.assertEqual([2, ],
                         self.p.primes,
                         "Check default cache")

    def test_create_31(self):
        self.p.clear()
        p1 = Convergence(31)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,],
                         p1.primes,
                         "Check fill cache out to 31")

    def test_create_30(self):
        self.p.clear()
        p1 = Convergence(30)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29,],
                         p1.primes,
                         "Check fill cache out to 31")

    def test_isprime_3(self):
        self.assertTrue(self.p.is_prime(3), "Check result for 3")
        self.assertEqual([2, 3, ],
                         self.p.primes,
                         "Check list for 3")

    def test_isprime_4(self):
        self.p.is_prime(4)
        self.assertEqual([2, 3, ],
                         self.p.primes,
                         "Check list for 4")
        self.assertFalse(self.p.is_prime(4), "Check result for ")

    def test_isprime_5(self):
        self.p.is_prime(5)
        self.assertEqual([2, 3, 5, ],
                         self.p.primes,
                         "Check list for 5")
        self.assertTrue(self.p.is_prime(5), "Check result for 5")

    def test_isprime_6(self):
        self.p.is_prime(6)
        self.assertEqual([2, 3, 5, ],
                         self.p.primes,
                         "Check list for 6")
        self.assertFalse(self.p.is_prime(6), "Check result for 6")

    def test_isprime_11(self):
        n = 11
        self.assertTrue(self.p.is_prime(n), "Check result for {}".format(n))
        self.assertEqual([2, 3, 5, 7, 11,],
                         self.p.primes,
                         "Check list for {}".format(n))

    # def test_singleton(self):
    #     self.p.clear()
    #     p1 = Convergence(11)
    #     # TODO: проверить атрибут
    #     p2 = Convergence(5)
    #     # TODO: убедиться, что кеш уже заполен до 11 включительно