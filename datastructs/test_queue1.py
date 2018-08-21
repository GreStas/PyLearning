#!/usr/bin/env python3

import unittest

from datastructs.queue1 import Queue1 as Q1


class TestMain(unittest.TestCase):
    # def tearDown(self): print("Tear Down")

    def setUp(self):
        self.q1 = Q1(3)

    def testCreate(self):
        size = 4
        self.q1 = Q1(size)
        self.assertEqual([None,]*size,
                         self.q1.data,
                         "Test content of rawdata for just created Queue1")
        self.assertEqual("None:None {}".format(repr([None]*size)),
                         repr(self.q1),
                         "Test __repr__ for just created Queue1")
        self.assertEqual("{}".format(str([])),
                         str(self.q1),
                         "Test __str__ for just created Queue1")
        with self.assertRaises(ValueError) as cm:
            self.q1.get()
        err = cm.exception
        self.assertEqual("Queue is empty.",
                         str(err),
                         "Check exception message:")

    def testPut1st(self):
        self.q1.put(1)
        self.assertEqual((0,1,1),
                         (self.q1.tail,self.q1.head,self.q1.data[self.q1.tail]),
                         "Check attributes:")
        self.assertEqual(1,
                         len(self.q1),
                         "Test length:")
        self.assertEqual("{}:{} {}".format(repr(0), repr(1), repr([1, None, None,])),
                         repr(self.q1),
                         "Test repr:")
        self.assertEqual(str([1,]),
                         str(self.q1),
                         "Test str:")

    def testFillUp(self):
        for i in range(self.q1.size):
            self.q1.put(i+1)
        self.assertEqual((0, 0, 1, [1, 2, 3]),
                         (self.q1.tail, self.q1.head, self.q1.data[self.q1.tail], self.q1.data),
                         "Check attributes:")
        self.assertEqual(3,
                         len(self.q1),
                         "Test length:")
        self.assertEqual("{}:{} {}".format(repr(0), repr(0), repr([1, 2, 3,])),
                         repr(self.q1),
                         "Test repr:")
        self.assertEqual(str([1, 2, 3]),
                         str(self.q1),
                         "Test str:")

    def testOverflow(self):
        for i in range(self.q1.size):
            self.q1.put(i+1)
            # self.q1.prn_state()
        else:
            with self.assertRaises(ValueError) as cm:
                self.q1.put(i + 1)
            err = cm.exception
            self.assertEqual("Queue is full.",
                             str(err),
                             "Check exception message:")
        self.assertEqual((0, 0, 1, [1, 2, 3]),
                         (self.q1.tail, self.q1.head, self.q1.data[self.q1.tail], self.q1.data),
                         "Check attributes:")
        self.assertEqual(3,
                         len(self.q1),
                         "Test length:")
        self.assertEqual("{}:{} {}".format(repr(0), repr(0), repr([1, 2, 3,])),
                         repr(self.q1),
                         "Test repr:")
        self.assertEqual(str([1, 2, 3]),
                         str(self.q1),
                         "Test str:")

    def testGet1st(self):
        self.q1.put(1)
        self.assertEqual(1, self.q1.get(), "Check getting 1st value.")
        self.assertEqual((None, None,),
                         (self.q1.tail,self.q1.head),
                         "Check attributes:")

    def testGetOverhead(self):
        self.q1.put(1)
        self.q1.get()
        with self.assertRaises(ValueError) as cm:
            self.q1.get()
        err = cm.exception
        self.assertEqual("Queue is empty.",
                         str(err),
                         "Check exception message:")

    def testGetOverheadCycle(self):
        # Заполним полностью
        self.q1.put(1); self.q1.put(2); self.q1.put(3)
        # Вычитаем на 1 меньше
        self.q1.get(); self.q1.get()
        self.q1.put(4); self.q1.put(5)
        self.q1.get(); self.q1.get()
        self.assertEqual((1, 2, 5, [4, 5, 3]),
                         (self.q1.tail, self.q1.head, self.q1.data[self.q1.tail], self.q1.data),
                         "Check attributes:")

    def testLong(self):
        """ Goal: Create 2-nd list from 1-st list by Queue1. """
        li = [x for x in range(1, 11)]
        lo = []
        for x in li:
            try:
                self.q1.put(x)
            except ValueError as eread:
                while True:
                    try:
                        lo.append(self.q1.get())
                    except ValueError as ewrite:
                        break
                self.q1.put(x)
        else:
            while True:
                try:
                    lo.append(self.q1.get())
                except ValueError as ewrite:
                    break
        self.assertEqual(li,
                         lo,
                         "Check lists:")
        self.assertEqual((None, None,),
                         (self.q1.tail,self.q1.head),
                         "Check attributes:")
