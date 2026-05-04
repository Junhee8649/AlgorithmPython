def solution(n, lost, reserve):
    temp = 0
    temp_set = set()
    for i in lost:
        for j in reserve:
            if i == j:
                temp_set.add(i)
    for i in temp_set:
        lost.remove(i)
        reserve.remove(i)
    lost.sort()
    reserve.sort()
    for i in lost:
        for j in reserve:
            if j == (i-1) or j == (i+1):
                reserve.remove(j)
                temp += 1
                break
    return n-(len(lost)-temp)