plus, minus = map(int, input().split())
big = (plus + minus) // 2
small = plus - big
if big + small == plus and big - small == minus and big >= 0 and small >= 0:
    print(big, small)
else:
    print(-1)