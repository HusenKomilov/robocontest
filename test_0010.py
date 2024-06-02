n = int(input())

a, b, c = map(int, input().split())

if a+b+c < n:
    print("No")
elif a+b+c > n:
    print("Yes")
