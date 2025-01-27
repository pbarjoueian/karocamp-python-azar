from insertion_sort import insertion_sort

import pytest

# my_list = [5, 1, 8, 435, 465, 71]
# print(insertion_sort(my_list))


# a = int(-10)
# assert isinstance(a, int)
# assert a > 0


# insertion_sort_test.py

# assert insertion_sort([3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]
# assert insertion_sort([1, 1, 1]) == [1, 1, 1]
# assert insertion_sort([]) == []


# def test_insertion_sort():
#     assert insertion_sort([3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]
#     assert insertion_sort([1, 1, 1]) == [1, 1, 1]
#     assert insertion_sort([]) == []


def test_no_argument_raises():
    with pytest.raises(TypeError):
        insertion_sort()


# class TestExceptions():
#     def test_no_argument_raises(self):
#         with pytest.raises(TypeError):
#             insertion_sort()

#     def test_different_types_raises(self):
#         with pytest.raises(TypeError):
#             insertion_sort(["a", 1])


# insertion_sort_test.py
import unittest


class InsertionSort(unittest.TestCase):
    def test_five_items(self):
        input = [3, 2, 4, 1, 5]
        expected = [1, 2, 3, 4, 5]
        actual = insertion_sort(input)
        self.assertEqual(actual, expected)

    def test_empty(self):
        actual = insertion_sort([])
        self.assertEqual(actual, [])
