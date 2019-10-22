"""
This is a demo task.

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited. 
"""
from utils import *


@timetest
def solution(A):
    ceil = 1

    P = [a for a in A if a > 0]

    if not P:
        return ceil

    maxPPlus1 = max(P) + 1

    R = set(range(1, maxPPlus1))

    D = list(R - set(P))

    if D:
        ceil = min(D)
    else:
        ceil = maxPPlus1

    return ceil


@timetest
def solution2(A):
    ceil = 1

    maxAPlus1 = max(A) + 1

    if maxAPlus1 <= 1:
        return ceil

    R = [0] * maxAPlus1

    for a in A:
        if a > 0:
            R[a - 1] = 1

    try:
        ceil = R.index(0) + 1
    except:
        ceil = maxAPlus1

    return ceil


if __name__ == '__main__':

    A = [1]

    A = [9]

    # A = [1, 3, 6, 4, 1, 2]

    # A = [1,2,3]

    # A = sample_list(-100000, -1, 10005)

    # A = sample_list(-1000000, 1000000, 100000)

    print(solution(A))
    print(solution2(A)) # 100%