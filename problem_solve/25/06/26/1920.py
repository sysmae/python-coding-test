# https://www.acmicpc.net/problem/1920
# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# 예제 입력 1 
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
# 예제 출력 1 
# 1
# 1
# 0
# 0
# 1

# import inspect
# import bisect

# print(inspect.getsource(bisect))

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
M = int(input())
targets = list(map(int,input().split()))

nums.sort() 

def search(st, en, target):
    if st == en:
        if nums[st] == target:
            print(1)
        else:
            print(0)
        return
    mid = (st+en) //2
    if nums[mid] < target:
        search(mid+1,en,target)
    else:
        search(st,mid,target)

for target in targets:
    # 이진 탐색을 사용하여 target이 nums에 있는지 확인
    search(0, N-1, target)