def solution(s):
    answer = [-1]
    for i in range(1, len(s)):
        find = s[i]
        count = 0
        is_same = False
        for j in range(i-1, -1, -1):
            count += 1
            if find == s[j]:
                answer.append(count)
                is_same = True
                break
        if not is_same:
            answer.append(-1)
    return answer