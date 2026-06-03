dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(dirs):
    y, x = 0, 0
    temp = set()
    for dir in dirs:
        if dir == 'U':
            ny, nx = y + dy[0], x + dx[0]
        elif dir == 'R':
            ny, nx = y + dy[1], x + dx[1]
        elif dir == 'D':
            ny, nx = y + dy[2], x + dx[2]
        elif dir == 'L':
            ny, nx = y + dy[3], x + dx[3]
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            temp.add((x, y, nx, ny))
            temp.add((nx, ny, x, y))
            y, x = ny, nx
    return len(temp) // 2