def solution(s):
    answer = ''
    word_index = 0 # 단어별 인덱스를 카운트할 변수
    
    for char in s:
        if char == ' ':
            answer += ' '
            word_index = 0 # 공백을 만나면 인덱스 초기화
        else:
            if word_index % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()
            word_index += 1 # 공백이 아닐 때만 인덱스 증가
            
    return answer