from utils import timetest


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

@timetest
def solution(A):
    """Returns the missing element of a list of distinct integers.
       N is an integer within the range [0..100,000];
       the elements of A are all distinct;
       each element of array A is an integer within the range [1..(N + 1)].


    Parameters:
    A (list): list of distinct integers


    Returns:
    N (int): missing element


    """

    maximum = len(A) + 1

    A = set(A)

    B = set(range(1, maximum + 1))

    C = B - A

    return C.pop()

if __name__ ==  '__main__':
    A = []

    print(solution(A))

