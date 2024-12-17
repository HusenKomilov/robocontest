def solve(n: int, k: int) -> int:
    c = k // n
    d = k - (c * n)
    return d


n, k = map(int, input().split())
print(solve(n, k))
