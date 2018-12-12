from tkinter import *
from environnement import Env
from line_next import LineNext
from my_time import timeit
from copy import deepcopy


class Display:
    env = None
    cell_size = 8
    master = None
    w = None

    def __init__(self, env):
        self.env = deepcopy(env)
        self.master = Tk(className='Jeu De La Vie')
        self.w = Canvas(self.master, width=self.env.size * self.cell_size, height=self.env.size * self.cell_size)
        self.w.pack()
        start_but = Button(self.master, text='Next', command=self.next_adj)
        start_but.pack(side=BOTTOM, padx=5, pady=5)

    @timeit
    def next_adj(self):
        new = deepcopy(self.env)
        for i in range(self.env.size):
            for j in range(self.env.size):
                booly = self.env.adj_live(i, j)
                if booly != self.env.map[self.env.index_to_cell(i, j)]:
                    new.adj_set(i, j, booly)
        self.env = new
        self.display_state()

    @timeit
    def focus_next(self):
        new = Env(size=self.env.size)
        for i, j in self.env.to_check:
            if self.env.live(i, j):
                new.focus_set(i, j)
        self.env = new
        self.display_state()

    @timeit
    def next(self):
        new = Env(size=self.env.size)
        pool = list()
        for i in range(new.size):
            thr = LineNext(self.env, i)
            thr.start()
            pool.append(thr)

        new_map = []

        for thread in pool:
            thread.join()
            new_map += thread.res

        new.map = new_map
        self.env = new
        self.display_state()

    @timeit
    def display_state(self):
        y = 0
        for i in range(self.env.size):
            x = 0
            for j in range(self.env.size):
                if self.env.is_alive(i, j):
                    self.w.create_rectangle(x, y, x+self.cell_size, y+self.cell_size, fill="black")
                else:
                    self.w.create_rectangle(x, y, x+self.cell_size, y+self.cell_size, fill="white")
                x += self.cell_size
            y += self.cell_size

    def start(self):
        self.display_state()
        self.master.mainloop()
