# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    
    N = len(A)
    
    if N <= 1:
        return A

    if K == 0 or K == N:
        return A

    R = A

    for k in range(K):
        R = [R[-1]] + R[0:-1] 

    return R


if __name__ == '__main__':
    A = [1,2,3,4]

    for K in [0,1,2,3,4,5]:
        print(K, solution(A, K))
