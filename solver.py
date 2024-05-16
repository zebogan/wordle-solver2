from collections import Counter

f = open("words.txt")
lines = f.readlines()
f.close()
fixedlines = []

for line in lines:
    fixedlines.append(line.strip())

print(fixedlines)

combined = ''.join(fixedlines)
x = Counter(combined)

print(x)