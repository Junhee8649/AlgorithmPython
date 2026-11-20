def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    while True:
        temp_set = set()

        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '_':
                    temp_set.update([(i, j), (i, j+1), (i+1, j), (i+1, j+1)])

        if not temp_set:
            break

        answer += len(temp_set)
        for r, c in temp_set:
            board[r][c] = '_'

        for c in range(n):
            temp_c = []
            for r in range(m-1, -1, -1):
                if board[r][c] != '_':
                    temp_c.append(board[r][c])
            for r in range(m):
                if r < len(temp_c):
                    board[m-r-1][c] = temp_c[r]
                else:
                    board[m-r-1][c] = '_'

    return answer