import itertools

import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt


def add_edge(f_item, s_item, graph=None):
    graph.add_edge(f_item, s_item)
    graph.add_edge(s_item, f_item)


if __name__ == '__main___':
    graph = nx.Graph()
    add_edge('A', 'B', graph=graph)
