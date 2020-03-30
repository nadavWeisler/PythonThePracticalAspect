import ex1
import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(ex1.min_count1([1, 4, 2, 10, 102]), [1, 1], "min_count1([1, 4, 2, 10, 102]) Should be [1, 1]")
        self.assertEqual(ex1.min_count2([1, 4, 2, 10, 102]), [1, 1], "min_count2([1, 4, 2, 10, 102]) Should be [1, 1]")
        self.assertEqual(ex1.min_count1([-1, 2, -1, 3]), [-1, 2], "ex1.min_count1([-1, 2, -1, 3]) Should be [-1, 2]")
        self.assertEqual(ex1.min_count2([-1, 2, -1, 3]), [-1, 2], "ex1.min_count2([-1, 2, -1, 3]) Should be [-1, 2]")
        self.assertEqual(ex1.min_count1([1, 1, 1, 1, 1]), [1, 5], "ex1.min_count1([1, 1, 1, 1, 1]) Should be [1, 5]")
        self.assertEqual(ex1.min_count2([1, 1, 1, 1, 1]), [1, 5], "ex1.min_count2([1, 1, 1, 1, 1]) Should be [1, 5]")
        self.assertEqual(ex1.min_count1([1]), [1, 1], "ex1.min_count1([1]) Should be [1, 1]")
        self.assertEqual(ex1.min_count2([1]), [1, 1], "ex1.min_count2([1]) Should be [1, 1]")
        self.assertEqual(ex1.min_count1([2, 3]), [2, 1], "ex1.min_count1([2, 3]) Should be [2, 1]")
        self.assertEqual(ex1.min_count2([2, 3]), [2, 1], "ex1.min_count2([2, 3]) Should be [2, 1]")
        self.assertEqual(ex1.min_count1([0]), [0, 1], "ex1.min_count1([0]) Should be [0, 1]")
        self.assertEqual(ex1.min_count2([0]), [0, 1], "ex1.min_count2([0]) Should be [0, 1]")
        self.assertEqual(ex1.min_count1([]), [], "ex1.min_count1([]) Should be []")
        self.assertEqual(ex1.min_count2([]), [], "ex1.min_count2([]) Should be []")
        self.assertEqual(ex1.only_even(3, 10), [4, 6, 8], "ex1.only_even(3, 10) Should be [4, 6, 8]")
        self.assertEqual(ex1.only_even(1, 1), [], "ex1.only_even(1, 1) Should be []")
        self.assertEqual(ex1.only_even(1, 2), [], "ex1.only_even(1, 2) Should be []")
        self.assertEqual(ex1.only_even(1, 3), [2], "ex1.only_even(1, 3) Should be [2]")
        self.assertEqual(ex1.only_even(10, 3), [4, 6, 8], "ex1.only_even(10, 3) Should be [4, 6, 8]")
        self.assertEqual(ex1.only_strings([1, "a", 2]), ["a"], "ex1.only_strings([1, 'a', 2]) Should be ['a']")
        self.assertEqual(ex1.only_strings(["v", "a", 2]), ["v", "a"],
                         "ex1.only_strings(['v', 'a', 2]) Should be ['v', 'a']")
        self.assertEqual(ex1.only_strings([1, 2, 3, 4]), [], "ex1.only_strings([1, 2, 3, 4]) Should be []")
        self.assertEqual(ex1.only_strings(["a", "a", 2]), ["a", "a"],
                         "ex1.only_strings(['a', 'a', 2]) Should be ['a', 'a']")
        self.assertEqual(ex1.only_strings([]), [], "ex1.only_strings([]) Should be []")


if __name__ == '__main__':
    unittest.main()
