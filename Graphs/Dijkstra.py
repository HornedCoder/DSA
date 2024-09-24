import heapq

def dijkstra(graph, start):
    """
    Function to implement Dijkstra's algorithm.
    :param graph: A dictionary where the keys are node identifiers and the values are lists of (neighbor, weight) tuples.
    :param start: The starting node for the shortest path calculation.
    :return: A dictionary of shortest distances from the start node to all other nodes.
    """

    # Initialize the distance dictionary with infinity for all nodes except the start node
    distances = {node : float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store (distance, node) pairs
    priority_queue = [(0, start)]

    while priority_queue:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        # If the distance for the current node is already greater than the known distance, skip
        if current_distance > distances[current_node]:
            continue

        # Iterate over the neighbors of the current node
        for neighbour, weight in graph[current_node]:
            distance = current_distance+weight

            # If a shorter path is found, update the distance and push it into the priority queue
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(priority_queue,(distance, neighbour))
            
    return distances

# Example usage
if __name__ == "__main__":
    # Graph represented as an adjacency list (dictionary of lists of tuples)
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    
    # Start node is 'A'
    start_node = 'A'
    
    # Get the shortest distances from 'A' to all other nodes
    distances = dijkstra(graph, start_node)
    
    print("Shortest distances from node A:", distances)