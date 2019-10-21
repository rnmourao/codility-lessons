from utils import *

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

@timetest
def solution(N, A):

    counters = [0] * N

    max_counter = 0
    last_was_max_counter = True
    for a in A:
        if a == N + 1:
            if not last_was_max_counter:
                last_was_max_counter = True
                counters = [max_counter] * N
        else:
            value = counters[a-1] + 1
            counters[a-1] = value
            last_was_max_counter = False

            if value > max_counter:
                max_counter = value
    
    return counters


if __name__ == '__main__':

    N, A = (5, [3,4,4,6,1,4,4])

    N, A = (1, [2])

    N, A = (100, [1]*100000)

    N, A = (100000, [100001] * 100000)

    solution(N, A)