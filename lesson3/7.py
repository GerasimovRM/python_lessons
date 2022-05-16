# "abcd" -> abbcccdddd
st = input()
for i in range(len(st)):
    print(st[i] * (i + 1), end="")
