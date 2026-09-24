def cafe_calculator(a, operator, b):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return round(a / b, 2)

    elif operator == "%":
        if b == 0:
            return "Cannot divide by zero"
        return a % b

    elif operator == "**":
        return a ** b

    else:
        return "Invalid operator"


print(cafe_calculator(10, "+", 5))
print(cafe_calculator(10, "-", 3))
print(cafe_calculator(10, "*", 4))
print(cafe_calculator(10, "/", 3))
print(cafe_calculator(10, "%", 3))
print(cafe_calculator(2, "**", 3))