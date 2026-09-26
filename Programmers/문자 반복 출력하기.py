def solution(my_string, n):
    answer = ''
    
    for s in my_string:
        answer += (n * s)
    
    return answer