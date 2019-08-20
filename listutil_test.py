import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):
    """Test the unique method."""
    def test_empty_list(self):
        self.assertEqual([],unique([]))

    def test_oneitem_list(self):
        self.assertEqual([10],unique([10]))
        self.assertEqual(['apple'],unique(['apple']))

    def test_many_oneitem_list(self):
        self.assertEqual([6],unique([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]))
        self.assertEqual(['doc'],unique(['doc','doc','doc','doc','doc','doc','doc','doc']))

    def test_many_twoitem_list(self):
        self.assertEqual(['b', 'a'],unique(['b','a','a','b','b','b','a','a']))
        self.assertEqual([[1,2,3,4]],unique([[1,2,3,4],[1,2,3,4]]))

    def test_int(self):
        with self.assertRaises(TypeError): 
            lst = unique(-10) 

        with self.assertRaises(TypeError): 
            lst = unique(65)     

