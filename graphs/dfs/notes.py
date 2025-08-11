DFS is the idea of going all the way down one path till NULL, coming back out and going with next possible direction/path  

Preorder, inorder and postorder traversals are all a form of DFS ---- >  solutions for 3 Qs ----> arrays < stacks


def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
