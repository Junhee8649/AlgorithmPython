def solution(answers):
    answer = []
    one = [1,2,3,4,5] * 2000
    two = [2,1,2,3,2,4,2,5] * 1250
    three = [3,3,1,1,2,2,4,4,5,5] * 1000
    one_count, two_count, three_count = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == one[i]:
            one_count += 1
        if answers[i] == two[i]:
            two_count += 1
        if answers[i] == three[i]:
            three_count += 1
    temp = max(one_count, two_count, three_count)
    if temp == one_count:
        answer.append(1)
    if temp == two_count:
        answer.append(2)
    if temp == three_count:
        answer.append(3)
    answer.sort()
    return answer