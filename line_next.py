from threading import Thread
from my_time import timeit


class LineNext(Thread):
    env = None
    line = 0
    res = []

    def __init__(self, env, line):
        Thread.__init__(self)
        self.env = env
        self.line = line
        self.res = [False] * env.size

    def run(self):
        for j in range(self.env.size):
            self.res[j] = self.env.live(self.line, j)
