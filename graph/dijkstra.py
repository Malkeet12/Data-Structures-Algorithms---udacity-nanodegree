# Dijkstra's Algorithm In the "Greedy Algorithms" lesson, we implemented the Dijkstra's Algorithm to find the
# distance of each node from the given source node. In this exercise, you'll implement the same Dijkstra's algorithm
# to find the length of the shortest path between a given pair of nodes, but this time we will have a better time
# complexity. First, let's build the graph.
#
# Graph Representation In order to run Dijkstra's Algorithm, we'll need to add distance to each edge. We'll use the
# GraphEdge class below to represent each edge between a pair of nodes. You are free to create your own
# implementation of an undirected graph. Helper Code
from collections import defaultdict


# Helper Class
class GraphEdge(object):
    def __init__(self, destinationNode, distance):
        self.node = destinationNode
        self.distance = distance


# Helper Classes
class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    # adds an edge between node1 and node2 in both directions
    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


import math


def dijkstra(graph, start_node, end_node):
    shortest_distance = {}
    distance_dict = {node: math.inf for node in graph.nodes}

    distance_dict[start_node] = 0

    while distance_dict:
        # Sort the distance_dict, and pick the key:value having smallest distance
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]

        # Remove the current node from the distance_dict, and store the same key:value in shortest_distance
        shortest_distance[current_node] = distance_dict.pop(current_node)
        for edge in current_node.edges:
            if edge.node in distance_dict:

                distance_to_neighbour = node_distance + edge.distance
                if distance_dict[edge.node] > distance_to_neighbour:
                    distance_dict[edge.node] = distance_to_neighbour

    return shortest_distance[end_node]


# Test Case 1:

# Create a graph
node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])

# add_edge() function will add an edge between node1 and node2 in both directions
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_y, 5)

# Shortest Distance from U to Y is 14
print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(graph, node_u, node_y)))

# Test Case 2
node_A = GraphNode('A')
node_B = GraphNode('B')
node_C = GraphNode('C')

graph = Graph([node_A, node_B, node_C])

graph.add_edge(node_A, node_B, 5)
graph.add_edge(node_B, node_C, 5)
graph.add_edge(node_A, node_C, 10)

# Shortest Distance from A to C is 10
print('Shortest Distance from {} to {} is {}'.format(node_A.value, node_C.value, dijkstra(graph, node_A, node_C)))