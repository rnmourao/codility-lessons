from utils import *

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

@timetest
def solution(X, Y, D):
    """Count the minimal number of jumps that the small frog must perform to reach its target.


    Parameters:
    X (int): Frog's current position
    Y (int): Frog's target position
    D (int): Frog jump's distance


    Returns:
    jumps (int): number of jumps


    """

    jumps = (Y - X) / D

    int_jumps = int(jumps)

    if jumps > int_jumps:
        int_jumps += 1

    return int_jumps


if __name__ ==  '__main__':
    X, Y, D = 2, 200000000, 1

    solution(X, Y, D)
    
