from utils import *

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

@timetest
def solution(A):

    N = len(A)

    b = 0
    c = sum(A)
    smallest = 99999

    for p in range(0, N-1):
        b = b + A[p]
        c = c - A[p]

        diff = abs(b - c)

        if diff < smallest:
            smallest = diff

    return smallest


if __name__ == '__main__':

    # A = [3,1,2,4,3]

    # A = [1,2,-1000,1000]

    # A = [1] * 100000

    # A = [1, 2]

    A = [-1000, 1000]

    print(solution(A))




