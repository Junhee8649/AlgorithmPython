def solution(brown, yellow):
    total_area = brown + yellow
    
    for height in range(3, total_area + 1):
        if total_area % height == 0:
            width = total_area // height
            if width >= height:
                # 내부의 노란색 격자 개수가 맞는지 검증
                if (width - 2) * (height - 2) == yellow:
                    return [width, height]