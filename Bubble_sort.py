def BUBBLE_SORT(arr, len):
    for j in range(len):
        for i in range(0, len - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp


arr = []

len = int(input("Enter the length of array: "))
if (len < 0):
    print("Please enter positive length of Array.")
    # exit()

print("Enter the number: ")
for a in range(0, len):
    ele = int(input())
    arr.append(ele)
print("Array before sorting : ", arr)

BUBBLE_SORT(arr, len)

print("Sorted Array is:", end=" ")
for a in range(len):
    print("%d" % arr[a], end=" ")
