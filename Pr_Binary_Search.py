# *Note: please enter numbers in ascending order.*
# define a function for search element by binary search method using recursion;
def Binary_Search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid + 1
        elif arr[mid] > x:
            return (Binary_Search(arr, low, mid - 1, x))
        else:
            return (Binary_Search(arr, mid + 1, high, x))
    else:
        return 0


array = []
length = int(input("Enter the Number of Total Numbers: "))  # size of array

# taking inputs from user;
print("Enter the Numbers: ")
for a in range(0, length):
    val= int(input())
    array.append(val)


# take input from user to find element in array as ele;
ele = int(input("Enter the number would you like to find from array is:"))

# call Binary_Search function and store its value in res;
res = Binary_Search(array, 0, len(array) - 1, ele)
if res != 0:
    print("Given element'", ele, "'is found at position:", res)
else:
    print("Given element'", ele, "'is not found in array.")
