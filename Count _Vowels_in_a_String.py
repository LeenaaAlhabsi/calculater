print("welcome to the Vowel Counter App") #start of the program

program = True
while program:
   input_string = input("\nEnter a word or phrase: ")#get the input string from the user
   if input_string == "": #check if the input string is empty
    print("\nPlease enter a non-empty string") #print a message to the user
    print("Try again!") #print a message to the user
   else:
    input_string1 = input_string.lower() #convert the input string to lowercase
    program = False

vowels = ['a', 'e', 'i', 'o', 'u'] #list of vowels
vowels_count = 0 #variable to count the vowels

for char in input_string1: #loop to count the vowels in the input string
    if char in vowels: #check if the character is a vowel, char is the character in the input string
        vowels_count += 1 #increment the count of vowels

print(f"\nThe number of vowels in {input_string} is {vowels_count}.") #the result of the program
print("\nGoodbye!") #end of the program


