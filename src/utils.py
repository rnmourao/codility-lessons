def time_delta(func, arg):
    import time
    from datetime import timedelta    
    start = time.time()
    func(arg)
    end = time.time()
    delta = end - start
    print(delta)