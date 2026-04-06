def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


x = int(input())
for _ in range(x):
    k = int(input())
    print(fibonacci(k + 1))
