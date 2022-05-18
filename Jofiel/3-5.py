nums = list(map(int, input().split()))
n = len(nums)

if n == 1:
    result = nums
else:
    result = [nums[(i-1) % n]+nums[(i+1) % n] for i in range(n)]

print(*result)
