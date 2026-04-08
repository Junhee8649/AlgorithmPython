from collections import deque

# N x N과 day일
N, day = map(int, input().split())
# 음식 배열, T 민트, C 초코, M 우유
F_grid = [[""] * N for _ in range(N)]
for i in range(N):
    foods = input()
    for j in range(N):
        F_grid[i][j] = foods[j]
# 신앙심 원본 배열
B_grid = [list(map(int, input().split())) for _ in range(N)]
# 북 남 서 동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def morning():
    for i in range(N):
        for j in range(N):
            B_grid[i][j] += 1


def lunch_group_make():
    visited = [[False] * N for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                group = [[i, j]]
                # 탐색하려는 음식
                food = F_grid[i][j]
                q.append((i, j))
                visited[i][j] = True
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if (
                            0 <= nr < N
                            and 0 <= nc < N
                            and not visited[nr][nc]
                            and F_grid[nr][nc] == food
                        ):
                            visited[nr][nc] = True
                            group.append([nr, nc])
                            q.append((nr, nc))
                groups.append(group)


def lunch_owner_select():
    for group in groups:
        temp_group = []
        for person in group:
            tr, tc = person
            temp_group.append((B_grid[tr][tc], tr, tc))
        temp_group.sort(key=lambda x: (-x[0], x[1], x[2]))

        for person in range(len(temp_group)):
            r, c = temp_group[person][1], temp_group[person][2]
            if person == 0:
                B_grid[r][c] += len(temp_group) - 1
            else:
                B_grid[r][c] -= 1
        y, x = temp_group[0][1], temp_group[0][2]
        owners.append([F_grid[y][x], B_grid[y][x], y, x])


def evening():
    # 신앙 전파 순서
    owners.sort(key=lambda x: (len(x[0]), -x[1], x[2], x[3]))
    # 전파 당했는지 확인하는 배열
    owner_grid = [[False] * N for _ in range(N)]
    for owner in owners:
        f, b, r, c = owner
        if not owner_grid[r][c]:
            # x는 간절함, d는 전파 방향
            x, d = b - 1, b % 4
            # 전파자는 1만 남기고 다 간절함으로 바꿈
            B_grid[r][c] = 1
            nr, nc = r + dr[d], c + dc[d]
            while 0 <= nr < N and 0 <= nc < N and x != 0:
                # 전파 대상이 전파자와 신봉 음식이 다른 경우
                if F_grid[nr][nc] != f:
                    y = B_grid[nr][nc]
                    # 강한 전파
                    if x > y:
                        F_grid[nr][nc] = f
                        x -= y + 1
                        B_grid[nr][nc] += 1
                        owner_grid[nr][nc] = True
                        if x == 0:
                            break
                    # 약한 전파
                    else:
                        new_food = list(set(f + F_grid[nr][nc]))
                        new_food.sort()
                        new_food = "".join(new_food)
                        F_grid[nr][nc] = new_food
                        B_grid[nr][nc] += x
                        owner_grid[nr][nc] = True
                        break
                nr, nc = nr + dr[d], nc + dc[d]


def all_b_sum():
    sum_grid = [0] * 7
    for i in range(N):
        for j in range(N):
            if F_grid[i][j] == "CMT":
                sum_grid[0] += B_grid[i][j]
            elif F_grid[i][j] == "CT":
                sum_grid[1] += B_grid[i][j]
            elif F_grid[i][j] == "MT":
                sum_grid[2] += B_grid[i][j]
            elif F_grid[i][j] == "CM":
                sum_grid[3] += B_grid[i][j]
            elif F_grid[i][j] == "M":
                sum_grid[4] += B_grid[i][j]
            elif F_grid[i][j] == "C":
                sum_grid[5] += B_grid[i][j]
            elif F_grid[i][j] == "T":
                sum_grid[6] += B_grid[i][j]
    print(*sum_grid)


for _ in range(day):
    # 그룹들과 각 그룹 인원 좌표 모음, 대표자들의 음식종류(TCM) 신앙심 좌표 모음
    groups, owners = [], []
    morning()
    lunch_group_make()
    lunch_owner_select()
    evening()
    all_b_sum()
