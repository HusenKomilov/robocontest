n = int(input())
nums = list(map(int, input().split()))

if len(nums) == n:
    mx = max(nums)
    idx = nums.index(mx)
    nums.pop(idx)
    print(max(nums))