def solution(num):
    if num == 1:
        return 0
    answer = 0
    isFinish = False
    for i in range(500):
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        answer += 1
        if num == 1:
            isFinish = True
            break
    if not isFinish:
        answer = -1
    return answer