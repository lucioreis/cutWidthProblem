import os
import pathlib as path
import numpy as np
from GraphStructure import Graph

# import numpy as np


def pipe(*args, params=[], **kwargs):
    result = args[0](params, **kwargs)
    for func in args[1:]:
        result = func(result, **kwargs)
    return result


def tap(arg):
    print("{trace}\n{arg}\n{trace}".format(trace="="*80, arg=arg))
    return arg


def list_files(directories, **kwargs):
    files_path = []
    for directory in directories:
        listfiles = os.listdir(directory)
        listfiles.sort()
        for file in listfiles:
            file_path = path.Path(
                "{dir}/{file}".format(dir=directory, file=file)
            )
            files_path.append(file_path)
    return files_path


def open_file(filename, **kwargs):
    content = []
    with open(filename, 'r') as file:
        for line in file:
            content.append(line)
    return content


def open_files(list_of_files, **kwargs):
    contents = []
    for file_name in list_of_files:
        file_content = open_file(file_name)
        contents.append(file_content)
    return contents


def interpret_list(list_of_content, **kwargs):
    instance_name = (list_of_content[0]).split()[-1]
    num_edges, num_vertices, num_arcs = (
        int(x) for x in list_of_content[1].split())
    arcs = [(int(i.split()[0]), int(i.split()[1])) for i in list_of_content[2:]]
    arcs = [(i[0], i[1]) if i[0] <= i[1] else (i[1], i[0]) for i in arcs]
    return Graph(instance_name,
                 num_vertices,
                 num_arcs,
                 arcs)


def interpret_grid(list_of_content, **kwargs):
    instance_name = (list_of_content[0]).split()[-1]
    grid = [[int(value) for value in line.split()] for line in list_of_content[1:]]
    arcs = []
    for i in range(len(grid)):
        for j in range(i, len(grid[i])):
            if grid[i][j] == 1:
                arcs.append((i+1, j+1))

    # arcs = [(i[0], i[1]) if i[0] <= i[1] else (i[1], i[0]) for i in arcs] this one wont never happen
    num_arcs = len(arcs)
    num_vertices = len(grid)
    return Graph(instance_name,
                 num_vertices,
                 num_arcs,
                 arcs)


def interpret_data(list_of_contents, dir=str()):
    instance_name = list_of_contents[0]
    datas = []
    for data in list_of_contents:
        if(data[0].startswith("Grid")):
            datas.append(interpret_grid(data))
        else:
            datas.append(interpret_list(data))
    return datas


def count_edge(graph):
    accum = []
    cuts = [0]*(len(graph) - 1)
    for bottom, top in graph:
        for i in range(bottom, top):
            cuts[i] += 1
    return max(cuts)


def cut_widhts(graphs, **kwargs):
    cws = []
    for graph in graphs:
        cws.append(count_edge(graph))
    return cws


def local_min(graph):
    pass
