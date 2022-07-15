# # fibonacci series of n terms:
# def Fibonacci(terms):
#     n1, n2 = 0, 1
#     count = 0
#     # check if the number of terms is valid or not?
#     if terms <= 0:  # if given terms are negative;
#         print("Please Enter positive integer.")
#     elif terms == 1:
#         print("Fibonacci sequence upto", terms, ":")
#         print(n1)
#     else:
#         print("Fibonacci sequence:")
#         while count < terms:
#             print(n1)
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
#             count = count + 1
#
# terms = int(input("How many terms? "))
# res= Fibonacci(terms)
# print(res)


# ------------------------------------------------------------------------------------

num = int(input("Enter the range of fibonacci series: "))
n1, n2 = 0, 1

def Fibonacci_Series(num, n1, n2):
    print("Fibonacci series of", num, "is:", n1, n2, end=" ")
    for a in range(2, num):
        nth = n1 + n2
        n1 = n2
        n2 = nth
        print(nth, end=" ")
    print()


Fibonacci_Series(num, n1, n2)
