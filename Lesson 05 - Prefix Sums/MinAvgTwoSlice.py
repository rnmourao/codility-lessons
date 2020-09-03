"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).
For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:
slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.
Write a function:
int solution(int A[], int N);
that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.
For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].

"""
from typing import List


def prefix_sums(A, N):
    sums = [0] * (N + 1)
    for i in range(1, N+1):
        sums[i] = sums[i - 1] + A[i - 1]
    return sums


def average(sums, P, Q):
    return (sums[Q + 1] - sums[P]) / (Q - P + 1)


def solution(A: List[int], N: int) -> int:

    sums = prefix_sums(A, N)

    min_avg = 100000
    p = -1
    for P in range(0, N - 1):
        for Q in range(P + 1, N ):
            avg = average(sums, P, Q)
            if avg <= min_avg:
                if avg == min_avg:
                    if p < P:
                        continue
                min_avg = avg
                p = P
    
    return p
                

if __name__ == "__main__":
    A = [4, 2, 2, 5, 1, 5, 8]
    N = len(A)

    print(solution(A, N))
    
