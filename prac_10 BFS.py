from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            neighbors = graph[vertex]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    "1": ['2', '3'],
    "2": ['1', '4', '6'],
    "3": ['1', '5'],
    "4": ['2'],
    "5": ['3'],
    "6": ['2']
}

start_vertex = "1"
bfs(graph, start_vertex)
