# to handle the if denominator is 0;
try:
#The code which is writting try block can be occur error at runtime
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))

    c = a/b    #Exception occur on runtime because division by zero

    print("Answer : ",c)

except Exception as e:               #exception class
    #this block will run when exception occur
    print("Exception Caught :",e)         #exception caught


