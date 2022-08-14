#Function Defination , add two number based on user input 
def fnSum():
     print("Please provide first number here")
     number1 =int(input())
     
     print("Please provid second number here")
     number2 =int(input())
     
     sum = number1 + number2
     print("The sum of two number is" , sum)
     
#Function Call
print("We will call function here : fnSum()")
fnSum()