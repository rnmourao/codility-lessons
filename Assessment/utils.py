def timetest(input_func):

    def timed(*args, **kwargs):
        import time


        start_time = time.time()
        result = input_func(*args, **kwargs)
        end_time = time.time()
        print("Method Name:", input_func.__name__, 
            #   "Args:", args, 
            #   "Kwargs:", kwargs, 
              "Execution Time:", end_time - start_time)

        return result
    
    
    return timed


def sample_list(first, last, size):
    from random import sample

    return sample(range(first, last + 1), size)