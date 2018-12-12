class Env:
    def __init__(self, size=10):
        self.map = [False] * size * size
        self.size = size
        self.to_check = set()
        self.adj = list()
        for i in range(size):
            self.adj.append([0] * size)

    def focus_set(self, i, j):
        cell = self.index_to_cell(i, j)
        if not cell == -1:
            self.map[cell] = True
            for x in [i - 1, i, i + 1]:
                for y in [j - 1, j, j + 1]:
                    self.to_check.add((x, y))

    def print_adj(self):
        for line in self.adj:
            print(line)

    def adj_set(self, i, j, booly):
        cell = self.index_to_cell(i, j)
        self.print_adj()
        if not cell == -1:
            self.map[cell] = booly
            inc = 1 if booly else -1
            for x in [i - 1, i, i + 1]:
                for y in [j - 1, j, j + 1]:
                    if x > 0 and x < self.size and y > 0 and y < self.size and (not (x == i and y == j)):
                        print(self.adj[x][y])
                        self.adj[x][y] += inc
                    else:
                        print("{}:{} to {} error on  {}:{}".format(i, j, booly, x, y))

    def index_to_cell(self, i, j):
        if i < 0 or j < 0:
            return -1
        if not j < self.size or not i < self.size:
            return -1
        return i * self.size + j

    def is_alive(self, i, j):
        cell = self.index_to_cell(i, j)
        if cell == -1:
            raise IndexError('Index out of map.')

        return self.map[cell]

    def nb_adj(self, i, j):
        nb = 0
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                if not (x == i and y == j):
                    cell = self.index_to_cell(x, y)
                    if self.map[cell]:
                        nb += 1
        return nb

    def adj_live(self, i, j):
        cell = i * self.size + j
        nb_adj = self.adj[i][j]

        if nb_adj == 3:
            return True

        if self.map[cell]:
            if nb_adj > 3 or nb_adj < 2:
                return False
            return True

        return False

    def live(self, i, j):
        cell = i * self.size + j
        nb_adj = self.nb_adj(i, j)

        if nb_adj == 3:
            return True

        if self.map[cell]:
            if nb_adj > 3 or nb_adj < 2:
                return False
            return True

        return False
