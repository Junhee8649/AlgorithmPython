from collections import deque

# 탐사 횟수 K, 벽면 유물 조각 개수 M
K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)]
wall_num = list(map(int, input().split()))
wall_count = 0
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
angle = [90, 180, 270]


# r, c는 부분 배열 좌측 상단 좌표고 angle은 90 180 270 l은 부분 배열 길이인데 이 문제는 3 고정이라 l을 파라미터로 안받음
# 이 배열 회전 테크닉은 꼭 암기하도록 하자
def rotate_grid(current_grid, r, c, angle):
    l = 3
    sub_grid = [row[c : c + l] for row in current_grid[r : r + l]]

    k = angle // 90
    for _ in range(k):
        sub_grid = list(map(list, zip(*sub_grid[::-1])))
    for i in range(l):
        for j in range(l):
            current_grid[r + i][c + j] = sub_grid[i][j]
    return current_grid


def find_artifact(current_grid):
    groups = []
    visited = [[False] * 5 for _ in range(5)]
    q = deque()
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                group = [[i, j]]
                num = current_grid[i][j]
                visited[i][j] = True
                q.append((i, j))
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if (
                            0 <= nr < 5
                            and 0 <= nc < 5
                            and not visited[nr][nc]
                            and current_grid[nr][nc] == num
                        ):
                            visited[nr][nc] = True
                            group.append([nr, nc])
                            q.append((nr, nc))
                if len(group) >= 3:
                    for a in group:
                        groups.append(a)
    return groups


for _ in range(K):
    rotate_group = []
    for i in range(3):
        for j in range(3):
            for k in angle:
                temp_grid = [row[:] for row in grid]
                temp_grid = rotate_grid(temp_grid, i, j, k)
                groups = find_artifact(temp_grid)
                if groups:
                    rotate_group.append((len(groups), k, i, j))
    if not rotate_group:
        break
    rotate_group.sort(key=lambda x: (-x[0], x[1], x[3], x[2]))
    _, select_angle, r, c = rotate_group[0]

    final_value = 0
    grid = rotate_grid(grid, r, c, select_angle)
    groups = find_artifact(grid)
    while groups:
        final_value += len(groups)
        groups.sort(key=lambda x: (x[1], -x[0]))
        for group in groups:
            r, c = group
            grid[r][c] = wall_num[wall_count]
            wall_count += 1
        groups = find_artifact(grid)
    print(final_value)
