# Connect Islands using Prim’s Algorithm A. Problem Statements In an ocean, there are n islands some of which are
# connected via bridges. Travelling over a bridge has some cost attaced with it. Find bridges in such a way that all
# islands are connected with minimum cost of travelling.
#
# You can assume that there is at least one possible way in which all islands are connected with each other.
#
# You will be provided with two input parameters:
#
# num_islands = number of islands
#
# bridge_config = list of lists. Each inner list will have 3 elements:
#
#  a. island A
#  b. island B
#  c. cost of bridge connecting both islands
# Each island is represented using a number
#
# Example:
#
# num_islands = 4
# bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
# Input parameters explanation:
#
# 1. Number of islands = 4
# 2. Island 1 and 2 are connected via a bridge with cost = 1
#    Island 2 and 3 are connected via a bridge with cost = 4
#    Island 1 and 4 are connected via a bridge with cost = 3
#    Island 4 and 3 are connected via a bridge with cost = 2
#    Island 1 and 3 are connected via a bridge with cost = 10
# In this example if we are connecting bridges like this...
#
# between 1 and 2 with cost = 1
# between 1 and 4 with cost = 3
# between 4 and 3 with cost = 2
# ...then we connect all 4 islands with cost = 6 which is the minimum traveling cost.
#

# B.
#
# Hint: Use a Priority Queue or Min-Heap In addition to using a graph, you may want to use a custom priority queue
# for solving this problem. If you do not want to create a custom priority queue, you can use Python's inbuilt heapq
# implementation.
#
# Using the heapq module, you can convert an existing list of items into a min-heap. The following two
# functionalities can be very handy for this problem:
#
# heappush(heap, item) — add item to the heap
# heappop(heap) — remove the smallest item from the heap
# Let's look at the above methods in action. We start by creating a list of integers.


# C.
#
# The Idea, based on Prim’s Algorithm: Our objective is to find the minimum total_cost to visit all the islands. We
# will start with any one island, and follow a Greedy approach. Step 1 - Create a Graph
#
# Create a graph with given number of islands, and the cost between each pair of islands. A graph can be represented
# as a adjacency_matrix, which is a list of lists. For example, given: num_islands = 4 bridge_config = [[1, 2, 1],
# [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
#
# The graph would look like: graph =  [[], [(2, 1), (4, 3), (3, 10)], [(1, 1), (3, 4)], [(2, 4), (4, 2), (1, 10)],
# [(1, 3), (3, 2)]] where, a sublist at  𝑖𝑡ℎ  index represents the adjacency_list of  𝑖𝑡ℎ  island. A tuple within
# a sublist is (neighbor, edge_cost). Step 2 - Traverse the graph in a Greedy way. Create a blank minHeap,
# and push any one island (vertex) into it. While there are elements remaining in the minHeap, do the following:
#
# Pop out an island having smallest edge_cost, and reduce the heap size. You can use heapq.heappop() for this
# purpose. If the current island has not been visited before, add the edge_cost to the total_cost. You can use a list
# of booleans to keep track of the visited islands. Find out all the neighbours of the current island from the given
# graph. Push each neighbour of the current island into the minHeap. You can use heapq.heappush() for this purpose.
# Mark current island as visited tuple in the adjacency_list of the When we have popped out all the elements from the
# minHeap, we will have the minimum total_cost to visit all the islands.
#


import heapq


def create_graph(no, bridge_config):
    graph = [list() for item in range(no + 1)]

    for value in bridge_config:
        graph[value[0]].append((value[1], value[2]))
        graph[value[1]].append((value[0], value[2]))
    return graph


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)

    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1

    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]

    # Heap is represented as a list of tuples
    # A "node" in heap is represented as tuple (edge_cost, neighbor)
    minHeap = [(0, start_vertex)]
    total_cost = 0

    while len(minHeap) > 0:
        # Here, heapq.heappop() will automatically pop out the "node" having smallest edge_cost, and reduce the heap size
        cost, current_vertex = heapq.heappop(minHeap)

        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue

        # else add cost to total-cost
        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(minHeap, (edge_cost, neighbor))

        # mark current vertex as visited
        visited[current_vertex] = True

    return total_cost


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
