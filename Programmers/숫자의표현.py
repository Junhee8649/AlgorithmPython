def solution(n):
    count = 0
    for i in range(1,n+1):
        temp = i
        if temp == n:
            count += 1
            break
        for j in range(i+1, n+1):
            temp += j
            if temp > n:
                break
            elif temp == n:
                count += 1
                break

    return count