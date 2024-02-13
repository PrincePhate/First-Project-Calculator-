first = float(input("Enter first number => "))
sec = float(input("Enter first number => "))
opr = str(input("Enter operation (+, -, *, /) => "))

if opr == "+":
    total = first + sec
elif opr == "_":
    total = first - sec
elif opr == "*":
    total = first * sec
elif opr == "/":
    total = first / sec
else:
    total = str("Please Enter a Valid operation")
print (total)