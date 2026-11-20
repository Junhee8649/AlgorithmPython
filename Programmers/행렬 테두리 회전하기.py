def solution(rows, columns, queries):
    answer, grid = [], []
    for i in range(1, rows+1):
        temp = []
        for j in range(1, columns+1):
            t = columns * (i-1) + j
            temp.append(t)
        grid.append(temp)

    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

        coords = []
        for c in range(y1, y2):
            coords.append((x1, c))
        for r in range(x1, x2):
            coords.append((r, y2))
        for c in range(y2, y1, -1):
            coords.append((x2, c))
        for r in range(x2, x1, -1):
            coords.append((r, y1))

        vals = [grid[r][c] for r, c in coords]
        answer.append(min(vals))
        vals = [vals[-1]] + vals[:-1]
        for i in range(len(coords)):
            r, c = coords[i]     
            grid[r][c] = vals[i]   

    return answer