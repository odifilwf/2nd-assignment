k = int(input())

if k % 3 == 0 or k % 5 == 0 or (k > 7 and (k % 3 == 1 or k % 3 == 2)):
  print("YES")
else:
  print("NO")