from itertools import product

def solution(numbers, target):
    choices = [(x, -x) for x in numbers]
    all_combinations = list(product(*choices))
    answer = list(map(sum, all_combinations)).count(target)
    return answer