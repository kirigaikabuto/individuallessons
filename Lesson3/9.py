a = int(input())
b = int(input())
c = int(input())
d = int(input())
maximum = 0
minimum = 0
if a > b and a > c:
    maximum = a
elif b > a and b > c:
    maximum = b
else:
    maximum = c

if a < b and a < c:
    minimum = a
elif b < a and b < c:
    minimum = b
else:
    minimum = c


status = ""
status_chet = ""
if d == maximum:
    status = "максимальное"
else:
    status = "минимальное"

if d%2==0:
    status_chet = "четное"
else:
    status_chet = "не четное"

output = f"{d} {status} {status_chet}"
print(output)
