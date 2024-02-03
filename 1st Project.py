 first, sec=float(input("Enter first number => "))
sec=float(input("Enter sec number =>"))
opr = str(input("Enter operation (+, -, *, /) => "))
if opr == "+":
    total = first + sec
elif opr == "_" "*" "/":
    total =first - sec,first * sec, first / sec
else:
    total = str("Please Enter a Valid operation")
print (total)
