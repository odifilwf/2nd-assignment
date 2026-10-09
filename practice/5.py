x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1 Quadrant")
elif x < 0 and y > 0:
    print("2 Quadrant")
elif x < 0 and y < 0:
    print("3 Quadrant")
else:
    print("4 Quadrant")