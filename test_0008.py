def solve(n: List[int]) -> List[int]:
    a = sum(n) - max(n)
    b = sum(n[::-1]) - min(n)
    return (a, b)


n = list(map(int, input().split()))
solve(n)[0]
solve(n)[1]
