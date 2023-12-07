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
   def shortest_shortest_path_helper(visited, frontier):
        if len(frontier) == 0:
            return visited
        else:
            # Pick next closest node from heap
            distance_weight, distance_edges, node = heappop(frontier)
            print('visiting', node)
            if node in visited:
                return shortest_shortest_path_helper(visited, frontier)
            else:
                visited[node] = (distance_weight, distance_edges)
                print('...distance_weight=', distance_weight, ' distance_edges', distance_edges)
                for neighbor, weight in graph[node]:
                    heappush(frontier, (distance_weight + weight, distance_edges + 1, neighbor))                
                return shortest_shortest_path_helper(visited, frontier)
        
    frontier = []
    heappush(frontier, (0, 0, source))
    visited = dict()  # store the final shortest paths for each node.
    return shortest_shortest_path_helper(visited, frontier)
    
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    def bfs_path_helper(visited, frontier, parents):
        if len(frontier) == 0:
            return parents
        else:
            node = frontier.popleft()
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    parents[n] = node
                    frontier.append(n)
            return bfs_path_helper(visited, frontier, parents)

    parents = dict()
    frontier = deque()
    frontier.append(source)
    visited = set()
    return bfs_path_helper(visited, frontier, parents)
    ###



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
    if destination in parents:
        return get_path(parents, parents[destination]) + parents[destination]
    else:
        return ''

