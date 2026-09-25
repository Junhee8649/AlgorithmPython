def solution(num_list):
    holl, jjak = 0, 0
    for num in num_list:
        if num % 2 == 0:
            jjak += 1
        else:
            holl += 1
    return [jjak, holl]