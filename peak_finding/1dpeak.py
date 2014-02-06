"""
       File : 1dpeak.py
     Author : Drew Verlee
       Date : 29.06.13.
     GitHub : https://github.com/Midnightcoffee/
Description : quick peak find
"""

import unittest


def peak_find(A):
    """
        given an array returns a peak
        [1, 3, 2] => 3
        [4, 3, 3,5] => 4 or 5
    """

    if len(A) == 1:
        return A[0]
    start = 0
    end = len(A)
    middle = (start + end)/2
    right = middle + 1
    left = middle - 1

    if right < end and A[right] > A[middle]:
        return peak_find(A[middle:end])
    elif left >= start and A[left] > A[middle]:
        return peak_find(A[start:middle])
    else:
        return A[middle]

class TestPeakFind(unittest.TestCase):
    """test a one d peak find"""
    msg = 'failed to find peak on '

    def test_one(self):
        A = [3]
        s = peak_find(A)
        self.assertEqual(3, s, self.msg + 'only element, returned {0}'.format(s))

    def test_peak_on_left(self):
        A = [1,2,3]
        s = peak_find(A)
        self.assertEqual(3, s, self.msg + 'left, returned {0}'.format(s))

    def test_peak_on_right(self):
        A = [3,2,1]
        s = peak_find(A)
        self.assertEqual(3, s, self.msg + 'right, returned {0}'.format(s))

    def test_peak_in_middle(self):
        A = [1,3,2]
        s = peak_find(A)
        self.assertEqual(3, s, self.msg + 'middle, returned {0}'.format(s))

    def test_several_peaks(self):
        A = [3,1,3,1,3]
        s = peak_find(A)
        self.assertEqual(3, s, self.msg + 'left, returned {0}'.format(s))


if __name__ == '__main__':
    unittest.main()
