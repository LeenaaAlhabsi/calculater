print("\nWelcome to the Pattern Printer\n")
#validate user input
program = True
while program:
    user_input = input("Enter the number of rows you want to print: ")
    
    if user_input.isdigit():
        if int(user_input) > 0:
            user_input = int(user_input)
            print("\n")
            program = False
    else:
        print("Please enter a valid number\n")
#pattern of increasing numbers
print("pattern of increasing numbers:")
for line in range(user_input):
    for number in range(line+1):
        print(number+1, end=" ")
    print()
#pattern of increasing stars
print("\npattern of increasing stars:")
for line in range(user_input):
    for star in range(line+1):
        print("*", end=" ")
    print()
#pattern for full triangle
user_input1 = input("\nDo you to complete the pattern into a full triangle(y/n): ")
if user_input1 == "y":
    print("\nFull triangle pattern:")
    for line in range(user_input):
        for space in range(user_input - line - 1): #input 3 -> 3-0-1 (line start from 0)
            print(" ",end=" ")
        for star in range(2 * line + 1): #
            print("*",end=" ")
        print()
else:
    print("Thank you for using the Pattern Printer")
#end of program
print("\nThank you for using the Pattern Printer")


