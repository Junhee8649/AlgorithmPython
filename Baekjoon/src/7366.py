N = int(input())
for i in range(1, N+1):
    num = int(input())
    words = input().split()
    count = words.count("sheep")
    print(f"Case {i}: This list contains {count} sheep.")
    print()