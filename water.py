from collections import deque

def bfs(vessels, volumes, depth = 0):                                        
    moves =[(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
    queue = deque([volumes])
    visited = {}
    visited[volumes] = 0
    result = {}
    while queue:
        current_state = queue.popleft()
        for vessel in current_state:
            if vessel not in result:
                result[vessel] = visited[current_state]
        for method in moves:
            from_ves, to_ves = method
            if current_state[from_ves] + current_state[to_ves] <= vessels[to_ves]:
                new_state = []
                for i in range(3):
                    if i == from_ves:
                        new_state.append(0)
                    elif i == to_ves:
                        new_state.append(current_state[from_ves] + current_state[to_ves])
                    else:
                        new_state.append(current_state[i])
                new_state = tuple(new_state)
                if new_state not in visited:
                    queue.append(new_state)
                    visited[new_state] = visited[current_state] + 1
    return result

data = list(map(int, input().split()))
vessels = tuple(data[:3])
volume =tuple(data[3:])
possibilities = bfs(vessels, volume)
for key in possibilities.keys():
    print(key, ':', possibilities[key], sep ='', end=' ')

