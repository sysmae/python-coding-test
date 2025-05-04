# https://www.acmicpc.net/problem/9012

# 스택을 활용해서 괄호의 짝을 맞추는 문제
# 스택에 여는 괄호를 넣고 닫는 괄호가 나올 때마다 스택에서 pop을 한다.

# from sys import stdin as s
# s=open("input.txt","rt")

# n = int(s.readline())

# for i in range(n):
#     input = s.readline()
#     stack =[]
#     for j in input:
#         if j == "(":
#             stack.append(j)
#         elif j ==")":
#             if stack:
#                 stack.pop()
#             else:
#                 print("NO")
#                 break
#     else:
#         if not stack:
#             print("YES")
#         else:
#             print("NO")

for _ in range(int(input())):
    stack = []
    isVps= True
    for ch in input():
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                isVps = False
                break

    if len(stack):
        isVps = False
    print("YES" if isVps else "NO")