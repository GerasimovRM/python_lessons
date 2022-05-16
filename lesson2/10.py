# int float bool
x = float(input())
if x < 0:
    print(x ** 2)
else:
    if 0 <= x <= 1:
        print(0)
    else:
        print(x - 1)
