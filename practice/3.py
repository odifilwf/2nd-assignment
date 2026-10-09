a = int(input())
b = int(input())
c = int(input())

if a > b and b > c:
    print(f'Maximum = {a}')
    print(f'Minimum = {c}')
    print(f'Medium = {b}')
elif a > b and a > c and c > b:
    print(f'Maximum = {a}')
    print(f'Minimum = {b}')
    print(f'Medium = {c}')
elif b > a and b > c and c > a:
    print(f'Maximum = {b}')
    print(f'Minimum = {a}')
    print(f'Medium = {c}')
elif b > a and a > c:
    print(f'Maximum = {b}')
    print(f'Minimum = {c}')
    print(f'Medium = {a}')
elif c > b and b > a:
    print(f'Maximum = {c}')
    print(f'Minimum = {a}')
    print(f'Medium = {b}')
else:
    print(f'Maximum = {c}')
    print(f'Minimum = {b}')
    print(f'Medium = {a}')