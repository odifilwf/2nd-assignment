n = int(input())

a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10

if n == a**4 + b**4 + c**4 + d**4:
    print("Armstrong number")

