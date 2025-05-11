# 이항계수 nCr
# nCr = n! / (r! * (n - r)!)
# bino(n,0) = 1
# bino(n,1) = n
# bino(n,n) = 1
# bino(n, r) = n! / (r! * (n - r)!)
# https://www.acmicpc.net/problem/11051
# 문제
# 자연수 
# \(N\)과 정수 
# \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 
# \(N\)과 
# \(K\)가 주어진다. (1 ≤ 
# \(N\) ≤ 1,000, 0 ≤ 
# \(K\) ≤ 
# \(N\))

# 출력
 
# \(\binom{N}{K}\)를 10,007로 나눈 나머지를 출력한다.

# 예제 입력 1 
# 5 2
# 예제 출력 1 
# 10

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7) # 재귀 깊이 제한 늘리기

# 일단 단순하게 재귀로 구현
# 1000 500 넣으면 시간초과
# MOD = 10007
# N,K = map(int, input().split())
# def bino(n,k):
#     if k == 0 or n == k:
#         return 1
#     return bino(n-1,k-1) + bino(n-1,k)
# print(bino(N,K))

# 메모이제이션을 이용한 재귀
# MOD = 10007
# N,K = map(int, input().split())
# cache = [[0] * 1001 for _ in range(1001)]
# def bino(n,k):
#   if cache[n][k] != 0:
#     return cache[n][k]
#   if k == 0 or n == k:
#     return 1
#   cache[n][k] = (bino(n-1,k-1) + bino(n-1,k)) % MOD
#   return cache[n][k]
# print(bino(N,K))

# 반복문을 이용한 DP
MOD = 10007
N,K = map(int, input().split())
cache = [[0] * 1001 for _ in range(1001)]
for i in range(1001):
    cache[i][0] = 1
    cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= MOD
print(cache[N][K])