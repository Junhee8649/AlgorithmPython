def solution(s):
    answer = ""
    s_split = s.split(" ")
    
    for word in range(len(s_split)):
        if s_split[word] == "":
            pass 
        else:
            if s_split[word][0].isdigit():
                answer += s_split[word][0] 
            elif s_split[word][0] == s_split[word][0].lower():
                answer += s_split[word][0].upper()
            elif s_split[word][0] == s_split[word][0].upper():
                answer += s_split[word][0]
            answer += s_split[word][1:].lower()
        
        if word < len(s_split) - 1:
            answer += " "
            
    return answer