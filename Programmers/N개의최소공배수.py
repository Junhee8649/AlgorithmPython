import math

def solution(arr):
    lcm_val = arr[0]
    for num in arr[1:]:
        # (현재까지의 최소공배수 * 다음 수) / 두 수의 최대공약수
        lcm_val = (lcm_val * num) // math.gcd(lcm_val, num)
    return lcm_val