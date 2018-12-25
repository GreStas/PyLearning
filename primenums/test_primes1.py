#!/usr/bin/env python3

import unittest

from primenums import Convergence, Primes


class TestConvergence(unittest.TestCase):

    # def tearDown(self):
    #     del self.p

    def setUp(self):
        self.p = Convergence()
        self.p.clear()  # чтобы не мешал Синглтон

    def test_append(self):
        self.assertEqual(3, self.p.append())
        self.assertEqual(5, self.p.append())
        self.assertEqual(7, self.p.append())
        self.assertEqual(11, self.p.append())

    def test_create_def(self):
        self.assertEqual([2, ],
                         self.p.primes,
                         "Check default cache")

    def test_singleton(self):
        p1 = Convergence(100)
        p2 = Convergence(10)
        self.assertEqual(p1.primes, p2.primes, "Check create come instances with diferent init parameter")

    def test_create_for31(self):
        self.p.clear()
        p1 = Convergence(31)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,],
                         p1.primes,
                         "Check fill cache out to 31")

    def test_create_for30(self):
        self.p.clear()
        p1 = Convergence(30)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,],
                         p1.primes,
                         "Check fill cache out to 31")

    def test_isprime_for1(self):
        self.assertTrue(self.p.is_prime(1), "Check result for 1")
        self.assertEqual([2, ],
                         self.p.primes,
                         "Check list for 1")

    def test_isprime_for3(self):
        self.assertTrue(self.p.is_prime(3), "Check result for 3")
        self.assertEqual([2, 3, ],
                         self.p.primes,
                         "Check list for 3")

    def test_isprime_for4(self):
        self.p.is_prime(4)
        self.assertEqual([2, 3, 5, ],
                         self.p.primes,
                         "Check list for 4")
        self.assertFalse(self.p.is_prime(4), "Check result for ")

    def test_isprime_for5(self):
        self.p.is_prime(5)
        self.assertEqual([2, 3, 5, ],
                         self.p.primes,
                         "Check list for 5")
        self.assertTrue(self.p.is_prime(5), "Check result for 5")

    def test_isprime_for6(self):
        self.p.is_prime(6)
        self.assertEqual([2, 3, 5, 7, ],
                         self.p.primes,
                         "Check list for 6")
        self.assertFalse(self.p.is_prime(6), "Check result for 6")

    def test_isprime_for11(self):
        n = 11
        self.assertTrue(self.p.is_prime(n), "Check result for {}".format(n))
        self.assertEqual([2, 3, 5, 7, 11,],
                         self.p.primes,
                         "Check list for {}".format(n))


class TestPrimes(unittest.TestCase):

    def setUp(self):
        self.p = Primes()
        self.p.clear()  # чтобы не мешал Синглтон

    def test_create_def(self):
        self.assertEqual(1,
                         self.p.bufsize,
                         "Check default bufsize")
        self.assertEqual([2, ],
                         self.p.get_primes,
                         "Check default cache")

    def test_create_bufsize2(self):
        p1 = Primes(2)
        self.assertEqual([2, ],
                         p1.get_primes,
                         "Check default cache for bufsize=2")

    def test_index_def(self):
        self.assertEqual(2, self.p[0])
        self.assertEqual(1, len(self.p), "Check length of cache")
        self.assertEqual(3, self.p[1])
        self.assertEqual(2, len(self.p), "Check length of cache")
        self.assertEqual(5, self.p[2])
        self.assertEqual(3, len(self.p), "Check length of cache")
        self.assertEqual([2, 3, 5, ],
                         self.p.get_primes,
                         "Check default cache")

    def test_index_bufsize2(self):
        p1 = Primes(2)
        primes_list = [2, 3, 5, 7, 11, ]
        for i in range(len(primes_list)):
            j = primes_list[i]
            self.assertEqual(j, p1[i], "Check Primes[{}] == {}".format(i, j))
            l = (i + p1.bufsize - 1) // p1.bufsize * p1.bufsize +1
            self.assertEqual(l, len(p1), "Check length of cache bufsize == {} for {} is {}".format(p1.bufsize, i, l))
        self.assertEqual(primes_list,
                         self.p.get_primes,
                         "Check default cache")

    def test_index_bufsize3(self):
        p1 = Primes(3)
        primes_list = [2, 3, 5, 7, 11, 13, 17, ]
        for i in range(len(primes_list)):
            j = primes_list[i]
            self.assertEqual(j, p1[i], "Check Primes[{}] == {}".format(i, j))
            l = (i + p1.bufsize - 1) // p1.bufsize * p1.bufsize +1
            self.assertEqual(l, len(p1), "Check length of cache bufsize == {} for {} is {}".format(p1.bufsize, i, l))
        self.assertEqual(primes_list,
                         self.p.get_primes,
                         "Check default cache")