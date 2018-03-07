num1 = int (input("Your 1st number= "))
operator = input("What you want to do + - * / ")
num2 = int (input("Your 2nd number= "))

if operator == "+":
    answer = num1 + num2
elif operator == "-":
    answer = num1 - num2
elif operator == "*":
    answer = num1 * num2
elif operator == "/":
    answer = num1 / num2
elif operator == "**":
    answer = num1 ** num2

print("Your Answer is " + str(answer))
