def binary_search(arr, item):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        gues = arr[mid]
        if gues <= item:
            low = mid + 1
        else:
            high = mid
    return low


n = int(input())

nl = list(map(int, input().split(" ")))
nl.sort()
m = int(input())

for _ in range(m):
    i = int(input())
    x = binary_search(nl, i)
    print(x)
