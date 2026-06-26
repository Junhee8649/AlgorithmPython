def solution(files):
    answer, temp = [], []
    for file in files:
        for i in range(len(file)):
            if file[i].isdecimal():
                head = file[:i]
                t = i
                break
        for j in range(t, len(file)):
            if not file[j].isdecimal():
                number = file[t:j]
                break
            if j == len(file) - 1:
                number = file[t:]
        temp.append([file, head, number])
    temp.sort(key=lambda x: (x[1].lower(), int(x[2])))
    
    for k in temp:
        answer.append(k[0])
    return answer