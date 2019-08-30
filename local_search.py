from GraphStructure import Graph
import auxtools as at


def run_neighbors(graph: Graph, num_of_neighbors: int):
    list_of_neighbors = [at.generate_neighbor(graph) for i in range(num_of_neighbors)]
    best = graph
    for neighbor in list_of_neighbors:
        # print("before neighbor.widht: {}, best.widht: {}".format(neighbor.width, best.width))
        best = best if best <= neighbor else neighbor
        # print("after neighbor.widht: {}, best.widht".format(neighbor.width, best.width))
    return best


def local_search(graph: Graph, num_of_neighbors: int):
    best = run_neighbors(graph, num_of_neighbors)
    while best > graph:
        graph = best
        best = run_neighbors(graph, num_of_neighbors)
    return best

