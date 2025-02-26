print("\nWelcome to the Multiplication Table Generator\n")
program = True
while program:
    x = input("Enter the number for which you want to generate the table: ")
    y = input("Enter the range of the table: ")
    if x.isdigit() and y.isdigit() and int(y) > 0:
        x = int(x)
        y = int(y)
        program = False
    else:
        print("Please enter a valid number and the range must be a positiv number\n")

print("\nThe multiplication table for", x, "is: ")
for i in range(1, y+1):
  print(x, "x", i, "=", x*i)

print("\n")
print("Thank you for using the Multiplication Table Generator")
