import numpy as np


class Graph(object):
    def __init__(self, name, num_vertices, num_arcs, arcs):
        self.instance_name = name
        self.num_vertices = num_vertices
        self.vertices = [i for i in range(1, num_vertices+1)]
        self.num_arcs = num_arcs
        self.arcs = arcs
        self.index = 0

    def __str__(self):
        return self.__str_arcs()

    def __getitem__(self, indice):
        return self.arcs[indice]

    def __next__(self):
        try:
            v1 = self.arcs[self.index]
            v2 = self.arcs[self.index+1]
            self.index += 2
            return (v1, v2)
        except IndexError:
            self.index = 0
            raise StopIteration

    def __iter__(self):
        return self

    def __repr__(self):
        return "\n***\nname: %s\nn_vertices: %d ,n_edges: %d, n_arcs:%d \n%s\n" % (
            self.instance_name,
            self.num_vertices,
            self.edges,
            self.num_arcs,
            __str_arcs()
        )

    def __len__(self):
        return len(self.arcs)

    def __format__(self, format_spec):
        return self.__str__()

    def swap(one, other):
        indx_one = self.vertice.index(one)
        indx_other = self.vertice.index(other)
        self.vertice[indx_one], self.vertice[indx_other] = self.vertice[indx_other], self.vertice[indx_one]
        for vertice in self.arcs:
            if vertice == one:
                vertice = other
            if vertice == other:
                vertice = one        

    def copy(self):
        new_graph = Graph(self.instance_name+"copy",
                          self.num_vertices,
                          self.num_arcs,
                          self.vertices,
                          self.arcs.copy())
        return new_graph

    def __str_arcs(self):
        _str_ = "({} {})|"*(len(self.arcs)//2)
        _str_ = "<|{}|>\n".format(_str_)
        return _str_.format(*self.arcs)
