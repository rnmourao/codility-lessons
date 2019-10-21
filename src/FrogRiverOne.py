from utils import *

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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
    "100% Correcteness, 80% Performance = 90%"
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
    solution3(X, A)