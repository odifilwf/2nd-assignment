a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < b:
    r1b = a
    r1e = b
else:
    r1b = b
    r1e = a
if c < d:
    r2b = c
    r2e = d
else:
    r2b = d
    r2e = c

if r1e > r2b:
    print("overlapping")
