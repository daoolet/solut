from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(target_node):
    search_queue = deque()
    search_queue += graph['A']
    searched = []

    while search_queue:
        current_node = search_queue.popleft()
        if not current_node in searched:
            if current_node == target_node:
                print("Found!")
                return True
            else:
                search_queue += graph[current_node]
                searched.append(current_node)
    
    return False

print(bfs('F'))



