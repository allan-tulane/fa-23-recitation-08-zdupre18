from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
       """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    distances = {vertex: [float('inf'), float('inf')] for vertex in graph}
    distances[source] = [0, 0]
    min_heap = [(0, 0, source)]  # (distance, number of edges, vertex)
    
    while min_heap:
        curr_dist, curr_edges, curr_vertex = heapq.heappop(min_heap)
        
        if [curr_dist, curr_edges] > distances[curr_vertex]:
            continue
        
        for neighbor, weight in graph[curr_vertex]:
            new_dist = curr_dist + weight
            new_edges = curr_edges + 1
            
            if [new_dist, new_edges] < distances[neighbor]:
                distances[neighbor] = [new_dist, new_edges]
                heapq.heappush(min_heap, (new_dist, new_edges, neighbor))
    
    return distances

    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    visited = {vertex: False for vertex in graph}
    parent = {vertex: None for vertex in graph}
    queue = deque([source])
    visited[source] = True

    while queue:
        current_vertex = queue.popleft()

        for neighbor in graph[current_vertex]:
            if not visited[neighbor] and neighbor != source:
                visited[neighbor] = True
                queue.append(neighbor)
                parent[neighbor] = current_vertex

    return parent


def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
    while destination is not None:
        path.append(destination)
        destination = parents[destination]
    return list(reversed(path[:-1])) if path else None


