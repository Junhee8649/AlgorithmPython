def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    amount = len(score)
    if amount >= m:
        i = 0
        while (i + m) <= amount:
            answer += score[i+m-1] * m
            i += m
    return answer