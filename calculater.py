print("let's do some math")

x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))

operetion = input("Please enter the operation (+, -, *, /): ")


if operetion == "+":
    print(f"The result of adding {x} and {y} is:", x + y)
elif operetion == "-":
    print(f"The result of subtracting {x} from {y} is:", y - x)
elif operetion == "*":
    print(f"The result of multiplying {x} and {y} is:", x * y)
elif operetion == "/":
    print(f"The result of dividing {x} by {y} is:", x / y)
else:
    print("Invalid operation")

print("End of program")

#--------------------------------------------------------------- 

print("let's try eval function")

x = eval(input("Enter the mathmatic opreation you want to do: "))
print("The result is:", x)

print("End of program")

#---------------------------------------------------------------

print(f"the result is {eval(input('Enter the mathmatic opreation you want to do: '))}")

