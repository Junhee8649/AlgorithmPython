def solution(want, number, discount):
    answer = 0

    for i in range(len(discount) - 9):
        temp = discount[i:i+10]
        isbuy = True
        for j in range(len(want)):
            if temp.count(want[j]) != number[j]:
                isbuy = False
                break
        if isbuy:
            answer += 1
    return answer