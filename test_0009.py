n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(1)
else:
    for i in arr:
        if arr.count(i) < 2:
            print(i)
