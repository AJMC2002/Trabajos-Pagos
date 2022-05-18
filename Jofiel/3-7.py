sum, sum_sq = 0, 0

while True:
    n = int(input())
    sum += n
    sum_sq += n ** 2
    if sum == 0:
        break

print(sum_sq)
