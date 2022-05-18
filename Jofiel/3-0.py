s = input()
chars = [" ", ",", "."]

for char in chars:
    if char in s:
        words = s.split(char)
        break

print(len(words))
