def divisorCount(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            if i * i == num:
                count += 1
            else:
                count += 2
    return count

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if divisorCount(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer