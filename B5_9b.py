import time
from functools import wraps


class Timer:

    def __init__(self, func, num_runs=10):
        self.func=func
        self.num_runs = num_runs
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

    def __call__(self,iter):
        avg_time = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.func(iter)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.num_runs
        print("Выполнение заняло %.5f секунд" % avg_time)

@Timer
### <<полезный>> код
def f(iter):
    """
        Цикла, который ничего не делает.
        Параметер iter задает количество итераций
    """
    for j in range(iter):
        pass

f(1000000)
