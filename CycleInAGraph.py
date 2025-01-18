def dfsFindCycleDirectedGraph(graph, current_vertex, visited, helper, path=[]):
    visited[current_vertex] = True
    helper[current_vertex] = True
    path.append(current_vertex)
    for i in range(1, graph[current_vertex][0] + 1):
        next_vertex = graph[current_vertex][i]
        if not visited[next_vertex]:
            if dfsFindCycleDirectedGraph(graph, next_vertex, visited, helper, path):
                return True
        elif helper[next_vertex]:
            return printTheCycle(path, next_vertex)
    helper[current_vertex] = False
    path.pop()
    return False


def printTheCycle(path, path_start):
    path_start_index = path.index(path_start)
    cycle = path[path_start_index:]
    print(len(cycle))
    print(*cycle)
    return True


vertexes = int(input())
graph = {}
for i in range(1, vertexes + 1):
    graph[i] = list(map(int, input().split()))
helper = [False] * (vertexes + 1)
visited = [False] * (vertexes + 1)
for current_vertex in graph.keys():
    if not visited[current_vertex]:
        isCycleInTheGraph = dfsFindCycleDirectedGraph(graph, current_vertex, visited, helper)
        if isCycleInTheGraph:
            break
if not isCycleInTheGraph:
    print("neni")