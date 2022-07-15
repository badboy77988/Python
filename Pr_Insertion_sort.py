array = [1, 3, 4, 9, 11]
n = len(array)
# length=int(input("Enter the size of Array: "))
ele = int(input("Enter the element: "))


def Insertion_Sort(array, n, ele):
    i = n - 1
    while array[i]>ele and i>0:
        array[i+1]=array[i]
        i=i-1
    array[i+1]=ele
    n=n+1

Insertion_Sort(array,n,ele)
print(array)