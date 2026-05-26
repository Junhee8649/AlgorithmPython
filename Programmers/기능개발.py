from collections import deque

def solution(progresses, speeds):
    answer = []
    # 진도와 속도를 짝지어 리스트 형태로 큐에 저장합니다. (튜플은 값을 수정할 수 없으므로 리스트 사용)
    q = deque([[p, s] for p, s in zip(progresses, speeds)])
    
    while q:
        # 1. 하루치 작업 진행 (진도 + 속도)
        for i in range(len(q)):
            q[i][0] += q[i][1]
        
        # 2. 배포 로직: 맨 앞의 기능이 100% 이상인지 확인
        count = 0
        while q and q[0][0] >= 100:
            q.popleft() # 100%가 넘은 기능과 속도를 큐에서 제거
            count += 1  # 배포 개수 증가
        
        # 3. 오늘 배포된 기능이 있다면 정답에 추가
        if count > 0:
            answer.append(count)
            
    return answer