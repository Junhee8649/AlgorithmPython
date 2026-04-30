def solution(n):
    temp = n + 1
    while temp <= 1000000:
        if bin(n).count('1') == bin(temp).count('1'):
            return temp
        temp += 1
print(solution(78))