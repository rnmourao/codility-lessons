# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    A.sort()

    odd = None
    for a in A:

        if not odd:
            odd = a
        elif odd == a:
            odd = None
        else:
            if odd:
                break

    return odd
                

if __name__ == '__main__':
    from utils import time_delta

    X = [9,3,9,3,9,7,9]

    X = [1, 1, 1]

    print(solution(X))

    time_delta(solution, X)

