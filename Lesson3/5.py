znak = input()
first = int(input())
second = int(input())
c = 0
if znak == "+":
    c = first+second
elif znak == "-":
    c = first-second
elif znak == "/":
    c = first/second
elif znak == "*":
    c = first*second
else:
    print("znak not found")
print(f"Ваш Ответ:{c}")