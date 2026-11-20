from collections import defaultdict

def solution(clothes):
    c_dic = defaultdict(list)
    for c in clothes:
        c_dic[c[1]].append(c[0])

    temp = 1
    for k in c_dic:
        temp *= len(c_dic[k]) + 1
    
    return temp - 1