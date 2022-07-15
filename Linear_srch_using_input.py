# #---------------------------First Method for Linear_Search It is valid for only input as a integer--------------------------------------------------------------------------#
# # Function for linear search
# def Lin_Srch(arr,ele):
#     for a in range (0,len(arr)):
#         if(arr[a]==ele):
#             return a+1
#     return 0
#
# print("Enter the elements : ",end=" ")
# arr = list(map(int, input().split()))           # take elements as input from user;
# ele = int(input("Enter the element to find in Array: "))        # take element to find from given array;
#
# # call function to search element;
# srch = Lin_Srch(arr,ele)
# if(srch != 0):
#     print("Your given element ", ele ," at position", srch)
# else:
#     print("Given element ", ele , " is not in Array.")

# # print("Enter the elements : ")
# # for i in range(0,size):
# #     ele = int(input())
# #     arr.append(ele)

#---------------------------Second Method for Linear_Search  It is valid for only input as a integer---------------------------------------------------------------------------#

# Function for Linear_search
def Lin_Srch(arr,ele):
    for i in range(0,len(arr)):
        if(arr[i]==ele):
            return i+1
    return 0


size = int(input("Enter the size of Array : "))
arr = []
print("Enter the elements to the Array : ")
for a in range(0,size):
    ele = int(input())
    arr.append(ele)
print(arr)

ele = int(input("Enter the element do you want to find : "))

search = Lin_Srch(arr,ele)
if(search != 0):
    print("Your given element ", ele, " at position", search)
else:
    print("Given element ", ele , " is not in Array.")

#---------------------------Third Method for Linear_Search  It is valid for input as a integer or string---------------------------------------------------------------------------#

# This is valid for find element of datatype integer and string
# def Lin_Srch(arr,ele):
#     for i in range(0,len(arr)):
#         if(arr[i]==ele):
#             return i+1
#     return 0
#
# size = int(input("Enter the size of Array : "))
# arr = []
# print("Enter the elements to the Array : ")
# for a in range(0,size):
#     ele = input()
#     arr.append(ele)
# print(arr)
#
# ele = input("Enter the element do you want to find : ")
#
# search = Lin_Srch(arr,ele)
# if(search != 0):
#     print("Your given element ", ele, " at position", search)
# else:
#     print("Given element ", ele , " is not in Array.")


