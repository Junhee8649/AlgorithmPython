from collections import Counter


def solution(k, tangerine):
    answer = 0
    counts = Counter(tangerine)
    values = list(counts.values())
    values.sort(reverse=True)

    for i in values:
        if k > 0:
            k -= i
            answer += 1
        else:
            break
    return answer