val = input("Enter the value to check it is palindrome or not: ")

# Function to check it is palindrome or not;
def palindrome(val):
   rev = val[::-1]
   if val == rev:
       return 1
   else:
       return 0

# store the value of palindrome function in res;
res = palindrome(val)
if res==1:
    print(val, "is palindrome.")
else:
    print(val, "is not palindrome.")