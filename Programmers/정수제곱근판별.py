from math import sqrt


def solution(n):
    temp = sqrt(n)
    if temp == int(temp):
        return (temp + 1) * (temp + 1)
    else:
        return -1