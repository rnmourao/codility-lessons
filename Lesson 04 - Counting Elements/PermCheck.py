"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].
"""
import sys
sys.path.append("..")

from utils import *


@timetest
def solution(A):

    A.sort()

    B = list(range(1, len(A) + 1))
    
    if A != B:
        return 0

    return 1

@timetest
def solution2(A):
    lenA = len(A)
    B = set(A)
    lenB = len(B)
    if lenA != lenB:
        return 0

    C = set(range(1, lenB + 1))
    D = C - B
    if D:
        return 0

    return 1

@timetest
def solution3(A):
    N = len(A)
    n = 1

    A.sort()

    while n <= N:
        if n == A[0]:
            del A[0]
        else:
            return 0
        n += 1
    
    if not A:
        return 1

    return 0


if __name__ == '__main__':
    A = [1]

    # A = [2]

    # A = [2, 1]

    A = list(range(1, 1000000))  

    # A = list(range(1, 10))  

    print(solution(A))
    print(solution2(A))
    print(solution3(A))
    
