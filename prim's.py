def prim(graph, start):
    """
    graph: dict where keys are nodes and values are lists of (neighbor, weight) tuples.
    start: starting node for the MST.
    """
    # Track which nodes have been added to the MST
    visited = {start}
    
    mst = []
    total_weight = 0
    num_vertices = len(graph)
    
    # Loop until all vertices are in the MST
    while len(visited) < num_vertices:
        min_weight = float('inf')
        best_edge = None
        
        # Look at all visited nodes
        for u in visited:
            # Check all neighbors of the visited nodes
            for v, weight in graph[u]:
                # Find the smallest edge pointing to an unvisited node
                if v not in visited and weight < min_weight:
                    min_weight = weight
                    best_edge = (u, v, weight)
        
        # If no edge is found, the graph is disconnected
        if best_edge is None:
            break
            
        u, v, weight = best_edge
        visited.add(v)
        mst.append((u, v, weight))
        total_weight += weight
        
    return mst, total_weight

# Example usage:
example_graph = {
    'A': [('B', 4), ('H', 8)],
    'B': [('A', 4), ('H', 11), ('C', 8)],
    'C': [('B', 8), ('I', 2), ('D', 7), ('F', 4)],
    'D': [('C', 7), ('F', 14), ('E', 9)],
    'E': [('D', 9), ('F', 10)],
    'F': [('C', 4), ('D', 14), ('E', 10), ('G', 2)],
    'G': [('F', 2), ('I', 6), ('H', 1)],
    'H': [('A', 8), ('B', 11), ('G', 1), ('I', 7)],
    'I': [('C', 2), ('G', 6), ('H', 7)]
}

mst_edges, cost = prim(example_graph, 'A')
print("Edges in MST:", mst_edges)
print("Total Cost:", cost)
