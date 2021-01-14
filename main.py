import itertools

import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
from typing import Union


def add_edge(f_item: str, s_item: str, graph=Union[nx.Graph, nx.DiGraph]):
    graph.add_edge(f_item, s_item)
    graph.add_edge(s_item, f_item)


def draw(graph=Union[nx.Graph, nx.DiGraph]):
    nx.draw_circular(
        graph,
        node_color='red',
        node_size=1000,
        with_labels=True
    )

    plt.show()


if __name__ == '__main__':
    graph = nx.Graph()
