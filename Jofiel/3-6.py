nums = sorted(list(map(int, input().split())))
repeated = []
temp = None

for num in nums:
    if temp is not None:
        if temp == num and num not in repeated:
            repeated.append(num)
    temp = num

print(*repeated)
