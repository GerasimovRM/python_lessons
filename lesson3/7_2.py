# "abcd" -> abbcccdddd
st = input()
result = ""
for i in range(len(st)):
    result += st[i] * (i + 1)
print(result)
