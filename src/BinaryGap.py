# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    import re

    splits = re.split("(1)", str(bin(N)))

    counts = 0
    greatest = 0
    for split in splits:
        if split in ['', '0b']:
            continue

        if split == '1':
            if counts > greatest:
                greatest = counts
                            
        if int(split) == 0:
            counts = len(split)

    
    return greatest


if __name__ == '__main__':

    X = [1,2,3,4,5,6,7,8,9,10,20,32,100,230,529,1041,2147483647]
    for x in X:
        print(x, bin(x), solution(x))