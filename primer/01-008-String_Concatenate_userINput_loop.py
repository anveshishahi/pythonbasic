#loop

print("Please enter name which you want to print")
name = input()
print("Please enter last name")
Lastname = input()

Fullname = name +" " +Lastname

print("Please enter the number of how many times you want to print the data")
numberofprint = int(input())

#range on userinput
for i in range (numberofprint):
    print(Fullname , i+1)