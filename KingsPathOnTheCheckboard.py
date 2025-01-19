from collections import deque

#finds the shortest path between start_point and finish_point, but it is reversed
#returns dictionary where key is the coordinate of the current node and the value is the coordinate of the previous node from which we got here
def findTheShortestPath(checkboard, start_point, finish_point):        
    queue = deque([])
    previous = {start_point: None}
    queue.append(start_point)
    while len(queue) != 0:
        x_now, y_now = queue.popleft()
        for delta_x in range(-1, 2):
            for delta_y in range(-1, 2):
                next_x, next_y = (x_now + delta_x, y_now + delta_y)
                if not checkboard[next_x][next_y]:
                    upcoming = (next_x, next_y)
                    previous[upcoming] = (x_now, y_now)
                    if upcoming == finish_point:
                        return printTheShortestPath(previous, finish_point)
                    checkboard[next_x][next_y] = True
                    queue.append(upcoming)
    print(-1)

#printing the path from start_point to finish_point
def printTheShortestPath(previous, finish_point):
    path = [finish_point]
    while previous[path[-1]] != None:
        path.append(previous[path[-1]])
    for coordinate in reversed(path):
        print(' '.join(map(str, coordinate)))
  

#Initialization of checkboard
def buildCheckboard(obstacles, start_point):
    checkboard = []
    checkboard.append([True] * 10)
    for i in range(1, 9):
        checkboard.append([])
        checkboard[i].append(True)
        for j in range(1, 9):
            checkboard[i].append(False)
        checkboard[i].append(True)
    checkboard.append([True] * 10)
    for x, y in obstacles:
        checkboard[x][y] = True
    checkboard[start_point[0]][start_point[1]] = True
    return checkboard

#reading data
def readCoordinates():
    return tuple(map(int, input().split()))

if __name__ == "__main__":
    number_of_obstacles = int(input())
    obstacles = []
    for i in range(number_of_obstacles):
        obstacles.append(readCoordinates())
    start_point = readCoordinates()
    finish_point = readCoordinates()
    checkboard = buildCheckboard(obstacles, start_point)
    findTheShortestPath(checkboard, start_point, finish_point)


