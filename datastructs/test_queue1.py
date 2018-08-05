import unittest
import unittest.mock

from testing import main4unittests as mn


class TestMain(unittest.TestCase):

    def setUp(self):
        self.m = mn.Maxer([1,2,3])
        print("Set Up")

    @unittest.mock.patch('main4unittests.f')
    def testMax1(self, a):
        a.side_effect = [0] # подменить результат возврата функции f() в значение 5
        self.assertEqual(self.m.max(), 3, "max([1,2,3])")

    def testMax2(self):
        self.m.append(5)
        self.assertEqual(self.m.max(), 5, "max([1,2,3])")

    def tearDown(self):
        print("Tear Down")
