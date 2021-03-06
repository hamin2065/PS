# https://www.acmicpc.net/problem/2579
# 계단 오르기

from sys import stdin
n = int(input())
stairs = [0] * 301
for i in range(n) : 
    stairs[i] = int(stdin.readline().strip())
dp = [0] * 301

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])

for i in range(3, n):
    # 마지막 전의 계단을 밟은 경우, 마지막 전의 계단을 밟지 않은 경우
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
    
print(dp[n-1])