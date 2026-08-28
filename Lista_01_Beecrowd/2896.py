T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    total = (N // K) + (N % K)
    print(total)