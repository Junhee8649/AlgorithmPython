def solution(n):
    n = str(n)
    temp = []
    for i in n:
        temp.append(i)
    temp.sort(reverse=True)
    answer = "".join(temp)
    return int(answer)