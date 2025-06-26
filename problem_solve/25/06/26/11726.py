# https://www.acmicpc.net/problem/11726
# 문제
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.



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

import sys
input = sys.stdin.readline

# 점화식: dp[n] = dp[n-1] + dp[n-2]

n = int(input())
# rs = [0,1,2]
# for i in range(3, n+1):
#   rs.append(rs[i-1] + rs[i-2])
# print(rs[n] % 10007)

dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n])