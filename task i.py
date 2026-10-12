a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and b == 0:
  print("INF")
elif a == 0 or b % a != 0:
  print("NO")
else:
  x = -b // a
  # Check that the denominator is not zero at this root
  if c * x + d == 0:
    print("NO")
  else:
    print(x)