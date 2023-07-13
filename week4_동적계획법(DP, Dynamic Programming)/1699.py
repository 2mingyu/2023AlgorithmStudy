"""
1: 1 (1)
2: 2 (1+1)
3: 3 (1+1+1)
4: 1 (4)
5: 2 (4+1)
6: 3 (4+1+1)
7: 4 (4+1+1)
8: 2 (4+4)
9: 1 (9)
10: 2 (9+1)
11: 3 (9+1+1)
12: 3 (4+4+4) ..(9+1+1+1)이 아니다!
13: 2 (9+4)
14: 3 (9+4+1)
15: 4 (9+4+1+1)
16: 1 (16)
dp[N] = 자연수 N을 제곱수들의 합으로 표현할 때에 그 항의 최소 개수
dp[12]를 구하는 법?
check 1 -> dp[1] + dp[11] = 4
check 2 -> dp[4] + dp[8] = 3
check 3 -> dp[9] + dp[3] = 4
check 4 -> 16>12 이므로 break
위의 4,3,4 중에 min 구하기
"""

N = int(input())
dp=[N] * (N + 1)    # dp[N] = 자연수 N을 제곱수들의 합으로 표현할 때에 그 항의 최소 개수
dp[0] = 0
for i in range(1, N+1):
    for j in range(1, i+1):
        jj = j * j
        if jj > i:
            break
        if dp[i-jj] + 1 < dp[i]:
            dp[i] = dp[i-jj] + 1
print(dp[N])
