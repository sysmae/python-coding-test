from sys import stdin as s
s=open("input.txt","rt")

n = int(s.readline())

for i in range(n):
    input = s.readline()
    stack =[]
    for j in input:
        if j == "(":
            stack.append(j)
        elif j ==")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
