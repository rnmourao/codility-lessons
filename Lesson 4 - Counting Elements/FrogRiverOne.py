"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

    def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

        N and X are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..X].

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
from utils import *


@timetest
def solution(X, A):

    N = len(A)

    if X > N:
        return -1

    if X not in A:
        return -1

    B = set(range(1, X))

    t = -1
    n = 0
    matched = False
    while n < N:
        if A[n] == X:
            matched = True
        
        if matched:
            C = set(A[:n + 1]) 
            if  B.issubset(C):
                t = n
                break

        n +=1
    
    return t


@timetest
def solution2(X, A):

    B = list(range(1, X))

    t = -1
    match = False
    n = 0
    for a in A:
        if a == X:
            match = True

        if a < X:
            
            try:
                B.remove(a)
            except:
                pass
        
        if match and not B:
            t = n
            break
        
        n += 1
        
    return t


@timetest
def solution3(X, A):
    
    B = [1] * (X - 1)
    C = [0] * (X - 1)

    t = -1
    match = False
    n = 0
    for a in A:
        if a == X:
            match = True

        if a < X:
            B[a-1] = 0
        
        if match:
            if B == C:
                t = n
                break
        
        n += 1
        
    return t


if __name__ == '__main__':
    X, A = (5, [1, 3, 1, 4, 2, 3, 5, 4])

    # X, A = (5, [1,2,3,4,4,4])

    # X, A = (5, [5])

    # X, A = (2, [2, 2, 2, 2, 2])

    # X, A = (3, [1, 3, 1, 3, 2, 1, 3])

    solution(X, A)
    solution2(X, A)
    solution3(X, A) # 100% Correcteness, 80% Performance, 90% Overall