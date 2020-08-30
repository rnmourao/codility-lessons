"""
Write a function:
int solution(int A, int B, int K);
that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
{ i : A ≤ i ≤ B, i mod K = 0 }
For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11]namely 6, 8 and 10.
Write an efficient algorithm for the following assumptions:
A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.

"""

def solution(A: int, B: int, K: int) -> int:
    
    count = 0

    if A % K == 0 or B % K == 0:
        count += 1
    
    a = A // K
    b = B // K

    n = b - a
    if n > 0:
        count += n

    return count


if __name__ == '__main__':

    A = 7
    B = 11
    K = 2
    C = solution(A, B, K)
    print(C)

    A = 0
    B = 2000000000
    K = 1000
    C = solution(A, B, K)
    print(C)

    