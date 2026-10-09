h = int(input())
m = int(input())

if (h >= 0 and h < 24) and (m >= 0 and m < 60):
    print("Valid time")
else:
    print("Invalid time")