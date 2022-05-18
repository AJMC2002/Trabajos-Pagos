a, b, c = int(input()), int(input()), int(input())
p = (a+b+c)/2
result = (p*(p-a)*(p-b)*(p-c))**(1/2)
print(result)
