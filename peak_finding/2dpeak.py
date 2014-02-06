"""
       File : 2dpeak.py
     Author : Drew Verlee
       Date : 29.06.13.
     GitHub : https://github.com/Midnightcoffee/
Description : Program and tests for finding peak in a Matrix, inspired by
    lecture : http://ocw.mit.edu/courses/electrical-engineering-and-computer-
    science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-1-
    algorithmic-thinking-peak-finding/
"""

import unittest
# You will need python 2.7, to run simple type: python 2dpeak.py

# Note this probable isn't the efficient because:
#     A) its recursive
#     B) I copy over the matrix
# some random things I didn't test for
# TODO make sure we have matrix, with equal length rows etc..
# TODO make sure we have numbers, and that they are positive
# TODO other edge cases?

def two_peak(M):
    """find a  peak in a matrix

    :M: Matrix
    :returns: location of peak (i,j) in the (M)atrix
    : Example:
        1  2  2
        1 [3] 2
        1  2  2
    """

    # find out how many columns and rows we have
    columns = len(M[0])
    # pick middle column j = M/2
    j = len(M[0])/2
    # find a global max on column j at (i,j)
    gm = max(M[j])
    i = M[j].index(gm)
    # label some key concepts
    left = j - 1
    right = j + 1

    # pick left columns if (i, j-1) is > (i,j)
    if  left >= 0 and M[i][left] > M[i][j]:
        NM = []
        for ir, r in enumerate(M): # row
            NM.append([])
            for ic, c in enumerate(r): # index, column
                if ic < j:
                    NM[ir].append(c)
        return two_peak(NM)
    # pick right columns if (i, j+1) is > (i,j)
    elif right < columns and M[i][right] > M[i][j]:
        NM = []
        for ir, r in enumerate(M): # row
            NM.append([])
            for ic, c in enumerate(r): # index, column
                if ic > j:
                    NM[ir].append(c)
        return two_peak(NM)
    else:
        return M[i][j]
    # otherwise we found a peak


class TestTwoPeak(unittest.TestCase):
    """a peak is the highest number above, below, right and left"""
    msg = 'failed to find the peak {0} in {1}, found {2}'

    def test_small_matrix(self):
        M = [
            [1,2,3],
            [1,3,2]
            ]
        correct_peak = 3
        found_peak = two_peak(M)
        self.assertEqual(correct_peak, found_peak,
                self.msg.format(correct_peak, M, found_peak))

    def test_medium_matrix(self):
        M = [
            [1,2,3],
            [1,3,2],
            [3,2,1]
            ]
        correct_peak = 3
        found_peak = two_peak(M)
        self.assertEqual(correct_peak, found_peak,
                self.msg.format(correct_peak, M, found_peak))

    def test_large_matrix(self):
        M = [
            [1,2,3,2],
            [1,3,2,1],
            [3,2,1,1],
            [3,2,1,1]
            ]
        correct_peak = 3
        found_peak = two_peak(M)
        self.assertEqual(correct_peak, found_peak,
                self.msg.format(correct_peak, M, found_peak))

if __name__ == '__main__':
    unittest.main()
