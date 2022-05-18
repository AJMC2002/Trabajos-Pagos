a, b = int(input()), int(input())
factors = [x for x in range(a, b+1) if x % 3 == 0]
result = sum(factors)/len(factors)
print(result)
