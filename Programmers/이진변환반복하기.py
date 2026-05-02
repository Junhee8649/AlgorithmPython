def solution(s):
    count, zero_count = 0, 0
    while s != "1":
        temp = ""
        for char in s:
            if char == "1":
                temp += char
            elif char == "0":
                zero_count += 1
        c = len(temp)
        s = str(bin(c))[2:]
        count += 1
    return [count, zero_count]