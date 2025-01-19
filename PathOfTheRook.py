from collections import deque

def bfsRook(checkboard, starting_point):
    queue = deque([starting_point])
    directions =[(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x_now, y_now = queue.popleft()
        for dr in directions:
            dr_x, dr_y = dr
            x_next = x_now + dr_x
            y_next = y_now + dr_y
            while (0 <= x_next < 8) and (0 <= y_next < 8) and (checkboard[x_next][y_next] != -2):
                if checkboard[x_next][y_next] == -1:
                    queue.append((x_next, y_next))
                    checkboard[x_next][y_next] = checkboard[x_now][y_now] + 1
                x_next += dr_x
                y_next += dr_y
    return checkboard

def readCheckboard(): 
# '.' - a free square
#'x' - an occupied square
#'v' - the starting position of the rook
#'c' - the ending position of the rook
    checkboard = []
    for i in range(8):
        line = input()
        checkboard.append([])
        for j in range(8):
            if line[j] == '.':
                checkboard[i].append(-1)
            elif line[j] == 'c':
                finish_point = (i, j)
                checkboard[i].append(-1)
            elif line[j] == 'x':
                checkboard[i].append(-2)
            elif line[j] == 'v':
                starting_point = (i, j)
                checkboard[i].append(0)
    return starting_point, finish_point, checkboard


starting_point, finish_point, checkboard = readCheckboard()
x_fin, y_fin = finish_point
bfsRook(checkboard, starting_point)
print(checkboard[x_fin][y_fin])