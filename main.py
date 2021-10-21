def dfc_grafs(v):
    graph = [
        [4],
        [2, 5],
        [1, 5],
        [7],
        [0, 6],
        [1, 2, 6],
        [4, 5],
        [3]
    ]

    visited = [False] * len(graph)
    previous = [None] * len(graph)

    visited[v] = True
    for neighbour in graph[v]:
        if  not visited[neighbour]:
            previous[neighbour] = v
            dfc_grafs(previous)
    return visited, previous
