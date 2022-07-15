# *Note: please enter numbers in ascending order.*
def Binary_Search(array, low, high, ele):
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < ele:
            low = mid + 1
        elif array[mid] > ele:
            high = mid - 1
        else:
            return mid + 1
    return -1


# take size of array;
len = int(input("Please enter size of Array:"))

# taking elements from user;
array = []
print("Enter the values:")
for a in range(0, len):
    val = int(input())
    array.append(val)

ele = int(input("Enter the number would you like to find: "))
low = 0
high = len-1

result = Binary_Search(array, low, high, ele)
if result != -1:
    print("Given element is found at position:", str(result))
else:
    print("Given element is not found in array.")
