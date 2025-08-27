num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter the operator: ")

if operator == "+":
    print(f"{num1} + {num2} = {num1+num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1-num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1*num2}")
elif operator == "/":
    if (num2 != 0):
        print(f"{num1} / {num2} = {num1/num2}")
    else:
        print("ERROR! DIVISION BY ZERO IS NOT POSSIBEL!")
elif operator == "%":
    print(f"{num1} % {num2} = {num1%num2}")