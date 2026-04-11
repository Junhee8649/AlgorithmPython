m, a, b = map(int, input().split())
while (m,a,b) != (0,0,0):
    a = m / a
    b = m / b
    time = a*60*60 - b*60*60
    hour = int(time // 3600)
    time %= 3600
    minute = int(time // 60) 
    sec = round(time % 60)
    if minute < 10:
        minute = "0" + str(minute)
    if sec < 10:
        sec = "0" + str(sec)
    print(f"{hour}:{minute}:{sec}")
    m, a, b = map(int, input().split())