from time import sleep, time

# Define a function which takes some argument
def f(sleep_time = 0.1):
    sleep(sleep_time)#f is expecting to be fed sleep default value of 0.1

# We therefore dont need need g anymore
def measure(func):
    def wrapper(*args, **kwargs):
        t=time()
        func(*args, **kwargs)
        print(func.__name__, 'took', time()-t)
        return wrapper
    f = measure(f)
    f(0.2)
    f(sleep_time = 0.3)