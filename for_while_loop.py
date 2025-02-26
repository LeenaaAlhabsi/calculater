# for i in range(10): #collection of numbers from 0 to 9
#     print(i)

#-------------------------------------------

# days: list[str] = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# for index, day in enumerate(days):
#     print(index+1,"-", day)

#-------------------------------------------

# for day in days:
#     print(day)
#-------------------------------------------

# start = 0
# while start < len(days):
#     print(days[start])
#     start += 1

#-------------------------------------------
carater = "*"
for line in range(5):
    for i in range(line+1):
        print(carater, end=" ") #end=" " is used to print the output in the same line
    print()


