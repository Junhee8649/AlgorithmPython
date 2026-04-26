def solution(s):
    s = s.split()
    nums = []
    for i in s:
        if '-' in i:
            nums.append(-int(i[1:]))
        else:
            nums.append(int(i))
    max_num, min_num = max(nums), min(nums)
    answer = f"{min_num} {max_num}"
    return answer