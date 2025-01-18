from collections import deque


def DFS(graph):                                         # dfs implementation on graph
    stack = [0]   
    visited = len(graph)*[False]
    visited[0] = True
    while len(stack) > 0:
        current_node = stack.pop()
        print(current_node)
        for node in graph[current_node]:
            if visited[node] == False:
                stack.append(node)
                visited[node] = True

def BipartGraph(graph):                                  # checks whether the graph is bipartite 
    stack = [0]  
    colour = [-1]*len(graph)
    colour[0] = 0
    while len(stack) > 0:
        current_node = stack.pop()
        for node in graph[current_node]:
            if colour[node] == -1:
                stack.append(node)
                if current_node == 1:
                    colour[node] = 0
                else:
                    colour[node] = 1
            else:
                if colour[current_node] == colour[node]:
                    return False
    return True


def BFS(graph):                                           # bfs implementation on graph
    queue = deque([0])
    visited = len(graph)*[False]
    visited[0] = True
    while len(queue) > 0:
        current_node = queue.popleft()
        print(current_node)
        for node in graph[current_node]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True
                

graph =[ [1],  # 0
    [2],  # 1
    [3],
    [0]
]
print(BipartGraph(graph))