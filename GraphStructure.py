import numpy as np


class Graph(object):
    def __init__(self, name, num_vertices, num_arcs, arcs):
        self.instance_name = name
        self.num_vertices = num_vertices
        self.vertices = [i for i in range(1, num_vertices+1)]
        self.num_arcs = num_arcs
        self.arcs = arcs
        self.index = 0
        self.width = self.__width()

    def __str__(self):
        return self.__str_arcs()

    def __getitem__(self, indice):
        return (self.arcs[indice], self.arcs[indice+1])

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
        return "\n***\nname: %s\nwidth: %d, n_vertices: %d, n_arcs:%d \n%s\n" % (
            self.instance_name,
            self.width,
            self.num_vertices,
            self.num_arcs,
            self.__str_arcs()
        )

    def __len__(self):
        return len(self.arcs)

    def __format__(self, format_spec):
        return self.__str__()

    # == operator
    def __eq__(self, other):
        return self.width == other.width

    # < operator
    def __lt__(self, other):
        return self.width < other.width

    # <= operator
    def __le__(self, other):
        return self.width <= other.width

    # >= operator
    def __ge__(self, other):
        return self.width >= other.width

    # > operator
    def __gt__(self, other):
        return self.width > other.width

    def swap(self, one, other):
        indx_one = self.vertices.index(one)
        indx_other = self.vertices.index(other)
        # print("indx one: {}, other: {}".format(indx_one, indx_other))
        self.vertices[indx_one], self.vertices[indx_other] = self.vertices[indx_other], self.vertices[indx_one]
        for i in range(len(self.arcs)):
            if self.arcs[i] == one:
                self.arcs[i] = other
            if self.arcs[i] == other:
                self.arcs[i] = one
        self.width = self.__width()

    def copy(self):
        new_graph = Graph(self.instance_name+"copy",
                          self.num_vertices,
                          self.num_arcs,
                          list(self.arcs))
        return new_graph

    def __str_arcs(self):
        _str_ = "({} {})|"*(len(self.arcs)//2)
        _str_ = "<|{}|>\n".format(_str_)
        return _str_.format(*self.arcs)

    def __width(self):
        cuts = [0]*(len(self.vertices) - 1)
        for bottom, top in zip(self.arcs[0::2], self.arcs[1::2]):
            for i in range(bottom - 1, top - 1):
                cuts[i] += 1
        return max(cuts)    