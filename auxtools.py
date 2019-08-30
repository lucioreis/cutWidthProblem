import os
import pathlib as path
import numpy as np
import local_search as ls
from GraphStructure import Graph
import random as rd
from datetime import datetime


def pipe(*args, params=[], **kwargs):
    result = args[0](params, **kwargs)
    for func in args[1:]:
        result = func(result, **kwargs)
    return result


def tap(arg):
    print("{trace}\n{arg}\n{trace}".format(trace="="*80, arg=arg))
    return arg


def list_files(directories: list, **kwargs):
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


def open_file(filename: str, **kwargs):
    content = []
    with open(filename, 'r') as file:
        for line in file:
            content.append(line)
    return content


def open_files(list_of_files: list, **kwargs):
    contents = []
    try:
        for file_name in list_of_files:
            file_content = open_file(file_name)
            contents.append(file_content)
    except IsADirectoryError:
        pass
    return contents


def interpret_list(list_of_content: list, **kwargs):
    instance_name = (list_of_content[0]).split()[-1]
    num_edges, num_vertices, num_arcs = (
        int(x) for x in list_of_content[1].split())
    arcs = [(int(i.split()[0]), int(i.split()[1])) for i in list_of_content[2:]]
    arcs = [(i[0], i[1]) if i[0] <= i[1] else (i[1], i[0]) for i in arcs]
    arcs = [vertice for pair in arcs for vertice in pair]
    return Graph(instance_name,
                 num_vertices,
                 num_arcs,
                 arcs)


def interpret_grid(list_of_content: list, **kwargs):
    instance_name = (list_of_content[0]).split()[-1]
    grid = [[int(value) for value in line.split()] for line in list_of_content[1:]]
    arcs = []
    for i in range(len(grid)):
        for j in range(i, len(grid[i])):
            if grid[i][j] == 1:
                arcs.append(i+1)
                arcs.append(j+1)

    # arcs = [(i[0], i[1]) if i[0] <= i[1] else (i[1], i[0]) for i in arcs] this one wont never happen
    num_arcs = len(arcs)
    num_vertices = len(grid)
    return Graph(instance_name,
                 num_vertices,
                 num_arcs,
                 arcs)


def interpret_data(list_of_contents: list, dir=str()):
    instance_name = list_of_contents[0]
    datas = []
    for data in list_of_contents:
        if(data[0].startswith("Grid")):
            datas.append(interpret_grid(data))
        else:
            datas.append(interpret_list(data))
    return datas


def count_edge(graph: Graph):
    return graph.width


def cut_widhts(graphs: Graph, **kwargs):
    cws = []
    for graph in graphs:
        cws.append(count_edge(graph))
    return cws


def generate_neighbor(graph: Graph, swaps: int = 1):
    neighbor = graph.copy()
    swaps = (len(neighbor.vertices)*10)//100
    for i in range(swaps):
        one = rd.choice(neighbor.vertices)
        other = rd.choice(neighbor.vertices)
        neighbor.swap(one, other)
    return neighbor


def write_results(results: list, **kwargs):
    time_now = datetime.now()
    results = str(results)
    content = "\nTime: {}\nresults: {}\n{}".format(time_now, results, '##'*len(results))
    with open('results', 'a') as file:
        file.write(content)
    return results


def local_searches(graphs: list):
    cws = []
    for graph in graphs:
        cws.append(ls.local_search(graph, 10))
    return cws