import unittest

from datastructure.排序.quicksort import quick_sort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_list_is_none(self):
        test_list = None
        result = quick_sort(test_list)
        self.assertEqual(None, result)

    def test_list_is_empty(self):
        test_list = []
        result = quick_sort(test_list)
        self.assertEqual([], result)


if __name__ == '__main__':
    unittest.main()
