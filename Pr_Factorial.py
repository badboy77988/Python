num = int(input("Enter the number: "))
factorial = 1

if num<0:
    print("Sorry, Factorial does not exist for negative numbers.")
elif num==0:
    print("Factorial of 0 is 1.")
else:
    for a in range(1,num+1):
        factorial = factorial*a
    print("The factorial of",num,"is:",factorial)