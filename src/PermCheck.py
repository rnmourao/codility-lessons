from utils import *
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

@timetest
def solution(A):

    A.sort()

    B = list(range(1, len(A) + 1))
    
    if A != B:
        return 0

    return 1

@timetest
def solution2(A):
    # check for duplicates
    lenA = len(A)
    B = set(A)
    lenB = len(B)
    if lenA != lenB:
        return 0

    # check if some value is missing
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
    
