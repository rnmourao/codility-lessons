# import sys
# sys.path.append("..")

# from utils import *


#@timetest
def solution(indices, K):

    lenI = len(indices)
    
    if lenI == 2:
        return [indices[0], indices[1], indices[1], indices[0]]
    
    size = lenI // K

    s = 0
    folds = []
    for i in range(K):
        fold = indices[:K]
        indices = indices[K:]
        folds.append(fold)

    if indices:
        folds.append(indices)

    result = []
    lenF = len(folds)
    for i in range(lenF):
        group = folds.copy()
        group.pop(i)
        result.append(group)
        result.append(folds[i])
        
    return result

# @timetest
def solution2(indices, K):
    lenI = len(indices)
    
    if lenI == 2:
        return [indices[0], indices[1], indices[1], indices[0]]

    avg = lenI // K

    res = lenI % K

    # identify folds indexes
    iFolds = [0]
    k = 1
    s = 0
    while k < lenI:
        s += avg
        if res > 0:
            s += 1
            res -= 1
        iFolds.append(s)
        k += s

    # create folds
    folds = []
    lenF = len(iFolds)
    for f in range(lenF):
        if f + 1 == lenF:
            fold = indices[iFolds[f]:]
        else:
            fold = indices[iFolds[f]:iFolds[f+1]]
        folds.append(fold)

    # create train and val sequences
    ls = []
    for f in folds:
        train = folds.copy()
        train.remove(f)
        ls += train
        ls.append(f)

    return(ls)
    

if __name__ == '__main__':
    indices, K = ([1,2,3], 2)

    # indices, K = ([1,2,3,4,5,6,7,8,9,10], 3)


    print(solution2(indices, K))