# N x N 격자와 M번의 택배 위치 정보
N, M = map(int, input().split())
# 택배 번호 k번, 세로 크기 h, 가로 크기 w, 좌측 좌표 c
parcels_location = [list(map(int, input().split())) for _ in range(M)]
grid = [[0] * N for _ in range(N)]


def insert(k, h, w, c):
    for i in range(h):
        for j in range(c - 1, c - 1 + w):
            grid[i][j] = k


# 덩어리 중력 패턴!!
def gravity():
    # 격자 안에 있는 택배 번호들을 모두 찾기
    parcels = set()
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                parcels.add(grid[i][j])

    # 바닥에 가까운(i가 큰) 택배부터 내리기 위해 정렬
    bottoms = []
    for k in parcels:
        max_i = -1
        for i in range(N):
            for j in range(N):
                if grid[i][j] == k:
                    max_i = max(max_i, i)
        # i번째 칸이 k번 택배 최하단
        bottoms.append((max_i, k))

    bottoms.sort(reverse=True)  # 아래에 있는 택배부터 처리

    # 덩어리째 아래로 내리기
    for _, k in bottoms:
        while True:
            can_move = True
            # 더 내릴 수 있는지 확인
            for i in range(N):
                for j in range(N):
                    if grid[i][j] == k:
                        # 바닥에 닿았거나, 바로 아래에 다른 택배가 있으면 멈춤
                        if i == N - 1 or (grid[i + 1][j] != 0 and grid[i + 1][j] != k):
                            can_move = False

            if not can_move:
                break

            # 한 칸씩 통째로 내리기 (덮어쓰지 않도록 밑에서부터 위로 탐색)
            for i in range(N - 1, -1, -1):
                for j in range(N):
                    if grid[i][j] == k:
                        grid[i + 1][j] = k
                        grid[i][j] = 0


# 2. 좌측 하차 조건 꼼꼼하게 수정
def left_pull():
    temp = set()
    # 모든 0이 아닌 번호에 대해 뺄 수 있는지 검사
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                temp.add(grid[i][j])

    pullable_list = []
    for k in temp:
        can_pull = True
        for i in range(N):
            for j in range(N):
                if grid[i][j] == k:
                    # 내 왼쪽(0 ~ j-1 칸)에 나랑 다른 택배가 하나라도 있으면 못 뺌
                    for c in range(j):
                        if grid[i][c] != 0 and grid[i][c] != k:
                            can_pull = False
        if can_pull:
            pullable_list.append(k)

    # 작성해주신 로직 그대로 활용 (정렬 후 첫 번째 값)
    pullable_list = sorted(pullable_list)
    delete_num = pullable_list[0]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == delete_num:
                grid[i][j] = 0
    print(delete_num)


# 2. 우측 하차 조건 꼼꼼하게 수정
def right_pull():
    temp = set()
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                temp.add(grid[i][j])

    pullable_list = []
    for k in temp:
        can_pull = True
        for i in range(N):
            for j in range(N):
                if grid[i][j] == k:
                    # 내 오른쪽(j+1 ~ N-1 칸)에 나랑 다른 택배가 하나라도 있으면 못 뺌
                    for c in range(j + 1, N):
                        if grid[i][c] != 0 and grid[i][c] != k:
                            can_pull = False
        if can_pull:
            pullable_list.append(k)

    pullable_list = sorted(pullable_list)
    delete_num = pullable_list[0]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == delete_num:
                grid[i][j] = 0
    print(delete_num)


def pull(count):
    if count % 2 == 0:
        left_pull()
    else:
        right_pull()


for parcel in parcels_location:
    k, h, w, c = parcel
    insert(k, h, w, c)
    gravity()

for count in range(M):
    pull(count)
    gravity()
