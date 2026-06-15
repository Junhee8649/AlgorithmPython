def solution(x):
    answer = True
    temp = str(x)
    new_x = 0
    for i in temp:
        new_x += int(i)
    if x % new_x != 0:
        answer = False
    return answer