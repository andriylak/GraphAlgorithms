def not_visited_node(visited):                         #finds node that we haven't visited before
    for i in range(1, len(visited)):
        if visited[i] == 0:
            return i


def dfs(graph, visited, node):                         #visits all nodes of component
    global number_of_visited
    number_of_visited += 1
    stack = [node]
    while len(stack) != 0:
        current = stack.pop()
        for element in graph[current]:
            if visited[element] == 0:
                stack.append(element)
                number_of_visited += 1
                visited[element] = visited[node]

def initializationOfDictionary(limit):
    dictionary = {}
    for j in range(1, limit + 1):
        dictionary[j] = []
    return dictionary

def readEdges(graph, edges):
    for i in range(edges):
        begin, end = map(int, input().split())
        graph[begin].append(end)
        graph[end].append(begin)

# input
nodes = int(input())
edges = int(input())

# initialization
graph = initializationOfDictionary(nodes)
readEdges(graph, edges)
number_of_visited = 0
colour_of_component = 0
visited = [0] * (nodes + 1)

# find components
while number_of_visited < nodes:
    colour_of_component += 1
    node = not_visited_node(visited)
    visited[node] = colour_of_component
    dfs(graph, visited, node)

# output
list_of_components = initializationOfDictionary(colour_of_component)
for i in range(1, nodes + 1):
    list_of_components[visited[i]].append(i)
for component in list_of_components.values():
    print(*component)