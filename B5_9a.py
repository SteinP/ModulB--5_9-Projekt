import time
from functools import wraps

def time_this(num_runs):
    def decorator(func):
        @wraps(func)
        def fun_wrap(iter):
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func(iter)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)
        return fun_wrap
    return decorator

@time_this(num_runs=10)
### <<полезный>> код
def f(iter):
    """
        Цикла, который ничего не делает.
        Параметер iter задает количество итераций
    """
    for j in range(iter):
        pass

f(1000000)
