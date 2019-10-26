from time import time


def timetest(input_func):

    def timed(*args, **kwargs):

        start_time = time()
        result = input_func(*args, **kwargs)
        end_time = time()
        print("Method Name:", input_func.__name__, 
            #   "Args:", args, 
            #   "Kwargs:", kwargs, 
              "Execution Time:", end_time - start_time)

        return result
    
    return timed


@timetest
def solution(indices, K):
    
    # get length of list of indices
    lenI = len(indices)
    
    # get probable size of each fold
    avg = lenI // K

    # get the remainder indices of a perfect
    rem = lenI % K

    # identify folds indexes
    ixs = []
    i = 0
    while i < lenI:
        ixs.append(i)        
        i += avg
        if rem > 0:
            i += 1
            rem -= 1

    # create folds
    folds = []
    lenIXS = len(ixs)
    for f in range(lenIXS):
        if f + 1 == lenIXS:
            fold = indices[ixs[f]:]
        else:
            fold = indices[ixs[f]:ixs[f+1]]
        folds.append(fold)

    # create train and val sequences
    ls = []
    for f in range(len(folds)):
        train = folds.copy()

        val = train.pop(f)

        ls += train
        ls.append(val)

    return ls


@timetest
def solution2(indices, K):
    
    # get length of list of indices
    lenI = len(indices)
    
    # get probable size of each fold
    avg = lenI // K

    # get the remainder indices of a perfect
    rem = lenI % K

    i = 0 
    j = 0
    result = []
    lenR = K * K
    folds = []
    c = 0
    for f in range(lenR):
        # create i-th fold
        if j < lenI:
            j += avg

            # distribute reimainder through folds
            if rem > 0:
                j += 1
                rem -= 1
            
            # create fold and add it to list of folds
            fold = indices[i:j]
            folds.append(fold)

            # move to next fold
            i = j

        # use k-th fold already created
        else:
            # find k-th fold
            k = f % K

            # do an array rotation
            if k == 0:
                c += 1
            m = (f + c) % K

            # select rotated fold
            fold = folds[m]
        
        # add fold to solution
        result.append(fold)

    return result
    

if __name__ == '__main__':
    # indices, K = ([1,2,3,4], 3)

    # indices, K = ([1, 2], 2)

    # indices, K = ([1,2,3], 2)

    # indices, K = ([1,2,3,4,5,6,7,8,9,10], 4)

    # indices, K = ([1,2,3,4,5,6,7,8,9], 3)

    # indices, K = (list(range(10)), 10)

    # print(solution(indices, K))
    # print(solution2(indices, K))

    indices, K = (list(range(100)), 100)
    solution(indices, K)
    solution2(indices, K)

    # indices, K = (list(range(10000)), 10000)
    # solution(indices, K)
    # solution2(indices, K)

