# https://www.acmicpc.net/problem/11726
# 문제
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.
# https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11726/1.png
# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

# 출력
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

# 예제 입력 1 
# 2
# 예제 출력 1 
# 2

# 예제 입력 2 
# 9
# 예제 출력 2 
# 55

# 맨 오른쪽에 세로 1개 놓거나 가로 2개 놓거나 이 두가지로 나눠서 생각
# 이를 재귀로 생각 f(n) = f(n-1) + f(n-2) 즉 점화식이 우연히 피보나치 수열과 같다.
# f(1) = 1
# f(2) = 2
# f(3) = 3
# f(4) = 5
# f(5) = 8
# f(6) = 13
# f(7) = 21
# f(8) = 34
# f(9) = 55

import sys
input = sys.stdin.readline
dp = [0] * (1001)
n = int(input())
MOD = 10007
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1): # O(n)
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
print(dp[n])